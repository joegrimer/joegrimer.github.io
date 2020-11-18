/* This is a rewrite of my Python solution to Euler project problem 3 in C */

#include <stdio.h> // all C programs need this methinks
//#include <stdlib.h> // not totally sure I need this...

void main()
{
	printf ("Euler Project #3\n");
	
	int bigNum = 13195;
//	int bigNum = 600851475143; // this line will break it... c is rather delicate
	int factors[bigNum]; // this is how you declare an array in C.
	// must declare how big it is... I think it's always smaller than bigNum,
	// but an alternative solution would be complex
	int bigFac;

	int posFac; // old-school - loop var must be declared
	for(posFac=2;posFac<bigNum;posFac++) {
	// it's i=2 because I want to skip the number one
		if((bigNum%posFac==0) && isPrime(posFac))
			bigFac=posFac;
	}
  printf("Largest Prime Factor:%d\n",bigFac);
//	exit(0);
}

int isPrime(int posPri) {
// it is called int because that's what it returns... really it's a bool, but this is C!

//	printf("checking %d for primeness\n",posPri);

	int posFac; // old-school - loop var must be declared
	for(posFac=2;posFac<posPri;posFac++) {
	// it's i=1 because I want to skip the number one
		if(posPri%posFac==0) {
//			printf("%d is not prime because it is made of %d and %d\n",posPri,posFac,posPri/posFac);
			return(0);
		}
	}
	// else
	return(1);
}

// there we go... my first (real) C program. One day again, perhaps...
// it ran in half the time of the original Python script, so that's some consolation
