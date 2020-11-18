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
#define MAX 9

int main() {

  printf("Commencing Program.\n");

  int i,j,k,
    fibonacci_buffer[2][1000],
    fb_lengths[2] = {0,0},
    alternator = 0,
    sum_of_column;
  
  // empty the slots
  for(i=0;i<1000;i++) fibonacci_buffer[0][i] = fibonacci_buffer[1][i] = 0;

  // starter
  fibonacci_buffer[0][0] = 1;
  fb_lengths[0] = 1;
  
  for(i=0;i<MAX;i++) {
    
    int max_len = fb_lengths[0];
    if(fb_lengths[1] > fb_lengths[0]) max_len = fb_lengths[1];
    
    // manual summing
    for(j=0;j<max_len;j++) {
      fibonacci_buffer[alternator][j] = fibonacci_buffer[alternator][j] + fibonacci_buffer[!alternator][j];
      if (fibonacci_buffer[alternator][j] > 10) {
        fibonacci_buffer[alternator][j+1]+=fibonacci_buffer[alternator][j]/10; // add to tens
        fibonacci_buffer[alternator][j]%=10; // remove from ones
        if(j==max_len-1) { // i.e. nearly out
          fb_lengths[alternator]++;
          max_len++; // go on one more
        }
      }
    }
    
    printf("%d. ",i);
    for(j=fb_lengths[alternator]-1;j>=0;j--) printf("%d-",fibonacci_buffer[alternator][j]);
    printf("(%d,%d)\n",fb_lengths[0],fb_lengths[1]);
    alternator = !alternator; // switch track
}

  printf("Program Terminating.\n");
  
  return 0;
}
