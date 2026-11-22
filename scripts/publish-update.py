#!/usr/bin/env python3
"""Publish signed update metadata and a candidate/release; never flash a device."""
import argparse,hashlib,json,os,shutil,subprocess,tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__);p.add_argument('artifacts',type=Path)
p.add_argument('--key',type=Path,required=True);p.add_argument('--usign',required=True)
p.add_argument('--unsquashfs',default='unsquashfs');p.add_argument('--channel',choices=['release','candidate'],default='candidate');p.add_argument('--tag')
a=p.parse_args();repo='Necrosiak/openwrt-sodola-sl-swtgw3c8f'
identity=json.loads((a.artifacts/'nekyron-release.json').read_text())
sha=os.environ.get('GITHUB_SHA') or subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
tag=a.tag or 'candidate-'+identity['flavor']+'-'+str(identity['build_id'])+'-'+sha[:8]
public=root/'package/luci-app-nekyron-update/files/usr/share/nekyron-update/release.pub'
fp=lambda flag,path:subprocess.check_output([a.usign,'-F',flag,str(path)],text=True).strip()
if fp('-s',a.key)!=fp('-p',public):raise SystemExit('Signing key does not match the firmware trust anchor')
subprocess.run(['python3',str(root/'scripts/sign-update.py'),str(a.artifacts),'--tag',tag,'--channel',a.channel,'--key',str(a.key),'--usign',a.usign,'--unsquashfs',a.unsquashfs],check=True)
manifest=a.artifacts/('nekyron-update-'+identity['flavor']+'.json')
subprocess.run([a.usign,'-V','-q','-p',str(public),'-m',str(manifest),'-x',str(manifest)+'.sig'],check=True)
(a.artifacts/'SHA256SUMS').write_text(''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.name+'\n' for f in sorted(a.artifacts.iterdir()) if f.is_file() and f.name!='SHA256SUMS'))
with tempfile.TemporaryDirectory() as td:
 notes=Path(td)/'notes.md';notes.write_text('Signed '+a.channel+' firmware for **'+identity['flavor']+'**.\n\nExperimental: successful compilation is not hardware validation. Review before installation. Settings are retained; the switch restarts. No automatic flashing.\n\n[Update guide](https://github.com/'+repo+'/blob/main/docs/UPDATES.md)\n')
 assets=[str(f) for f in sorted(a.artifacts.iterdir()) if f.is_file()]
 subprocess.run(['gh','release','create',tag,*assets,'--repo',repo,'--target',sha,'--prerelease','--title','Nekyron '+identity['version']+' ('+identity['flavor']+')','--notes-file',str(notes)],check=True)
 exists=subprocess.run(['gh','release','view','update-index','--repo',repo],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
 if not exists:
  subprocess.run(['gh','release','create','update-index','--repo',repo,'--target',sha,'--prerelease','--title','Signed firmware update feeds','--notes','Machine-readable signed update feeds. No firmware image is stored here.'],check=True)
 feed=Path(td)/('nekyron-update-'+identity['flavor']+'-'+a.channel+'.json')
 shutil.copyfile(manifest,feed);shutil.copyfile(str(manifest)+'.sig',str(feed)+'.sig')
 subprocess.run(['gh','release','upload','update-index',str(feed),str(feed)+'.sig','--clobber','--repo',repo],check=True)
print('Published signed update feed; no device was modified.')
