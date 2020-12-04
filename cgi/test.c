#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int 
main()
{
    int i = 0;
    while(1) {
        printf("%c\t", rand()%256);
        usleep(100);
    }
}
