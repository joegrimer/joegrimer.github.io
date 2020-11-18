/*
* A permutation is an ordered arrangement of objects.
* For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
* 
* If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
* The lexicographic permutations of 0, 1 and 2 are:
* 012   021   102   120   201   210
* 
* What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
*/

#include <stdio.h>

//#define MAX 3628800
#define MAX 9999999

int main() {

  printf("Commencing Program.\n");

  int sequence_length = 10;
  int i,j,k,l;
  int original_sequence[sequence_length];
  int current_sequence[sequence_length];
  int pieces_left[sequence_length];
  for(i=0;i<sequence_length;i++) original_sequence[i] = current_sequence[i] = pieces_left[i] = i;
  int true_maxi[sequence_length], true_max = 1;
  for(i=1;i<=sequence_length;i++) {true_max*=i;true_maxi[i-1]=true_max;}
  printf("len is: %d and truemax is %d\n",sequence_length,true_max);

  //~ printf("truemaxi: [");
  //~ for(j=0;j<sequence_length;j++) printf("%d,",true_maxi[j]);
  //~ printf("]\n");
  
  for(i=0;i<MAX&&i<true_max;i++) {
    
    for(j=0;j<sequence_length;j++) pieces_left[j]=original_sequence[j];

    for(l=0;l<sequence_length;l++) {
      //~ printf("%d/%d/%d; ",i,true_maxi[sequence_length-1-l],sequence_length-l);
      int new_piece_position = (i/(true_maxi[sequence_length-1-l]/(sequence_length-l)))%(sequence_length-l);
      //~ printf("nppl: %d (f%d) / (%d / %d); ",i%(sequence_length-l), (sequence_length-l), true_maxi[sequence_length-1-l], (sequence_length-l));
      //~ printf("npp: %d; ",new_piece_position);
      current_sequence[l] = pieces_left[new_piece_position];

      for(k=new_piece_position+1;k<sequence_length-l;k++)
        pieces_left[k-1] = pieces_left[k];

      //~ printf("pieces left: [");
      //~ for(j=0;j<sequence_length-1-l;j++) printf("%d,",pieces_left[j]);
      //~ printf("]\n");
    }

    //~ printf("current sequence: %d\n",current_sequence[0]);
    if(i==999999) {
      printf("current sequence: ");
      for(j=0;j<sequence_length;j++) printf("%d",current_sequence[j]);
      printf("\n");
      return 0;
    }
    //~ break;
  }
  printf("Program Terminating.\n");
  
  return 0;
}

int is_abundant(int number) {
  int i,factor_total = 1,top_bar=number;

  for(i=2;i<top_bar;i++) {
    if(number%i==0) {
      factor_total+=i;
      if(number/i!=i) factor_total+=(number/i);
      top_bar=(number/i);
    }
    if(factor_total>number) {
      //~ printf("A factor total:%d,",factor_total);
      return 1;
    }
  }
  return 0;
}

