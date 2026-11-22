# Sécurité et maintenance

## Mises à jour automatiques : ce qui est automatisé

Le workflow GitHub Actions s'exécute quotidiennement à 03:30 UTC et peut être lancé manuellement. Les exécutions planifiées suivent les sources amont actuelles d'OpenWrt et des feeds, réappliquent les correctifs SODOLA et construisent des candidats. Les références réellement utilisées sont enregistrées dans `resolved-sources.json`.

- Pas de connexion à votre switch depuis GitHub.
- Pas de mot de passe, clé SSH ou adresse de réseau privé dans les secrets du workflow.
- Aucun flash automatique, aucune promotion automatique d'un candidat en release validée.
- Si les patches ne s'appliquent plus ou si la compilation/les contrôles échouent, aucun candidat réussi n'est produit. Consulter l'onglet Actions et configurer ses notifications GitHub selon ses préférences.
- Un rafraîchissement amont peut inclure des correctifs de sécurité et des changements fonctionnels. Ce workflow n'est pas un scanner CVE et ne garantit pas la correction de toutes les vulnérabilités.
- Les artefacts sont conservés 14 jours. GitHub peut suspendre les workflows planifiés d'un dépôt public sans activité pendant une longue période.

Après un essai en RAM et une validation matérielle, le mainteneur peut promouvoir une image, puis l'utilisateur applique la mise à jour depuis LuCI. La procédure de validation doit inclure les liens et le trafic réels, pas uniquement une compilation réussie.

Ne pas utiliser une mise à jour globale `apk upgrade --prune` ou un firmware générique proposé par une intégration HA sur ce profil expérimental. Le noyau, les modules, la description de carte et nos correctifs doivent rester cohérents. Le service officiel ASU ne fournit pas automatiquement ce profil local. Les mises à jour ponctuelles de paquets demandent une vérification de compatibilité et d'espace libre.

## Réglages initiaux

- Root verrouillé, mot de passe à créer physiquement sur console.
- Clés privées/certificat générés sur l'appareil, jamais préchargés.
- Gestion HTTPS sur le LAN de gestion ; pas de publication Internet automatique.
- Routage IPv4/IPv6 désactivé, serveur DHCP/RA désactivé.
- Adblock installé mais désactivé, pas de forçage DNS, vérification TLS des listes activée.
- Pas de règles ou comptes Home Assistant actifs par défaut. Installer un compte dédié quand HA existe, avec les droits nécessaires à ses fonctions.

## Limites

La gestion est autorisée depuis le LAN connecté à la zone de gestion. Isoler ce LAN/VLAN si le réseau accueille des équipements non fiables. Le firmware fournit du code tiers ; la présence de durcissements ne garantit pas l'absence de vulnérabilités.

Les paquets et listes peuvent contacter leurs dépôts externes lorsqu'ils sont explicitement activés. Le thème n'utilise aucun asset externe, aucune vidéo ni police distante. La commutation matérielle peut rendre invisibles à tcpdump des flux qui ne passent pas par le CPU.
