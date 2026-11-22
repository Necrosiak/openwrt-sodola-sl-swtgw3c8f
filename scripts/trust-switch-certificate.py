#!/usr/bin/env python3
"""Trust one independently verified switch certificate in the user's NSS DB."""
import argparse, ipaddress, pathlib, subprocess
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('certificate',type=pathlib.Path,help='Public PEM/DER certificate downloaded over authenticated SSH or otherwise verified')
p.add_argument('--host',required=True,help='Actual administration IP address or DNS name')
p.add_argument('--nickname',default='Nekyron switch HTTPS')
p.add_argument('--nss-db',type=pathlib.Path)
a=p.parse_args()
cert=a.certificate.resolve()
def run(*args):return subprocess.run(args,check=True)
run('openssl','x509','-in',str(cert),'-noout','-subject','-dates','-fingerprint','-sha256','-checkend','0')
try:ipaddress.ip_address(a.host);check='-checkip'
except ValueError:check='-checkhost'
run('openssl','x509','-in',str(cert),'-noout',check,a.host)
run('openssl','verify','-CAfile',str(cert),'-purpose','sslserver',str(cert))
# Pin this server certificate as a trusted peer, not as a general-purpose CA.
db=a.nss_db or (pathlib.Path.home()/'.pki/nssdb' if (pathlib.Path.home()/'.pki/nssdb/cert9.db').exists() else pathlib.Path.home()/'.local/share/pki/nssdb')
if not (db/'cert9.db').is_file():p.error('NSS database not found; open your Chromium-based browser first or specify --nss-db.')
run('certutil','-A','-d','sql:'+str(db),'-n',a.nickname,'-t','P,,','-i',str(cert))
print('Trusted this certificate only. Restart the browser if needed. Re-import after renewal.')
