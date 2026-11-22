#!/usr/bin/env python3
"""Prepare pinned public sources, or an explicitly requested upstream candidate."""
import argparse,json,os,re,shutil,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('destination',type=Path);p.add_argument('--rolling',action='store_true');p.add_argument('--upstream-lock',type=Path);a=p.parse_args();dst=a.destination.resolve()
if dst.exists():raise SystemExit('Use an empty destination; existing build trees are never reset.')
lock=json.loads((root/'sources-lock.json').read_text())
upstream=json.loads(a.upstream_lock.read_text()) if a.upstream_lock else None
if upstream is not None:
 if not a.rolling:p.error('--upstream-lock requires --rolling')
 if not isinstance(upstream,dict) or set(upstream)!={'.','packages','luci','routing'} or any(not isinstance(v,str) or not re.fullmatch('[0-9a-f]{40}',v) for v in upstream.values()):p.error('Invalid upstream lock')
def revision(name,default):return upstream[name] if upstream is not None else default
def run(*args,cwd=None):subprocess.run(args,cwd=cwd,check=True)
def clone(url,target,revision):
 target.mkdir(parents=True);run('git','init','-q',str(target));run('git','remote','add','origin',url,cwd=target);run('git','fetch','--depth=1','origin',revision,cwd=target);run('git','checkout','--detach','FETCH_HEAD',cwd=target)
clone('https://github.com/openwrt/openwrt.git',dst,revision('.','main') if a.rolling else lock['.'])
# Fail closed if upstream changes no longer accept the board / PHY patches.
run('git','apply','--check',str(root/'patches/sodola.patch'),cwd=dst)
run('git','apply',str(root/'patches/sodola.patch'),cwd=dst)
urls={'packages':'https://github.com/openwrt/packages.git','luci':'https://github.com/openwrt/luci.git','routing':'https://github.com/openwrt/routing.git'}
for name,url in urls.items():clone(url,dst/'feeds'/name,revision(name,'HEAD') if a.rolling else lock[name])
shutil.copyfile(root/'patches/wget-no-host-paths.patch',dst/'feeds/packages/net/wget/patches/910-no-host-build-paths.patch')
run('git','apply','--check',str(root/'patches/luci-fr-size-placeholders.patch'),cwd=dst/'feeds/luci')
run('git','apply',str(root/'patches/luci-fr-size-placeholders.patch'),cwd=dst/'feeds/luci')
(dst/'feeds.conf').write_text(''.join(f'src-git {n} {u}\n' for n,u in urls.items()))
run('./scripts/feeds','update','-i','packages','luci','routing',cwd=dst)
run('./scripts/feeds','install','-a','-p','luci',cwd=dst)
run('./scripts/feeds','install','lldpd','net-snmp','iperf3','tcpdump-mini','ethtool-full','sqm-scripts','adblock-fast',cwd=dst)
# Unselected LuCI entry can introduce a known fwknop dependency recursion.
fw=dst/'package/feeds/luci/luci-app-fwknopd'
if fw.is_symlink():fw.unlink()
clone('https://github.com/jerrykuku/luci-theme-argon.git',dst/'package/luci-theme-argon',lock['argon'])
shutil.copytree(root/'package/luci-theme-nekyron',dst/'package/luci-theme-nekyron',symlinks=True)
shutil.copytree(root/'package/luci-app-nekyron-https',dst/'package/luci-app-nekyron-https',symlinks=True)
shutil.copytree(root/'config/files',dst/'files',symlinks=True)
shutil.copyfile(root/'config/config.seed',dst/'.config')
run('make','defconfig',cwd=dst)
actual={n:subprocess.check_output(['git','rev-parse','HEAD'],cwd=(dst if n=='.' else dst/'feeds'/n),text=True).strip() for n in ('.',*urls)}
actual['argon']=lock['argon'];actual['rolling']=a.rolling
(dst/'resolved-sources.json').write_text(json.dumps(actual,indent=2)+'\n')
print('Prepared',dst)
