#include <stdio.h>

/* this is a program written mainly so that I can get the hang of the c language - as I'm not very good yet
 * I've written better stuff in the past in python and js... but yeah
 *
 * Joseph Grimer June 2018 */

#define SIZE 5

main() {

  // initiate board
  static int board[SIZE][SIZE],i,j;


  // print board
  for(i = 0; i < SIZE; i++) {
    for(j=0;j<SIZE; j++) {

      switch (board[i][j]) {
        case 0:
          printf(".");
          break;
        case 1:
          printf("x");
          break;
        case 2:
          printf("o");
          break;
      }
    }
    printf("\n");
  }

}
