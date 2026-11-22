#!/usr/bin/env python3
"""Reject credentials, captured traffic and instance config in public overlays."""
import argparse,re,base64
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--tree',type=Path,required=True);p.add_argument('--build',type=Path);a=p.parse_args()
problems=[]
# Public source docs can discuss these files; never ship the instance files.
for base in [a.tree/'config/files',a.tree/'package']+([a.build/'files',a.build/'build_dir/target-mips_24kc_musl/root-realtek'] if a.build else []):
 if not base.exists():continue
 for f in base.rglob('*'):
  if f.is_symlink() or not f.is_file():continue
  rel=f.relative_to(base).as_posix();d=f.read_bytes()
  if re.search(r'(^|/)(authorized_keys|known_hosts|dropbear_[^/]*_host_key|id_rsa|id_ed25519|uhttpd\.(?:key|crt)(?:\.[^/]*)?|tailscaled\.state|nekyron-https\.state)$',rel):problems.append(rel+': instance credential')
  if f.suffix=='.sec':problems.append(rel+': signing secret')
  if d.startswith(b'untrusted comment:'):
   try:
    packet=base64.b64decode(d.splitlines()[1],validate=True)
    if packet.startswith(b'Ed') and len(packet)==104:problems.append(rel+': usign signing secret')
   except (ValueError,IndexError):pass
  if f.suffix in ('.pcap','.pcapng'):problems.append(rel+': packet capture')
  if re.search(rb'-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----[\r\n]+[A-Za-z0-9+/=\r\n]{64,}-----END ',d):problems.append(rel+': private key')
  if f.name=='shadow':
   for line in d.decode().splitlines():
    val=line.split(':')[1]
    if val and val not in ('!','!!','*','!*','x'):problems.append(rel+': preset password hash')
  if rel.startswith('etc/config/'):
   for line in d.splitlines():
    m=re.match(rb"\s*option\s+(?:password|secret|token)\s+['\"]?([^'\"\s]+)",line)
    if m and not m.group(1).startswith(b'$p$'):problems.append(rel+': preset secret')
if problems:raise SystemExit('\n'.join(problems))
print('Public overlay credential audit: OK (not a general vulnerability scanner)')
