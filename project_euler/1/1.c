// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

#include <stdio.h> // all C programs need this methinks
//#include <stdlib.h> // not totally sure I need this...

// declarations of functions
void p();

void main() {
	p("Euler Project #1");

	int bigNum = 10;
	int i;
	int factorAry[5];
	for(i=3;i<bigNum;i++) {
		if(i%3==0) {
			factorAry[1]=i;
		}
	}
	p(factorAry);
}

void p(char string[32]) {

	printf(">%s<",string);
	printf("\n");
}
