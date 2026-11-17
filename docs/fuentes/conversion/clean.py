import re,sys
src,dst,header=sys.argv[1],sys.argv[2],sys.argv[3]
t=open(src,encoding='utf-8').read()
# markers like [►M1](url "x") / [▼B](...) -> plain
t=re.sub(r'\[([►▼◄][A-Z]?\d*[A-Z]?\d*)\]\([^)]*\)',r'\1',t)
t=t.replace('\u00a0',' ').replace('\\(','(').replace('\\)',')')
t=re.sub(r' (bis|ter|quater) \)',r' \1)',t)
t=re.sub(r'^(\(\d+\))\n\n(?=\S)',r'\1 ',t,flags=re.M)
lines=[l.rstrip() for l in t.split('\n')]
out=[];i=0
def nxt(j):
    while j<len(lines) and not lines[j].strip(): j+=1
    return j
while i<len(lines):
    l=lines[i].strip()
    m=re.fullmatch(r'(\d+|[a-z]|[ivx]+)\)?\.?',l) if l else None
    if l and re.fullmatch(r'(\d+( bis| ter| quater)?[.)]|\([a-z0-9]+\)|[a-z]( bis| ter| quater)?\)|[ivx]+\))',l):
        j=nxt(i+1)
        if j<len(lines): out.append(l+' '+lines[j].strip()); i=j+1; continue
    if re.fullmatch(r'(CAPÍTULO [IVXLC]+|TÍTULO [IVXLC]+)',l):
        j=nxt(i+1); out.append('\n## '+l+' — '+lines[j].strip()); i=j+1; continue
    if re.fullmatch(r'(SECCIÓN \d+|Sección \d+)',l):
        j=nxt(i+1); out.append('\n### '+l+' — '+lines[j].strip()); i=j+1; continue
    if re.fullmatch(r'Artículo \d+( bis| ter| quater| quinquies)?',l):
        j=nxt(i+1); out.append('\n#### '+l+' — '+lines[j].strip()); i=j+1; continue
    if re.fullmatch(r'ANEXO [IVXLC]+',l):
        j=nxt(i+1); out.append('\n## '+l+' — '+lines[j].strip()); i=j+1; continue
    out.append(lines[i]); i+=1
t='\n'.join(out)
t=re.sub(r'\n{3,}','\n\n',t)
open(dst,'w',encoding='utf-8').write(header+'\n\n'+t.strip()+'\n')
