/*

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

(21)22 23 24(25)
 20 (7) 8 (9)10
 19  6 (1) 2 11
 18 (5) 4 (3)12
(17)16 15 14(13)

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

*/

#include <stdio.h>
#include <stdlib.h>
#define MIN_CYCLE 1
#define MAX_CYCLE 1000

int number_in_position(int position) {
    int res = 1;
    for(int i=0;i<=position;i++) {
        int mini_ring = (i+3)/4;
        res += mini_ring*2;
    }
    return res;
}

int sum_in_position(int position) {
    int res = 1;
    int sum = 0;
    for(int i=0;i<=position;i++) {
        int mini_ring = (i+3)/4;
        res += mini_ring*2;
        sum += res;
    }
    return sum;
}

int main() {
    printf("Start of Program.\n\n"); 

    int width = 1001;
    int aim = ((width-1)/2)*4;
    printf("width: %d; aim: %d\n", width, aim);
    //for(int i=0;i<=aim;i++)
    //    printf("%d = %d\n", i, number_in_position(i));
    printf("sum: %d", sum_in_position(aim));

    printf("\nEnd of Program.\n"); 
}



