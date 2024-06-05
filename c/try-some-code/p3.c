argc: est une abréviation de "argument count" (nombre d'arguments). 
      Le premier argument (indice 0) est le nom du programme lui-même. 
argv : "argument vector" (vecteur d'arguments).
example : 
./example arg1 arg2 arg3
argc sera égal à 4, car il y a 4 arguments passés au programme (y compris le nom du programme lui-même).
Le tableau argv sera ["./example", "arg1", "arg2", "arg3"]. L'indice 0 de argv contient le nom du programme lui-même
-----------------------------------------------------------------------------------------------------------------
La fonction strdup : abréviation de "string duplicate"
alloue dynamiquement de la mémoire pour une copie d'une chaîne de caractères spécifiée 
et copie cette chaîne dans la mémoire nouvellement allouée.
et retourne un pointeur vers la nouvelle chaîne de caractères dupliquée. 
et Si la mémoire ne peut pas être allouée, elle retourne NULL.
example :
const char *original = "Hello, world!";
char *duplicate = strdup(original);
free(duplicate); // N'oubliez pas de libérer la mémoire allouée
-----------------------------------------------------------------------------------------------------------------
execvp()
une fonction de la famille des fonctions exec qui exécute un fichier exécutable 
abréviation de "execute with a given PATH"
Elle est utilisée pour exécuter un fichier exécutable en utilisant une liste d'arguments fournie, en recherchant le fichier exécutable dans les répertoires répertoriés dans la variable d'environnement PATH.

La lettre "v" dans execvp() signifie "vector", car elle prend un vecteur (tableau) d'arguments. La lettre "p" signifie "path", indiquant que execvp() recherche le chemin d'accès au fichier exécutable dans les répertoires spécifiés par PATH.

La fonction execvp() (et ses variantes) utilise un tableau d'arguments où le dernier élément doit être NULL pour indiquer la fin du tableau. Cela permet à la fonction de savoir où s'arrêtent les arguments.
