"""Hash downloaded light curves without fetching or redistributing upstream data."""
import argparse,csv,hashlib,json,pathlib

def manifest(rows,root):
    base=pathlib.Path(root).resolve(); out=[]
    for r in rows:
        p=(base/r['cache_path']).resolve()
        if not p.is_relative_to(base): raise ValueError('cache path escapes cache root')
        if not p.is_file(): raise ValueError('missing cache file')
        if not r['source_url'].startswith('https://'): raise ValueError('HTTPS provenance required')
        if not r['sector'].isdigit(): raise ValueError('sector must be a positive integer')
        if int(r['sector'])<1: raise ValueError('sector must be positive')
        out.append(dict(r,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
    return out
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('input');a.add_argument('cache');a.add_argument('output');p=a.parse_args()
    with open(p.input) as f:rows=list(csv.DictReader(f))
    pathlib.Path(p.output).write_text(json.dumps(manifest(rows,p.cache),indent=2)+'\n')
