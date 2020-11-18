#include <stdio.h>
#include <stdlib.h>

/*
 *A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

 1/2    =   0.5
 1/3    =   0.(3)
 1/4    =   0.25
 1/5    =   0.2
 1/6    =   0.1(6)
 1/7    =   0.(142857)
 1/8    =   0.125
 1/9    =   0.(1)
 1/10   =   0.1
 Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

 Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
 */
#define MAX_DENOMINATOR 1000
#define MAX_DECIMAL 2000
#define MIN_CYCLE 1
#define MAX_CYCLE 1000

int find_cycle(int * numbuf) {
    for (int lshift=0;lshift<MAX_DECIMAL;lshift++) {
        for (int cycle_length=MIN_CYCLE; cycle_length<MAX_CYCLE; cycle_length+=1) {
            int matched_len = 1;
            for (int i=0;lshift+i+cycle_length<MAX_DECIMAL;i++) {
                int pos_a = numbuf[lshift+i];
                int pos_b = numbuf[lshift+i+cycle_length];
                // printf("\nposa %d posb %d\n", pos_a, pos_b);
           
                if(pos_a!=pos_b) matched_len = 0;
            }
            if(matched_len) return cycle_length;
        }
    }
    return -1;
}


//#long int maxifier = 999999999999999999;

int main() {
    int best_cycle = 0;
    int best_example = 0;
    printf("start\n");
    for (long int denom=2;denom<=MAX_DENOMINATOR;denom++){
        printf("\n1/%ld = ",denom);
        printf("0.");
        long int numer = 1;
        int numbuf[MAX_DECIMAL]; for(int i=0;i<MAX_DECIMAL;i++) numbuf[i] = 0;
        int j; // to keep track of ceiling
        for(j=0;j<MAX_DECIMAL;j++) {
            numer*=10;
            long int quotient = (numer/denom);
            long int remainder = numer%denom;
            if(quotient > 9) printf("quotient > 9!! TSNH");
            numbuf[j] = quotient;
            if (remainder == 0) break;
            numer = remainder;
        }
        for(int i=0;i<MAX_DECIMAL && i<=j;i++) printf("%d", numbuf[i]);
        int fc2 = find_cycle(numbuf);
        if(j==MAX_DECIMAL) printf(" | %d", fc2);
        if (fc2==-1) exit(1);
        if (fc2>best_cycle) {
            best_cycle = fc2;
            best_example = denom;
        }
    }
    printf("\nbest cycle: %d from %d\n", best_cycle, best_example);
    printf("\n\nend\n");
}



