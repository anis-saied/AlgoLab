# Git resume

## commit

faire un commit avec un message sur plusieurs lignes:
1. utiliser plusieurs -m, Chaque -m correspond à un paragraphe du message.
example
git commit -m "Titre du commit" -m "Première ligne de description
Deuxième ligne de description"

2. écrire le message de commit dans un editeur de texte
git commit : Git ouvre alors ton éditeur de texte. Puis enregistrer et quitter l'éditeur.

## HEAD
Le pointeur HEAD est simplement le curseur « Vous êtes ici » de Git. Il indique à votre ordinateur quelle version exacte du projet est actuellement affichée dans votre dossier de travail et modifiée.

Normalement, lorsque vous travaillez, HEAD pointe vers une branche (par exemple, master), et c'est cette branche qui pointe vers le dernier commit. C'est un peu comme un train attaché à sa locomotive : quand la locomotive avance, le train avance.

### Detached HEAD


## Branche
Techniquement, une branche dans Git n'est pas une boîte qui contient des commits. C'est simplement un marque-page mobile (ou un Post-it) collé sur le tout dernier commit que vous avez écrit.

Analogie : Votre marque-page s'appelle master. Il est posé sur la dernière page écrite (disons, le Chapitre 2). Vu que le Chapitre 2 est attaché au Chapitre 1, toute l'histoire (Chapitre 1 + Chapitre 2) forme la « branche » master. Mais au fond, la branche n'est qu'un pointeur vers le sommet de la pile.

crée directement le dépôt en nommant la première branche main au lieu de master.
git init --initial-branch=main
