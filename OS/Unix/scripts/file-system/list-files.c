#include <stdio.h>
#include <dirent.h>

int main(int argc, char *argv[]) {
    struct dirent *entry;
    DIR *dp;
    
    // If no directory is specified, use the current directory
    char *directory = argc > 1 ? argv[1] : ".";

    dp = opendir(directory);
    if (dp == NULL) {
        perror("opendir");
        return 1;
    }

    // Read and print the entries in the directory
    while ((entry = readdir(dp)) != NULL) {
        printf("%s\n", entry->d_name);
    }

    closedir(dp);
    return 0;
}
