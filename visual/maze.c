#include <stdio.h>

int main() {
    for(int i=0;i<100;i++) {
        for(int j=0;j<100;j++) {
            
            if (rand() %7) printf(" ");
            else printf("O");
        }
        printf("\n");
    }
}
