# Installation et récupération

## Avant tout flash

Ce firmware cible uniquement **SL-SWTGW3C8F / RTL9303 / 128 Mio RAM / 16 Mio SPI**, avec implantation compatible avec le profil fourni. Vérifier la carte, sa révision et les modules. Les adresses et procédures ci-dessous ne constituent pas une procédure universelle pour tous les chargeurs SODOLA.

1. Prévoir une console série au bon niveau électrique et brochage. Un câble console RJ45 ne se branche pas dans un port Ethernet quelconque. Vérifier le connecteur et les niveaux sur l'appareil avant connexion.
2. Sauvegarder **vos propres** partitions : chargeur, BDINFO, SYSINFO, configuration, firmware et OEMINFO. Stocker les fichiers hors du switch et vérifier leurs tailles/empreintes.
3. Garder le chargeur d'origine et les partitions d'identité intacts. Ne jamais déduire le numéro MTD d'une ancienne capture : les partitions noyau/rootfs modifient la numérotation après flash.
4. Télécharger les fichiers depuis la release, vérifier `sha256sum -c SHA256SUMS`.
5. Tester d'abord l'image initramfs en RAM via le chargeur, sans écriture flash. La méthode exacte dépend de la révision d'U-Boot. Les images ici portent le format Realtek uImage, pas un firmware constructeur universel.

## Premier accès à l'image propre

La connexion réseau de gestion demande une adresse DHCP à la box. Consulter les baux DHCP pour `switch-sodola`. En liaison directe, configurer temporairement le PC en `169.254.1.2/24` et accéder à `https://169.254.1.1/`.

**Root est verrouillé par défaut** : lancer `passwd` depuis la console série pour définir son propre mot de passe. Aucun mot de passe commun n'est fourni. Le certificat auto-signé est propre à chaque appareil ; sa confiance doit être établie localement après contrôle. Régler l'heure avant d'utiliser les téléchargements HTTPS.

Le client DHCP de gestion est actif. Les serveurs DHCP/RA/DNS, SNMP, LLDP, SQM et Adblock sont initialement désactivés. Le filtrage DNS nécessite une activation et un choix explicite des DNS des clients.

## Mise à jour depuis CET OpenWrt

Copier l'image sysupgrade en `/tmp`, vérifier son empreinte, puis :

```sh
sysupgrade -T /tmp/image-sysupgrade.bin
```

Continuer seulement si le contrôle réussit. Sauvegarder la configuration via LuCI. Depuis LuCI, charger l'image et conserver la configuration si elle correspond à cette version. Ne pas utiliser `-F` pour contourner un modèle incompatible. Une configuration conservée n'est pas remplacée par les valeurs par défaut de l'image : DHCP, firewall, thème et services doivent être vérifiés après mise à jour.

L'image publique complète n'a pas encore été démarrée sur matériel. La version précédente a été installée et utilisée sur un exemplaire ; ce statut ne se transfère pas automatiquement à une reconstruction.

## Restauration constructeur

Il faut vos sauvegardes et une méthode de récupération validée sur votre chargeur. Aucune image de flash constructeur issue de l'appareil de développement n'est publiée. Ne jamais écrire une flash complète provenant d'un autre appareil : elle peut contenir MAC, calibration, configuration et identifiants uniques.
