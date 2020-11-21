#include <stdio.h>
#include <math.h>
#define SIZE 10000

/*
void print_grid(int grid[SIZE][SIZE]) {
	int i,j;
	printf("\n");
	for(i=0;i<SIZE;i++) {
		for (j=0;j<SIZE;j++) {
			if(grid[i][j]) printf("O");
			else printf(" ");
		}
		printf("\n");
	}
}*/

int main() {
  
	// first, prepare a canvas
	//int grid[SIZE][SIZE];
	int i, j;
	unsigned long long int max=SIZE*SIZE;
 	unsigned long long int fraction=0;
	unsigned long long int c_squared = (SIZE+1)*(SIZE+1);
	//for(i=0;i<SIZE;i++) for (j=0;j<SIZE;j++) grid[i][j] = 0;

	// then draw a circle
	for(i=0;i<SIZE;i++) for (j=0;j<SIZE;j++) {
		int a = i+1, b = j+1;
		//printf("-\nc^2 = a^2 + b^2\n");
		//printf("%d^2 = %d^2 + %d^2\n",SIZE,a,b);
		//printf("%d = %d + %d\n",SIZE*SIZE, a*a, b*b);
		if(c_squared > a*a + b*b) {
		//	grid[i][j] = 1;
			fraction +=1;
		}
	}

//	print_grid(grid);
//	printf("%d/%d = %d%%\n", fraction,max, (fraction*100)/max);
	
	// pi is now fraction*4/max
	//	unsigned long long int estimate = (unsigned long long int)fraction*40000000/(unsigned long long int)max;
	//printf("pi estimate: %llu\n", estimate);
	
	printf("pi estimate: ");
	int remainder = fraction*4;
	for(int k=0;k<30;k++) {
		printf("%d", remainder/max);
		remainder = remainder%max;
		remainder *= 10;
	}
	printf("\n");
	
	printf("\n\nEnd of Program\n");
}
