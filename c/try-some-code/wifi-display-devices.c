/*
sudo apt-get update
sudo apt-get install nmap
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    // Run the nmap command to discover devices on the local network
    system("nmap -sn 192.168.1.0/24");

    return 0;
}

