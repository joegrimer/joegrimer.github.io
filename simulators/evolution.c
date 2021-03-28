#include <stdio.h>
#include <stdlib.h>

#define NUMBER_OF_CREATURES 1000
#define CREATURE_MAX 9999999
#define NUMBER_OF_ROUNDS 5
int creatures[NUMBER_OF_CREATURES];

int main() {
    for(int i=0;i<NUMBER_OF_CREATURES;i++) {
        creatures[i] = ((rand())%CREATURE_MAX)+1;
    }
    
    int total = NUMBER_OF_CREATURES;
    for(int r=0;r<NUMBER_OF_ROUNDS;r++) {
        printf("Round %d\n\n", r);
        for(int i=0;i<NUMBER_OF_CREATURES;i++) {
            int rand_num = (rand() % 100)+1;
    //        printf("about to check %d against %d\n", creatures[i], rand_num);
            if(creatures[i] % rand_num != 0) { // i.e. is not a factor
      //          printf("creature %d dies.\n", i);
                creatures[i] = 0;
                total--;
            }
        }
        printf("living/total = %d/%d\n\n", total, NUMBER_OF_CREATURES);
        for(int i=0;i<NUMBER_OF_CREATURES;i++) {
            if(creatures[i]) printf("%d, ", creatures[i]);
        }
        printf("\n\n");
    }
    return 0;
}
