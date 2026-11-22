[English](../en/GUIDE.md) · [Français](../INSTALLATION.md) · [Deutsch](../de/GUIDE.md) · [Español](../es/GUIDE.md) · [Italiano](../it/GUIDE.md) · [Português](../pt/GUIDE.md)

# Einrichtung, Updates und Sicherheit

## Vor dem Flashen

Nur die unterstützte SL-SWTGW3C8F-Hardware verwenden. Platine, Speicher und Flash-Aufteilung prüfen. Eigene verifizierte Sicherungen der Originalpartitionen und eine passende serielle Konsole bereithalten. Pinbelegung und elektrische Pegel vor dem Anschluss prüfen; ein Konsolenkabel gehört nicht in einen beliebigen Ethernet-Port.

Release-Prüfsummen mit `sha256sum -c SHA256SUMS` prüfen. Zuerst initramfs im RAM testen. Die Bootloader-Befehle hängen von der Revision ab. Keine Offsets erraten und keine Bootloader- oder Identitätspartitionen überschreiben. Das vollständige öffentliche Image wurde noch nicht auf Hardware gestartet.

## Erster Zugriff

Die Verwaltung erhält eine Adresse vom DHCP-Server des Netzwerks. In der Lease-Liste nach `switch-sodola` suchen. Für eine Direktverbindung dem PC vorübergehend `169.254.1.2/24` zuweisen und `https://169.254.1.1/` öffnen.

Root ist anfangs gesperrt. Über die serielle Konsole mit `passwd` ein eigenes Passwort setzen. SSH-Schlüssel und selbstsigniertes HTTPS-Zertifikat werden pro Gerät erzeugt. Vertrauen erst nach Prüfung der Geräteidentität herstellen. Vor HTTPS-Downloads die Uhrzeit einstellen.

## Updates und Zusatzfunktionen

Unter diesem OpenWrt ein passendes Image mit `sysupgrade -T /tmp/image-sysupgrade.bin` prüfen und die Konfiguration sichern. Nur bei erfolgreicher Prüfung fortfahren. Keine inkompatible Aktualisierung erzwingen. Beibehaltene Einstellungen nach dem Update kontrollieren.

Der tägliche Workflow erstellt ungetestete Kandidaten und flasht kein Gerät. Er garantiert nicht die Behebung aller CVEs. Generische Firmware-Updates und globale Paket-Upgrades sind für dieses angepasste Board ungeeignet.

Adblock-fast bleibt deaktiviert, bis es bewusst eingerichtet wird. Clients müssen den zugehörigen DNS-Resolver verwenden. tcpdump-mini sieht nicht zwingend den direkt in Hardware vermittelten Verkehr. Port-Mirroring muss geprüft werden; Mitschnitte privat halten.

Home Assistant: Anleitung und Nur-Lese-ACL sind vorbereitet. Vollständige Port-/VLAN-Steuerung ist noch nicht getestet; keine HA-Zugangsdaten oder neuen Rechte sind voreingestellt.

Nur das gewünschte Sprachpaket installieren. Fehlende Übersetzungen erscheinen auf Englisch.

---

[GitHub](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f) · [Releases](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f/releases)
