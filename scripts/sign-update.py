#!/usr/bin/env python3
"""Sign a board/profile-specific update manifest; never embeds the private key."""
import argparse,hashlib,json,lzma,re,struct,subprocess,zlib
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('artifacts',type=Path);p.add_argument('--tag',required=True);p.add_argument('--channel',choices=['release','candidate'],required=True)
p.add_argument('--unsquashfs',default='unsquashfs');p.add_argument('--key',type=Path,required=True);p.add_argument('--usign',default='usign');a=p.parse_args()
if not re.fullmatch('[A-Za-z0-9._-]+',a.tag):p.error('Invalid release tag')
i=json.loads((a.artifacts/'nekyron-release.json').read_text())
if i.get('board')!='sodola,sl-swtgw3c8f' or i.get('flavor') not in ('full','tailscale-lite') or i.get('contract')!=1 or not isinstance(i.get('build_id'),int):p.error('Unsupported image identity')
name='openwrt-realtek-rtl930x-sodola_sl-swtgw3c8f-squashfs-sysupgrade.bin';d=(a.artifacts/name).read_bytes()
if not 1048576<len(d)<0xc00000:p.error('Image exceeds the firmware partition')
h=struct.unpack('>7I4B32s',d[:64]);head=bytearray(d[:64]);head[4:8]=b'\0'*4
if h[0]!=0x83800000 or zlib.crc32(head)&0xffffffff!=h[1] or zlib.crc32(d[64:64+h[3]])&0xffffffff!=h[6]:p.error('Invalid image header/CRC')
if h[4]+len(lzma.decompress(d[64:64+h[3]]))>=0x81000000:p.error('Image overlaps reserved RAM')
offset=d.find(b'hsqs')
if offset<0:p.error('Missing squashfs')
embedded=json.loads(subprocess.check_output([a.unsquashfs,'-cat','-o',str(offset),str(a.artifacts/name),'etc/nekyron-release.json'],stderr=subprocess.DEVNULL))
if embedded!=i:p.error('Artifact identity does not match the image rootfs')
m={**i,'tag':a.tag,'channel':a.channel,'size':len(d),'sha256':hashlib.sha256(d).hexdigest(),'url':'https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f/releases/download/'+a.tag+'/'+name}
f=a.artifacts/('nekyron-update-'+i['flavor']+'.json');f.write_text(json.dumps(m,sort_keys=True,indent=2)+'\n')
subprocess.run([a.usign,'-S','-s',str(a.key),'-m',str(f),'-x',str(f)+'.sig','-c','Nekyron firmware update'],check=True)
print(str(f))
