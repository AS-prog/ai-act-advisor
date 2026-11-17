"""Lector mínimo de YAML en bloque, sin dependencias.

Cubre lo que usan los ficheros de configuración habituales y la base de
conocimiento del plugin: mapas y listas en bloque, listas y mapas en línea
sencillos, cadenas con o sin comillas, comentarios, booleanos, nulos, números
y escalares de bloque (| y >). No cubre anclas, etiquetas ni documentos
múltiples: si algo no se entiende, se devuelve como cadena.
"""

import re

__all__ = ["loads", "load"]


def _strip_comment(line):
    out, quote = [], None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in ("'", '"'):
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def _split_inline(body):
    parts, depth, quote, cur = [], 0, None, []
    for ch in body:
        if quote:
            cur.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ("'", '"'):
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append("".join(cur).strip())
            cur = []
            continue
        cur.append(ch)
    if "".join(cur).strip():
        parts.append("".join(cur).strip())
    return parts


def _scalar(text):
    t = text.strip()
    if t == "":
        return None
    if len(t) >= 2 and t[0] == t[-1] and t[0] in ("'", '"'):
        return t[1:-1]
    if t.startswith("[") and t.endswith("]"):
        return [_scalar(p) for p in _split_inline(t[1:-1])]
    if t.startswith("{") and t.endswith("}"):
        d = {}
        for p in _split_inline(t[1:-1]):
            k, _, v = p.partition(":")
            d[_scalar(k)] = _scalar(v)
        return d
    low = t.lower()
    if low in ("null", "~"):
        return None
    if low == "true":
        return True
    if low == "false":
        return False
    if re.fullmatch(r"-?\d+", t):
        return int(t)
    if re.fullmatch(r"-?\d+\.\d+", t):
        return float(t)
    return t


_KEY = re.compile(r"""^("[^"]*"|'[^']*'|[^:'"\s][^:]*?)\s*:(?:\s+(.*)|$)""")


class _Parser:
    def __init__(self, text):
        self.lines = []
        raw = text.splitlines()
        i = 0
        while i < len(raw):
            line = raw[i].replace("\t", "  ")
            if line.strip() in ("---", "...") and not line.startswith(" "):
                i += 1
                continue
            content = _strip_comment(line)
            if content.strip():
                indent = len(content) - len(content.lstrip(" "))
                self.lines.append([indent, content.strip(), i])
            i += 1
        self.raw = raw

    def parse(self):
        if not self.lines:
            return None
        value, _ = self._block(0, self.lines[0][0])
        return value

    def _block(self, idx, indent):
        if idx >= len(self.lines):
            return None, idx
        content = self.lines[idx][1]
        if content == "-" or content.startswith("- "):
            return self._seq(idx, indent)
        if _KEY.match(content):
            return self._map(idx, indent)
        return _scalar(content), idx + 1

    def _seq(self, idx, indent):
        out = []
        while idx < len(self.lines):
            ind, content, _ = self.lines[idx]
            if ind != indent or not (content == "-" or content.startswith("- ")):
                break
            rest = content[1:]
            item = rest.strip()
            if item == "":
                if idx + 1 < len(self.lines) and self.lines[idx + 1][0] > indent:
                    value, idx = self._block(idx + 1, self.lines[idx + 1][0])
                else:
                    value, idx = None, idx + 1
                out.append(value)
                continue
            new_indent = indent + 1 + (len(rest) - len(rest.lstrip(" ")))
            if _KEY.match(item) and not item.startswith(("[", "{", '"', "'")):
                self.lines[idx] = [new_indent, item, self.lines[idx][2]]
                value, idx = self._map(idx, new_indent)
            else:
                value, idx = _scalar(item), idx + 1
            out.append(value)
        return out, idx

    def _block_scalar(self, idx, indent, style):
        start = self.lines[idx][2] + 1
        collected, j = [], start
        while j < len(self.raw):
            line = self.raw[j]
            if line.strip() and (len(line) - len(line.lstrip(" "))) <= indent:
                break
            collected.append(line.strip())
            j += 1
        while idx + 1 < len(self.lines) and self.lines[idx + 1][2] < j:
            idx += 1
        text = ("\n" if style == "|" else " ").join(collected).strip()
        return text, idx + 1

    def _map(self, idx, indent):
        out = {}
        while idx < len(self.lines):
            ind, content, _ = self.lines[idx]
            if ind != indent or content.startswith("- ") or content == "-":
                break
            m = _KEY.match(content)
            if not m:
                break
            key = _scalar(m.group(1))
            rest = (m.group(2) or "").strip()
            if rest in ("|", ">", "|-", ">-", "|+", ">+"):
                out[key], idx = self._block_scalar(idx, indent, rest[0])
                continue
            if rest:
                out[key] = _scalar(rest)
                idx += 1
                continue
            nxt = idx + 1
            if nxt < len(self.lines) and self.lines[nxt][0] > indent:
                out[key], idx = self._block(nxt, self.lines[nxt][0])
            elif nxt < len(self.lines) and self.lines[nxt][0] == indent and (
                self.lines[nxt][1].startswith("- ") or self.lines[nxt][1] == "-"
            ):
                out[key], idx = self._seq(nxt, indent)
            else:
                out[key], idx = None, nxt
        return out, idx


def loads(text):
    """Convierte un texto YAML en estructuras de Python. Ante un error, None."""
    try:
        return _Parser(text).parse()
    except Exception:  # noqa: BLE001 - un YAML raro no debe romper un hook
        return None


def load(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return loads(fh.read())
