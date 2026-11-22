# Nekyron OpenWrt — SODOLA SL-SWTGW3C8F

Community experimental firmware for **SL-SWTGW3C8F / RTL9303 / 8 × SFP+ / 128 MiB RAM / 16 MiB SPI flash**. Not an official OpenWrt or SODOLA release. Other switches sharing the same SoC are not automatically compatible.

The public build includes the local board profile and QINIYEK / RTL8261BE fixes, LuCI HTTPS, the lightweight green Nekyron theme, disabled Adblock-fast, and packet/network diagnostic tools. Management uses the upstream network's DHCP. A direct maintenance address is available at `169.254.1.1/24`.

**No shared root password. Serial access is required to set your own password with `passwd`.** Keys and certificates are generated on each device. No private device backups, captured traffic, MAC addresses or household network settings are distributed.

[Downloads](../../releases) · [French documentation](README.md) · [Installation](docs/INSTALLATION.md) · [Build](docs/BUILD.md) · [Security refresh](docs/SECURITY.md) · [Home Assistant](docs/HOME-ASSISTANT.md) · [Languages](docs/LANGUAGES.md)

## Validation boundary

The earlier kernel/platform build was booted in RAM and flash on one device; management DHCP and a 1 Gb/s link were tested, and negotiated 2.5 / 10 Gb/s links were observed. The newly rebuilt complete public image **has not been booted on hardware**. Compilation, image CRC, size, firstboot configuration emulation and privacy checks do not establish full hardware compatibility or line-rate switching.

Test initramfs in RAM before flashing and keep your own verified stock backups. Never force an incompatible sysupgrade image. Do not use generic automatic firmware upgrades on this custom board.

## Updates and languages

GitHub Actions prepares an upstream candidate daily and can run pinned builds manually. Patch conflicts fail the build. There is **no automatic flashing or stable release promotion**, and no guarantee that every CVE is fixed. Review Actions results and validate hardware before installing candidates.

English is the source language; French is embedded. The release provides 42 LuCI language packs as separate APKs so users can install their own language without consuming flash for all translations. Functional theme labels use native LuCI catalogs; upstream translation completeness varies.

## Build

Install OpenWrt build prerequisites on Linux, then:

```sh
JOBS=4 scripts/build.sh "$PWD/build"
python3 scripts/audit.py --tree . --build build
python3 scripts/collect.py build artifacts
```

The source lock, patches, package sources and corresponding-source release bundle allow reconstruction. Builds are not claimed to be byte-identical. [Licenses and upstream attribution](docs/LICENSES.md).
