"""Restore the full, unmodified course CSV after cloning this GitHub folder."""
from pathlib import Path
import hashlib, shutil, zipfile
ROOT=Path(__file__).resolve().parent
target=ROOT/'Datasets/world_cities_pop.csv'
expected='14d45883d3d2426e50054c8777a7bad2fe68e59a6ddbbdb952c6bb68aafa8636'
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
if target.exists():
    if digest(target)!=expected:raise SystemExit('Existing CSV differs. Keep a backup and resolve it before restoring.')
    print('Full dataset already restored; SHA-256 matches.')
else:
    archive=ROOT/'Datasets/world_cities_pop.csv.zip'
    temp=target.with_suffix('.csv.restore-tmp')
    with zipfile.ZipFile(archive) as z:
        if z.namelist()!=['world_cities_pop.csv']:raise SystemExit('Unexpected archive layout')
        with z.open('world_cities_pop.csv') as src,temp.open('wb') as dst:shutil.copyfileobj(src,dst)
    if digest(temp)!=expected:raise SystemExit('Restored dataset checksum failed')
    temp.replace(target)
    print('Restored full CSV; SHA-256 matches: '+expected)
