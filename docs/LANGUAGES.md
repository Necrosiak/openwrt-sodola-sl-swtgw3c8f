# Langues / Languages

English is the source language; French is embedded. The release also provides the 42 language packs supported by the pinned LuCI version, for installation **one language at a time**. Upstream translation coverage varies; untranslated strings fall back to English.

Les libellés fonctionnels du thème utilisent les traductions natives de LuCI : réseau, vue d'ensemble, interfaces, ports, états et raccourcis. Les marques, références matérielles et acronymes LAN/NAS/GbE ne sont pas traduits. Les illustrations ne contiennent pas de phrases propres à une langue.

Toutes les traductions à la fois dépasseraient le budget raisonnable de flash. Le fichier `languages.tar.gz` de la release contient les APK générés avec les mêmes feeds que le firmware. Ils sont séparés par langue et possèdent leurs empreintes dans `SHA256SUMS`.

Installer uniquement la langue souhaitée et les traductions des applications concernées. Vérifier l'espace libre (`df -h /overlay`) et les empreintes avant l'installation. Les paquets sont signés par une clé de construction locale non publiée ; le firmware peut nécessiter l'ajout explicite de leur clé publique vérifiée, ou une installation locale `apk add --allow-untrusted` après vérification de leurs empreintes. Ne jamais utiliser cette option sur des fichiers de provenance inconnue.

Exemple après extraction d'un paquet de langue vérifié dans `/tmp` :

```sh
apk --no-network add --allow-untrusted /tmp/language/*.apk
```

Choisir ensuite la langue dans **Système → Système → Langue et apparence**. Les paquets optionnels de langues doivent rester adaptés à la version des applications installées. Ne pas utiliser un paquet d'une future snapshot pour écraser au hasard une ancienne base LuCI.

Codes disponibles pour cette version : `ar bg bn ca cs da de el es fa fi fil fr ga he hi hu it ja ka ko lo lt lv mr ms no nl pl pt pt-br ro ru sk sv ta tr uk vi yua zh-cn zh-tw`.
