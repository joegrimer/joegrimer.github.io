// remember to compile with -lcurses !

#include <stdio.h>
#include <ncurses.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

//~ #define SIZE 80
#define SLEEP_INTERVAL 150000
#define MAX_CHAINS 10

int semi_rand(int mod);
int maxx = 10;
int maxy = 10;

//~ void reload_neurons(int *neurons_ptr) {
   //~ int newx, newy;
   //~ for(int x=0;x<maxx;x++) {
      //~ for(int y=0;y<maxy;y++) {
         //~ newx = x+semi_rand(2)-1;
         //~ newy = y+semi_rand(2)-1;
         //~ if(newx<1) newx-=1;
         //~ if(newy<1) newy-=1;
         //~ if(newx > maxx) newx -= 2;
         //~ if(newy > maxy) newy -= 2;
         //~ if(newx < 0) newx += 2;
         //~ if(newy < 0) newy += 2;
         //~ *neurons_ptr[x][y][0] = newx;
         //~ *neurons_ptr[x][y][1] = newy;
      //~ }
   //~ }
//~ }

int main () {
   printf("start\n");

   int c = 0,
      d = 0;
   // Init ncurses mode
   initscr ();
   // Hide cursor
   curs_set (0);

   getmaxyx(stdscr, maxy, maxx);
   //~ printf("max_x is %d and maxy is %d\n", maxx, maxy);
   //~ exit(0);

   int neurons[maxx][maxy][2]; // 5 for x, 5 for y, 2 for link x, y

   //~ reload_neurons(&neurons);
   int newx, newy;
   for(int x=0;x<maxx;x++) {
      for(int y=0;y<maxy;y++) {
         newx = x+semi_rand(2)-1;
         newy = y+semi_rand(2)-1;
         if(newx<1) newx-=1;
         if(newy<1) newy-=1;
         if(newx > maxx) newx -= 2;
         if(newy > maxy) newy -= 2;
         if(newx < 0) newx += 2;
         if(newy < 0) newy += 2;
         neurons[x][y][0] = newx;
         neurons[x][y][1] = newy;
         //~ printf("%d,%d\t", newx, newy);
      }
      //~ printf("\n");
   }

   // prepare coords
   int coords[2] = {semi_rand(maxx),semi_rand(maxy)};
   int new_coords[2]; // = {coords[0], coords[1]};
   char star_symbol = '*';
   char forwardslash_symbol = '/';
   char *symbol_grid = "\\|/-*-/|\\";
   char *symbol = &symbol_grid[4];

   // colours
   start_color();
   short current_color = 7; // white
   init_pair(0,0,0); // black
   init_pair(1,1,0); // red
   init_pair(2,2,0); // green
   init_pair(3,3,0); // yellow
   init_pair(4,4,0); // blue
   init_pair(5,5,0); // purple
   init_pair(6,6,0); // cyan
   init_pair(7,7,0); // white
   attron(COLOR_PAIR(current_color));

   int colour_sequence[] = {7,6,5,1,4,0};
   //~ int firework_pos = 0;

   int number_of_chains = 0;
   int firework_chains[MAX_CHAINS][3];
   while(1) {
      if(semi_rand(3)==0 && number_of_chains < MAX_CHAINS) { // create a new chain
         firework_chains[number_of_chains][0] = semi_rand(maxy);
         firework_chains[number_of_chains][1] = semi_rand(maxy);
         firework_chains[number_of_chains][2] = 0; // index of chain
         number_of_chains++;
      }
      for(int n=0;n<number_of_chains;n++) {
         //~ int firework_pos = &firework_chains[n][2];
         //~ coords[0] = &firework_chains[n][0];
         //~ coords[1] = &firework_chains[n][1];
         if (firework_chains[n][2]>=7) {
            firework_chains[n][2] = 0;
            firework_chains[n][0] = semi_rand(maxx);
            firework_chains[n][1] = semi_rand(maxy);
         }
         attron(COLOR_PAIR(colour_sequence[firework_chains[n][2]])); // white
         mvprintw (firework_chains[n][1],firework_chains[n][0],"%c",*symbol);
         for(int m=0;m<2;m++) new_coords[m] = firework_chains[n][m];
         for(int l=0;l<7;l++)
            if (firework_chains[n][2] >= l) {
               int diffx = neurons[new_coords[0]][new_coords[1]][0] - new_coords[0];
               int diffy = neurons[new_coords[0]][new_coords[1]][1] - new_coords[1];
               symbol = &symbol_grid[(diffy+1)*3+(diffx+1)];

               new_coords[0] = neurons[new_coords[0]][new_coords[1]][0];
               new_coords[1] = neurons[new_coords[0]][new_coords[1]][1];
               mvprintw (new_coords[1],new_coords[0],"%c",*symbol);
            }

         firework_chains[n][2]++;
      }
      refresh();
      usleep(SLEEP_INTERVAL);
   }

   attroff(COLOR_PAIR(current_color));
   sleep(10);
   // End ncurses mode
   endwin();
}

short rand_clock = 0;
int semi_rand(int mod) {
   unsigned int res = rand()+time(NULL)+(97*rand_clock++)%mod;
   return res;
}
