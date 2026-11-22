[English](../en/GUIDE.md) · [Français](../INSTALLATION.md) · [Deutsch](../de/GUIDE.md) · [Español](../es/GUIDE.md) · [Italiano](../it/GUIDE.md) · [Português](../pt/GUIDE.md)

# Setup, updates and safety

## Before flashing

Use only the supported SL-SWTGW3C8F hardware revision. Check the board, memory and flash layout; a matching SoC alone is insufficient. Keep your own verified stock partition backups and a compatible serial console. Verify connector pinout and electrical levels before connecting: a console cable does not belong in an arbitrary Ethernet port.

Verify the release checksums with `sha256sum -c SHA256SUMS`. Test initramfs in RAM before writing flash. Bootloader commands depend on the device revision; do not guess offsets or overwrite bootloader/identity partitions. The public complete image has not been hardware-boot-tested.

## First access

Management obtains an address from the network's DHCP server. Look for `switch-sodola` in the lease list. For a direct connection, temporarily assign the PC `169.254.1.2/24` and use `https://169.254.1.1/`.

Root is initially locked. Set your own password with `passwd` on the serial console. SSH keys and the self-signed HTTPS certificate are generated per device. Establish certificate trust locally after checking the device identity. Set the correct time before HTTPS downloads.

## Updates and optional services

From this OpenWrt installation, check a matching sysupgrade image using `sysupgrade -T /tmp/image-sysupgrade.bin` and back up your configuration. Continue only if validation succeeds. Never force an incompatible image. Preserved settings override firstboot defaults and must be checked after upgrading.

The daily workflow creates untested upstream candidates; it never flashes your device. This is not a guarantee that every CVE is fixed. Avoid generic firmware updates or global package upgrades on this custom board.

Adblock-fast is installed but disabled. Filtering requires clients to use the configured DNS resolver. tcpdump-mini can capture traffic visible to the CPU; hardware-switched traffic may require validated port mirroring. Keep captures private.

Home Assistant setup instructions and a read-only ACL are provided. End-to-end integration and full port/VLAN control remain untested. No HA account or administrative permission is enabled by default.

Install only the desired language pack, not all 42. Upstream translation coverage varies; English is the fallback.

---

[GitHub](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f) · [Releases](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f/releases)
