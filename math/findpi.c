#include <stdio.h>
#include <math.h>
#define SIZE 30000
#define PRINT_GRID 0

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
}

int main() {

	// first, prepare a canvas
    #if PRINT_GRID
	int grid[SIZE][SIZE];
    #endif
	int i, j;
	unsigned long long int max=(SIZE*SIZE)/4;
 	unsigned long long int fraction=0;
	unsigned long long int c_squared = (SIZE+1)*(SIZE+1);

    printf("passed init\n");
	// then draw a circle
	for(i=0;i<SIZE;i++) for (j=0;j<SIZE;j++) {
        #if PRINT_GRID
	    grid[i][j] = 0;
        #endif
		int a = i+1, b = j+1;

		if(c_squared > a*a + b*b) {
            #if PRINT_GRID
			grid[i][j] = 1;
            #endif
			fraction +=1;
		}
	}

    #if PRINT_GRID
	print_grid(grid);
    #endif

	printf("pi estimate: ");
	int remainder = fraction;
	for (int k=0;k<30;k++) {
		printf("%llu", remainder/max);
		remainder = remainder%max;
		remainder *= 10;
	}
	printf("\n");

	printf("\n\nEnd of Program\n");
}
