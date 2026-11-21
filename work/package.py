from pathlib import Path
from html.parser import HTMLParser
import json,zipfile,hashlib

root=Path(__file__).resolve().parent.parent
files=('index.html','README.md','CLAUDE.md','BRIEF.md','work/SOURCES.json','work/COVERAGE_AUDIT.md','work/coverage.json','work/BUDEJOVICE.md','work/BUDEJOVICE-AUDIT.md','work/BUDEJOVICE-ARCHIV-6393.md','work/BUDEJOVICE-MAPA-ZADANI-6393.md','work/BUDEJOVICE-MAPA-PUVODNI-PDF.md','work/BUDEJOVICE-2019-2022-ULOHY.csv')
checks=json.loads((root/'tmp/check-results.json').read_text(encoding='utf-8'))
assert checks['status']=='PASS'
class Structure(HTMLParser):
    def __init__(self): super().__init__();self.ids=[];self.external_assets=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag in ('script','img','iframe','link') and (a.get('src') or a.get('href')):self.external_assets.append(a)
p=Structure();p.feed((root/'index.html').read_text(encoding='utf-8'))
assert len(p.ids)==len(set(p.ids)),'Duplicate DOM IDs'
assert not p.external_assets,'Unexpected external dependency'
dest=root/'outputs/studijni-kvizy-v2.39.0';dest.mkdir(parents=True,exist_ok=True)
for name in files:
    (dest/name).parent.mkdir(parents=True,exist_ok=True)
    (dest/name).write_bytes((root/name).read_bytes())
archive=root/'outputs/studijni-kvizy-v2.39.0.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for name in files:z.write(dest/name,arcname=dest.name+'/'+name)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(files)
    for name in files:assert z.read(dest.name+'/'+name)==(root/name).read_bytes()
result=dict(status='PASS',version='2.39.0',archive=str(archive),bytes=archive.stat().st_size,sha256=hashlib.sha256((root/'index.html').read_bytes()).hexdigest(),uniqueDOMIds=len(p.ids),externalAssets=0,zipIntegrity=True)
(root/'tmp/package-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
