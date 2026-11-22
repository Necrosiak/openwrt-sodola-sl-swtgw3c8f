# Adblock et capture réseau

## Adblock-fast

Le paquet et son interface LuCI sont intégrés mais désactivés. Les DNS/DHCP de l'installation ne sont pas modifiés par l'installation du firmware.

Le blocage DNS n'agit que sur les appareils qui utilisent le résolveur configuré. Brancher le switch entre la box et le NAS ne force pas les clients à utiliser son DNS. Pour utiliser ce service, organiser le DNS distribué par DHCP ou configurer volontairement les clients. Le rôle DHCP peut rester à la box.

Démarrer avec une petite liste et un cache en RAM, éviter de remplir la flash. Les listes ont un coût en RAM même si le générateur Adblock ne reste pas en tâche de fond. Un DNS filtrant sur un NAS/serveur est une alternative si les besoins sont importants.

Documentation : https://docs.mossdef.org/adblock-fast/

## Capture légère pour Wireshark

`tcpdump-mini` est inclus. Wireshark s'exécute sur le PC, sans interface graphique lourde sur le switch. Exemple pour capturer au maximum 200 paquets destinés au CPU, depuis une machine autorisée :

```sh
ssh root@SWITCH 'tcpdump -i switch.1 -U -s 256 -c 200 -w -' > capture.pcap
```

Adapter `switch.1` à l'interface réelle (`ip link`). La capture contient potentiellement des données privées : la garder localement, jamais dans un rapport public sans nettoyage.

La commutation matérielle peut contourner le CPU. Une capture sur une interface de gestion ne représente donc pas forcément tous les flux entre ports. Le mirroring matériel doit être testé sur cette carte avant de promettre une capture exhaustive. Ne pas désactiver la commutation matérielle pour faire traverser 10 Gb/s au CPU.
