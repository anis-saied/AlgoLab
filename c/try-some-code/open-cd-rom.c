/*

*/

#include <stdlib.h>
#include <unistd.h>  // Include for sleep function
int main() {
    // Open CD/DVD drive tray
    system("eject");

    // Wait for a few seconds (optional)
    sleep(3);

    // Close CD/DVD drive tray
    system("eject -t");

    return 0;
}

