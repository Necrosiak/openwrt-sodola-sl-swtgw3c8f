[English](../en/GUIDE.md) · [Français](../INSTALLATION.md) · [Deutsch](../de/GUIDE.md) · [Español](../es/GUIDE.md) · [Italiano](../it/GUIDE.md) · [Português](../pt/GUIDE.md)

# Installazione, aggiornamenti e sicurezza

## Prima di installare

Usare solo hardware SL-SWTGW3C8F compatibile. Controllare scheda, memoria e partizioni flash. Conservare copie verificate delle proprie partizioni originali e una console seriale compatibile. Verificare piedinatura e livelli elettrici: non collegare il cavo console a una porta Ethernet qualsiasi.

Verificare le somme della release con `sha256sum -c SHA256SUMS`. Provare prima initramfs in RAM. I comandi del bootloader dipendono dalla revisione. Non indovinare indirizzi e non sovrascrivere bootloader o partizioni di identità. L’immagine pubblica completa non è ancora stata avviata su hardware reale.

## Primo accesso

La gestione riceve un indirizzo dal server DHCP della rete. Cercare `switch-sodola` nei lease. Per un collegamento diretto, assegnare temporaneamente `169.254.1.2/24` al PC e aprire `https://169.254.1.1/`.

Root è inizialmente bloccato. Impostare una password personale con `passwd` dalla console seriale. Chiavi SSH e certificato HTTPS autofirmato vengono generati per ogni dispositivo. Verificare l’identità prima di considerare attendibile il certificato. Impostare l’ora prima dei download HTTPS.

## Aggiornamenti e funzioni opzionali

Da questo OpenWrt, controllare un’immagine compatibile con `sysupgrade -T /tmp/image-sysupgrade.bin` e salvare la configurazione. Continuare solo se il controllo riesce. Non forzare immagini incompatibili. Verificare le impostazioni conservate dopo l’aggiornamento.

Il workflow giornaliero genera candidati non testati; non installa firmware sullo switch e non garantisce la correzione di tutte le CVE. Evitare aggiornamenti generici del firmware o globali dei pacchetti su questa scheda personalizzata.

Adblock-fast è disattivato. I client devono usare il suo resolver DNS per essere filtrati. tcpdump-mini potrebbe non vedere il traffico commutato direttamente dall’hardware. Il mirroring delle porte deve essere convalidato; mantenere private le catture.

Home Assistant: istruzioni e ACL di sola lettura sono disponibili. Integrazione completa e controllo porte/VLAN non sono convalidati. Nessun account HA o nuovo permesso amministrativo è attivo per impostazione predefinita.

Installare solo la lingua desiderata. Le traduzioni mancanti vengono mostrate in inglese.

---

[GitHub](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f) · [Releases](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f/releases)
