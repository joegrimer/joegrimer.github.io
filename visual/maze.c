#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

#define WIDTH 60
#define HEIGHT 30
#define DENSITY_N 141
#define DENSITY_D 300
#define TRIES 2000

int grid[WIDTH][HEIGHT] = {};
int checked_grid[WIDTH][HEIGHT] = {};
void print_maze();
int finishable(int x, int y);
void init_checked_grid();
void init_maze();

int main() {
   printf("Welcome to maze. Your goal: get from top left to bottom right\n\n");
   srand(time(NULL));   // Initialization, should only be called once.
   int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.

   int i;
   for(i=0;i<TRIES;i++) {
     printf(".");
     init_maze();
     init_checked_grid();

     if (finishable(0, 0) == 1) {

       break;
     };
   }
   print_maze();

   printf("Fin\n");
}

void init_maze() {
   int i, j;
   for(i=0;i<HEIGHT;i++)
       for(j=0;j<WIDTH;j++) grid[i][j] = (rand() % DENSITY_D <= DENSITY_N);
}

void init_checked_grid() {
   int i, j;
   for(i=0;i<WIDTH;i++)
       for(j=0;j<WIDTH;j++) checked_grid[i][j] = 0;
}

int finishable(int x, int y) {
   if (y<0 || y>=HEIGHT || x<0 || x>=WIDTH) return 0;
   if (checked_grid[y][x] == 1) return 0;
   checked_grid[y][x] = 1;
   if (grid[y][x] == 1) return 0;
//   if (x > WIDTH-3 || y > HEIGHT-3)
//     printf("Finishable %d %d is %d\n", x, y, grid[x][y]);
   if (x == WIDTH-1 && y == HEIGHT-1) {
//      printf("Found bottom corner");
      return 1;
   }
   if (finishable(x+1, y)) return 1;
   if (finishable(x-1, y)) return 1;
   if (finishable(x, y+1)) return 1;
   if (finishable(x, y-1)) return 1;
   return 0;
}

void print_maze() {
   printf("\nStart\n");
   printf(" ");
    for(int i=0;i<WIDTH;i++) printf("#");
    printf("\n");
    for(int i=0;i<HEIGHT;i++) {
        for(int j=0;j<WIDTH;j++) {
            if (grid[i][j]) printf("#");
            else printf(" ");
        }
        printf("#\n");
    }
    for(int i=0;i<WIDTH-1;i++) printf("#");
   printf(" \n");
    for(int i=0;i<WIDTH-3;i++) printf(" ");
   printf("end\n\n");
}
