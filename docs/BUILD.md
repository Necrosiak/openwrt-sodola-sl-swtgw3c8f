# Reconstruction et provenance

Les références exactes sont dans `sources-lock.json`. Les branches amont sont utilisées seulement lors d'une construction `--rolling` explicitement demandée ou planifiée.

## Dépendances Linux

Exemple Debian/Ubuntu :

```sh
sudo apt-get install build-essential clang flex bison g++ gawk gcc-multilib gettext git libncurses-dev libssl-dev python3-setuptools rsync swig unzip zlib1g-dev file wget curl zstd libelf-dev
```

Construire avec un utilisateur normal, dans un chemin sans espace, avec plusieurs dizaines de Go libres :

```sh
JOBS=4 scripts/build.sh "$PWD/build"
python3 scripts/audit.py --tree . --build build
python3 scripts/collect.py build artifacts
```

Les packages de langues sont configurés en modules (`m`), hormis le français dans l'image (`y`). Ils sont produits dans `bin/packages/mips_24kc/` sans être tous inclus dans la flash.

La construction initiale a réutilisé une chaîne d'outils OpenWrt locale. Les recettes publiques téléchargent les sources et reconstruisent la chaîne. Les commits sont épinglés, mais une reconstruction n'est pas annoncée octet-identique : horodatages, chemin de construction et clés de signature peuvent changer les hashes. Seules les empreintes de la release identifient ses fichiers.

## Sources correspondantes

La release initiale inclut un bundle de sources : arbres OpenWrt et feeds aux commits exacts, sources Argon, modifications locales, configuration et archives amont téléchargées dans `dl/`. Les fichiers `.git`, caches d'accès, clés de signature privées, données appareil et journaux privés n'en font pas partie.

Pour réutiliser les archives de téléchargement, placer leur contenu dans `build/dl/` après la préparation de l'arbre. Les sources des binaires/firmwares tiers restent soumises aux licences de leurs fournisseurs ; une archive de firmware redistribuable n'est pas nécessairement un code source ouvert.

## Contrôles

- CRC de l'en-tête Realtek uImage et du payload ; décompression LZMA et limites de chargement.
- Image sysupgrade sous la limite de 12 Mio de la partition firmware, identité de carte vérifiable via métadonnées.
- Inspection du SquashFS extrait pour mots de passe, clés privées et données d'instance.
- Contrôle de la configuration de premier démarrage et des services désactivés.
- Validation du thème et de ses fonctions déjà réalisée sur le système en service ; image publique complète non encore testée au démarrage.

Les traces des anciens diagnostics restent locales : elles contiennent des informations de l'installation et ne sont pas nécessaires à la reconstruction. Les patches de diagnostic nécessaires au socle sont publiés dans leur forme source, sans dump mémoire ou configuration d'appareil.
