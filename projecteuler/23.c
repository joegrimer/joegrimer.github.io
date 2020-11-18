/*
* A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
* For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
* 
* A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
* 
* As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
* By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
* However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
* 
* Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
*/

#include <stdio.h>

#define MAX 28123

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

int main() {
	int i,j,total = 0;
	int abundant_numbers[9999];
	int abundant_numbers_i = 0;
	int not_be_written[MAX+1];
	
	for(i=0;i<1000;i++) abundant_numbers[i]=0;
	for(i=0;i<=MAX;i++) not_be_written[i]=i;
	
	for(i=1;i<=MAX;i++) {
		//~ if(i<30||i>28115) printf("%d? %d, \n",i,is_abundant(i));
		if(is_abundant(i)) {
			abundant_numbers[abundant_numbers_i++] = i;
			for(j=0;j<abundant_numbers_i;j++) if(i+abundant_numbers[j]<=MAX) {
				//~ printf("| %d+%d=%d |",i,abundant_numbers[j],i+abundant_numbers[j]);
				not_be_written[i+abundant_numbers[j]] = 0;
			}
		}
	}
	printf("stopped at %d\n",i);
	
	for(i=0;i<=MAX;i++) {
		total+=not_be_written[i];
		//~ if(i>20000 && not_be_written[i]!=0) printf("%d=%d,",i,not_be_written[i]);
	}
	printf("\n\nabundat i = %d",abundant_numbers_i);
	printf("\n\n%i\n",total);
	return 0;
}

