/*
* 
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
*/

#include <stdio.h>

//#define MAX 3628800
#define MAX 32767
#define GOAL 1000 // number of places looking for... finally 1000

int main() {

  printf("Commencing Program.\n");

  int i,j,k, // for loops
    fb[2][1000], // definelty want to keep top wto no's
    unit_ptr = 0, // tens, tens to start with
    ceiling = 0,
    alternator = 1; // where to put sum
  
  // empty the slots
  for(i=0;i<1000;i++) fb[0][i] = fb[1][i] = 0;

  // starter
  fb[0][0] = 1;

  for(i=1;i<MAX;i++) {
    alternator = !alternator;
    for(unit_ptr=0;unit_ptr<=ceiling;unit_ptr++) {
      fb[alternator][unit_ptr] = fb[!alternator][unit_ptr] + fb[alternator][unit_ptr]; // max 9999
      if (fb[alternator][unit_ptr] > 9) {
        fb[alternator][unit_ptr] -= 10;
        fb[alternator][unit_ptr+1] += 1; // carry me :)
        if(unit_ptr+1 > ceiling) ceiling += 1;
      }
    }
    //if (fb[alternator][unit_ptr] > 9999)
    
    if (ceiling+1 == GOAL) {
    printf("%d. ",i);
      // printer
      for(j=ceiling;j>=0;j--) {
//        printf("%d",fb[alternator][j]);
      }
      break;
    }
  }

//  printf("\nFinal ceiling is %d\n",ceiling+1);
  printf("Program Terminating.\n");
  
  return 0;
}
