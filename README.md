# RTS-V6.5 corrigée

RTS MÉDIÉVAL v6.2 — fichiers à placer à la racine du dépôt GitHub

  main.py  game.py  net.py  campaign.py  assets_data.py  sounds_data.py
  make_icons.py  presplash.png  icon.png  buildozer.spec

Compilation : .github/workflows/build.yml (inclus ; sinon le créer sur GitHub avec le contenu de build.yml.txt).
L'APK est dans Actions > dernier run > Artifacts > rtsmedieval-apk.
(presplash.png et icon.png sont aussi recréés automatiquement pendant la compilation s'ils manquent.)

Nouveautés v6.1 : personnages et Horde de l'intro corrigés (miroir), mise en page de l'interface sans chevauchement,
écran de démarrage Android, menu de la partie (reprendre / sauvegarder / charger / quitter),
sauvegarde et chargement dans chaque mode (escarmouche, campagne y compris tutoriels, multijoueur côté hôte).

v6.2 : boutons et noms de l'interface de jeu refaits : textes qui s'adaptent à la place disponible,
cartes d'action plus grandes (icône, nom sur 2 lignes, coût), boutons d'outils dimensionnés d'après l'écran,
aucun chevauchement entre ressources, objectifs, messages, minicarte, outils et barre du 
bas.
