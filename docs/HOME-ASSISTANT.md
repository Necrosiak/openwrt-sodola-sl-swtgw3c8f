# Home Assistant

## Choix d'intégration

L'intégration officielle [OpenWrt ubus](https://www.home-assistant.io/integrations/ubus/) vise principalement la détection de présence via hostapd sur un point d'accès Wi-Fi. Elle ne constitue pas une administration complète du switch Ethernet.

L'intégration communautaire [FaserF/ha-openwrt](https://github.com/FaserF/ha-openwrt), installée côté Home Assistant, documente des capteurs, reboot, services, sauvegardes, exécution de commandes et lecture/écriture UCI. Le switch possède déjà `uhttpd-mod-ubus` et `rpcd` ; aucun gros agent supplémentaire n'est nécessaire pour ce protocole.

**Compatibilité non validée de bout en bout avec cette carte.** Il faut un HA installé pour réaliser l'association et les tests. Les fonctions Wi-Fi/PoE ne s'appliquent pas automatiquement à un appareil sans ces équipements. L'état des huit ports et les VLAN peuvent nécessiter des capteurs et actions spécifiques ; l'existence de `uci_set` ne fournit pas, à elle seule, un écran complet de gestion des VLAN.

## Mise en place future

1. Installer HA et l'intégration choisie, noter l'adresse du serveur.
2. Créer un compte rpcd dédié localement avec un mot de passe propre. Ne pas publier celui-ci dans YAML, Git ou dans une capture d'écran.
3. Commencer par le profil ACL de lecture `home-assistant/ha-nekyron-read.json`. Adapter ce profil aux appels de la version d'intégration utilisée. Les permissions non listées seront refusées : ce modèle n'est pas un installateur universel.
4. Vérifier identité système, mémoire, uptime, vitesse et état des liens.
5. Ajouter seulement les opérations nécessaires. Les modifications UCI du réseau et l'exécution arbitraire de commandes sont des droits administrateur sensibles : les activer explicitement dans un profil séparé, pas par défaut.
6. Tester les opérations non destructives puis les commandes réversibles, avec accès console de secours.

Pour une administration complète, on peut construire des actions HA autour d'UCI/ubus/SSH. La validation de modifications de ports/VLAN doit éviter de couper le lien de gestion. Conserver LuCI comme accès complet de référence. Pas de mise à jour générique du firmware depuis HA : utiliser une image construite par ce projet et testée sur matériel.

Le projet n'embarque aucun compte HA prédéfini, jeton MQTT, mot de passe partagé ni adresse de serveur. Aucun port supplémentaire n'est ouvert pour HA au premier démarrage.
