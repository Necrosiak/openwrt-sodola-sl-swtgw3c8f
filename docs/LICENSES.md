# Licences et attributions

- OpenWrt : https://github.com/openwrt/openwrt ; licence globale et composants tels que documentés dans son arbre source.
- Profil SODOLA et correctifs noyau : GPL-2.0-or-later, dérivés du support realtek / Horaco amont. Les marqueurs SPDX et commentaires sont conservés dans les patches.
- LuCI : licences et attributions de chaque composant, sources du feed dans le bundle correspondant.
- Argon 3.1.4 : Jerrykuku et contributeurs, dérivé notamment du thème Material ; Apache-2.0 / MIT selon les fichiers. https://github.com/jerrykuku/luci-theme-argon
- Thème Nekyron : adaptations des templates Apache-2.0 avec notices conservées ; illustrations et icônes SVG locales distribuées avec la même licence du paquet.
- adblock-fast / luci-app-adblock-fast : MOSSDeF / Stan Grishin et contributeurs, AGPL-3.0-or-later.
- Bibliothèques, outils réseau, noyau et firmwares tiers : licences indiquées dans les Makefiles correspondants des sources OpenWrt/feeds. Le manifeste de chaque image liste les composants effectivement embarqués.

Les fichiers publics ne comprennent pas de sauvegarde constructeur ou de partition d'identité d'un appareil particulier. Les clés publiques de signature de paquets peuvent être distribuées ; leurs clés privées ne le sont jamais.
