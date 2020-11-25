#include <stdio.h>

/* a simple program used to establish maximums */
main() {
	unsigned char i = 1; // or long int, or short, int
	while(i>0) {
		++i;
		printf("%d, ",i);
	}
}
