
#include <stdio.h>
//#include <stdlib.h>

/* Euler 1 - Joseph Grimer Nov 2017
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
 */

void main() {
    printf("Euler 4 - The Pallindrome - Joseph Grimer Nov 2017\n\n\n");

    checkPallindrome(1111);
    // initiate vars
//    int max = 11; // largest 2 digit number
//    int total = 0; // ?
//
//    int i = 10; // smallest 2-digit number
//    for(i;i<max;i=i+1) {
//        if(checkPallindrome(i)) {
//            printf("I found one! : %i", i);
//            break;
//        }
//    }
//    printf("total: %i",total);

    printf("\n\nend of program\n\n");
//    return 0;
}

// bool function - not really an int!
int checkPallindrome(int posPall) {
    char* strnum[5]; // empty char ready to fill
    itoa(posPall, strnum, 10); // convert i to string [buf]

    short leftPointer = 0;
    short rightPointer = strlen(strnum)-1;

    printf("number is >%i< string version is >%s< leftPointer is>%i< rightPointeris >%i<\n",posPall,strnum,leftPointer,rightPointer);
    // print our string
    while (leftPointer<rightPointer) {
        printf("looping...\n");
        printf("number is >%i< string version is >%s< leftPointer is>%i< rightPointeris >%i<\n",posPall,strnum,leftPointer,rightPointer);

//        char oneletter = "g";
        int matches = (strnum[leftPointer] == strnum[rightPointer]);
        printf("matches is >%i<\n", matches);
        leftPointer = leftPointer + 1;
        rightPointer = rightPointer - 1;
    }
    return 0;
}

