#include <stdio.h>
#include <stdlib.h>

int main() {

    FILE *f;
    char c;
    f=fopen("info.txt","rt");

    while((c=fgetc(f))!=EOF){
        printf("%c\n",c);
    }

    fclose(f);
    return 0;
}