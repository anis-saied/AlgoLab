#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // useful for get process id
#include <string.h>
#include <sys/wait.h> // useful for wait()
#include <fcntl.h> 
/*
fcntl.h : pour la manipulation de fichiers et aux opérations d'E/S (entrée/sortie) basées sur des descripteurs de fichiers.

rediriger la sortie standard (stdout) vers un fichier spécifié. 
open() 
est utilisée pour ouvrir ou créer un fichier. 
Elle prend en général trois arguments : 
  le chemin vers le fichier, 
  le mode d'ouverture 
    "O" est utilisé pour indiquer qu'il s'agit d'un indicateur d'ouverture de fichier.
    O_CREATE : Crée le fichier s'il n'existe pas.
    O_WRONLY : Ouvre le fichier en mode écriture seulement.
    O_TRUNC : 
      si le fichier spécifié existe déjà, il sera vidé (tronqué) à zéro octet avant d'être ouvert. 
      Si le fichier n'existe pas, cette option n'a aucun effet.
  et les permissions.
    un masque de permission qui spécifie les permissions pour le propriétaire (user) du fichier. 
    Il définit les permissions de lecture (R), écriture (W) et exécution (X) pour l'utilisateur (U). 
    Dans ce cas, S_IRWXU donne à l'utilisateur la permission de lire, écrire et exécuter le fichier.
    
Dans ce cas, cela remplace le descripteur de fichier qui a été fermé précédemment pour la sortie standard.
*/
int main(int argc, char *argv[]){
  printf("hello (pid:%d)\n",(int)getpid());
  int rc = fork();
  if (rc < 0){ // fork failed; exit
    fprintf(stderr, "fork failed\n");
    exit(1);
  } else if (rc == 0){ // child (new process): redirect standard output to a file
    close(STDOUT_FILENO);
    open("./p4.output", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
    printf("hello i am child (pid: %d)\n", (int)getpid());
    // new execute wc 
    char *myargs[3];
    myargs[0] = strdup("wc"); // program: wc (word count)
    myargs[1] = strdup("p3.c"); // argument: the file to count
    myargs[2] = NULL; // marks end of array
    execvp(myargs[0], myargs); // runs word count
    printf("this shouldn't print out");
  } else { // parent goes down this path (main)
    int wc = wait(NULL); 
    printf("hello, i am parent of %d (wc: %d) (pid: %d)\n", rc, wc, (int)getpid());
  }
  return 0;
}
