#include <stdio.h>
#include <stdbool.h>

main() {
	int power = 20;
	unsigned long max = 1<<power;
	unsigned int numbers[max];
	unsigned long i, j;
	unsigned long product = 1;

	// init em

	for(i=0;i<max;i++) {
		numbers[i]=1;
	}

	// figure em

	for(i=2;i<max;i++) {
		if(numbers[i]==1 && j>i) {
			j=i;
			product = 2;
			while(product < max) {
				product = i*j;
				if(product < max) numbers[product] = 0; // otherwise mem leak
				j++;
			}
		}
	}

	long largest = 2;
	// print em
	printf("\n\nAnd here, sir, is the largest prime we could find:\n\n");
	for(i=1;i<max;i++) {
		if(numbers[i] == 1)	largest = i;//printf("%d,",i);
	}
	printf("%ld\n",largest);

	for(i=0;i<power;i++) {
		if (!!(largest&(i << 1))) printf("1");
		else printf("0");
	}
	printf("\n");
}
