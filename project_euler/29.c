#include <stdio.h>
#include <math.h>
#include <gmp.h>
#include <stdlib.h>

#define MAX 5
// need to try for 100
#define MAX_SQUARED MAX*MAX

int count = 0;
int i;
/*
int check_and_add(int new_int) {
	int i=-1;
	for(i=0;i<MAX*MAX;i++) {
		if(seq[i]==0) break; // reached end of sequence
		else if (seq[i] == new_int) return 1;
	}
	seq[i] = new_int;
	count += 1;
	return 1;
}
*/

int main() {

	printf("start\n");
    printf("max is %d\n",MAX);
    printf("max*max is %d\n",MAX_SQUARED);

    mpz_t new_num;
	mpz_t a_big;
	mpz_t b_big;
    //mpz_t *seq; //[MAX_SQUARED];
    //seq = (mpz_t *) malloc(MAX_SQUARED * sizeof(mpz_t));
    //for(i=0;i<MAX_SQUARED;i++) {
    //    mpz_set_ui(seq[i],0);
    //}

    int a=2,b=2;
    //for (unsigned long int a=2;a<=MAX;a++) for(unsigned long int b=2;b<=MAX;b++) {
	    mpz_set_ui(a_big, 100);
	    mpz_set_ui(b_big, 100);
        mpz_pow_ui(new_num, a_big, b);
	    printf("\n= ");
        mpz_out_str(stdout, 10, new_num);
	    //check_and_add(new_num);*/
    //}
    printf("\ncount: %d\n", count);
	printf("\nend\n");

    //free(seq);
    mpz_clear(new_num);
    mpz_clear(a_big);
    mpz_clear(b_big);
}
