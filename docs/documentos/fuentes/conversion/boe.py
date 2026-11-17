import sys,re,xml.etree.ElementTree as ET
src,dst,header=sys.argv[1:4]
root=ET.parse(src).getroot()
out=[header,'']
pend=None
for b in root.iter('bloque'):
    vs=b.findall('version')
    if not vs: continue
    v=vs[-1]
    for el in v:
        txt=''.join(el.itertext()).strip()
        if not txt: continue
        c=el.get('class','')
        if el.tag in('h4','h5') or c in('articulo',): out.append('\n#### '+txt+'\n')
        elif c in('titulo_num','capitulo_num'): pend=('## ' if c[0]=='t' else '### ')+txt
        elif c in('titulo_tit','capitulo_tit'): out.append('\n'+(pend+' — ' if pend else '## ')+txt+'\n'); pend=None
        elif c.startswith('seccion'): out.append('\n### '+txt+'\n')
        elif el.tag=='table': out.append('[tabla: '+re.sub(r'\s+',' ',txt)+']\n')
        else: out.append(txt+'\n')
open(dst,'w',encoding='utf-8').write(re.sub(r'\n{3,}','\n\n','\n'.join(out)))
