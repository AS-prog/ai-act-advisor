import sys
from bs4 import BeautifulSoup
src,dst=sys.argv[1:3]
soup=BeautifulSoup(open(src,encoding='utf-8').read(),'lxml')
tables=soup.find_all('table')
for t in reversed(tables):
    if t.parent is None: continue
    rows=t.find_all('tr',recursive=False) or [tr for tb in t.find_all(['tbody','thead'],recursive=False) for tr in tb.find_all('tr',recursive=False)]
    box=soup.new_tag('div')
    for r in rows:
        cells=r.find_all(['td','th'],recursive=False)
        if not cells: continue
        first=cells[0].get_text(' ',strip=True)
        if len(cells)>=2 and len(first)<=12:
            d=soup.new_tag('div')
            p=soup.new_tag('p'); p.string=first
            d.append(p)
            for c in cells[1:]:
                for ch in list(c.contents): d.append(ch)
            box.append(d)
        else:
            for c in cells:
                d=soup.new_tag('div')
                for ch in list(c.contents): d.append(ch)
                box.append(d)
    t.replace_with(box)
open(dst,'w',encoding='utf-8').write(str(soup))
