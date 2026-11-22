#!/usr/bin/env python3
import hashlib,json,shutil,sys,struct,zlib,lzma
from pathlib import Path
b=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
images=b/'bin/targets/realtek/rtl930x';report={'hardware_tested':False,'variant':'public clean image','images':{}}
for suffix in ('initramfs-kernel.bin','squashfs-sysupgrade.bin'):
 p=next(images.glob('*sodola*'+suffix));d=p.read_bytes();h=struct.unpack('>7I4B32s',d[:64]);hdr=bytearray(d[:64]);hdr[4:8]=b'\0'*4
 assert h[0]==0x83800000 and zlib.crc32(hdr)&0xffffffff==h[1]
 assert zlib.crc32(d[64:64+h[3]])&0xffffffff==h[6]
 raw=lzma.decompress(d[64:64+h[3]])
 assert h[4]+len(raw)<0x83f00000
 if suffix.startswith('squashfs'):assert len(d)<0xc00000 and h[4]+len(raw)<0x81000000
 else:assert 0x84000000+len(d)<0x88000000
 shutil.copyfile(p,out/p.name);report['images'][p.name]={'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'header_crc_ok':True,'payload_crc_ok':True}
for name in ('config.buildinfo','feeds.buildinfo','version.buildinfo'):
 if (images/name).exists():shutil.copyfile(images/name,out/name)
for p in images.glob('*sodola*.manifest'):shutil.copyfile(p,out/p.name)
if (b/'resolved-sources.json').exists():shutil.copyfile(b/'resolved-sources.json',out/'resolved-sources.json')
(out/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
(out/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in sorted(out.iterdir()) if p.is_file() and p.name!='SHA256SUMS'))
print(json.dumps(report,indent=2))
