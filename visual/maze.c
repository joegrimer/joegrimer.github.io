#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

#define WIDTH 60
#define HEIGHT 30

int grid[WIDTH][HEIGHT] = {};
void print_maze();
int finishable(int x, int y);

int main() {
   printf("Welcome to maze. Your goal: get from top left to bottom right\n\n");
   srand(time(NULL));   // Initialization, should only be called once.
   int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.

   int i, j;

   for(i=0;i<WIDTH;i++)
       for(j=0;j<WIDTH;j++) grid[i][j] = (rand() % 7 == 1);

   print_maze();

   printf("Finishable? %d\n", finishable(0, 0));
   printf("Fin\n");
}

int finishable(int x, int y) {
   if (grid[x][y] == '#') return 0;
   else if (x == WIDTH) return 1;
   else return finishable(x+1, y);
}

void print_maze() {
   printf("Start\n");
   printf("V");
    for(int i=0;i<WIDTH-1;i++) printf("_");
    printf("\n");
    for(int i=0;i<HEIGHT;i++) {
        for(int j=0;j<WIDTH;j++) {
            if (grid[i][j]) printf("#");
            else printf(" ");
        }
        printf("\n");
    }
    for(int i=0;i<WIDTH-1;i++) printf("-");
   printf("^\n");
    for(int i=0;i<WIDTH-3;i++) printf(" ");
   printf("end\n\n");
}
