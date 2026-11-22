#!/usr/bin/env python3
"""Resolve public upstream commits and fingerprint them with this recipe revision."""
import argparse, concurrent.futures, hashlib, json, re, subprocess
from pathlib import Path
SOURCES={'.':('https://github.com/openwrt/openwrt.git','refs/heads/main'),
 'packages':('https://github.com/openwrt/packages.git','HEAD'),
 'luci':('https://github.com/openwrt/luci.git','HEAD'),
 'routing':('https://github.com/openwrt/routing.git','HEAD')}
def resolve(item):
 name,(url,ref)=item
 result=subprocess.check_output(['git','ls-remote','--exit-code',url,ref],text=True,timeout=60)
 sha=result.split()[0]
 if not re.fullmatch('[0-9a-f]{40}',sha):raise ValueError('Invalid upstream commit: '+name)
 return name,sha
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('output',type=Path);a=p.parse_args()
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:state=dict(pool.map(resolve,SOURCES.items()))
 recipe=subprocess.check_output(['git','rev-parse','HEAD'],cwd=Path(__file__).resolve().parents[1],text=True).strip()
 fingerprint=hashlib.sha256(json.dumps({'sources':state,'recipe':recipe},sort_keys=True).encode()).hexdigest()
 a.output.write_text(json.dumps(state,indent=2)+'\n')
 print('fingerprint='+fingerprint)
if __name__=='__main__':main()
