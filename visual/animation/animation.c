#include <stdio.h>
#include <ncurses.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define DOWNSHIP_HEIGHT 4
#define DOWNSHIP_WIDTH 5
struct sprite {
	int x;
	int y;
	char pic[3][4];
};

struct sprite droplet;

int coinflip() {
	return rand() % 2;
}
int third() {
	return rand()%3==1;
}
int fifth() {
	return rand()%5==1;
}
int fractional() {
	return rand()%97==0;
}

short rand_clock = 0;
int semi_rand(int mod) {
//	rand_clock++;
	unsigned int res = labs(rand()+time(NULL)+(97*rand_clock++))%mod;
	return res;
}
/*
int clock_rand(int mod) {
//	rand_clock++;
	unsigned int res = abs(rand()+time(NULL)+(97*rand_clock++))%mod;
	return res;
}*/

int main (void) {
	/* compile with gcc -lncurses file.c */
	int d = 0;
	/* Init ncurses mode */
	initscr ();
	/* Hide cursor */
	curs_set (0);

	int maxx = 0;
	int maxy = 0;
	getmaxyx(stdscr, maxy, maxx);
	//maxy = 30;
	// int halfx = maxx/2;
	int quartx = maxx/4;

	/* prepare downship */
	int downship[] = {
		-3, // y
		(quartx+(semi_rand(quartx*2))), // x
		4, // size
		};

	// prepare the colours
	start_color();
	init_pair(4,4,0); // blue
	init_pair(5,7,0); // purple - white

	// ground
	//for (int k=0;k<maxx;k++) mvprintw (maxy, k,"_");

	while (true) {
		erase();
		attron(COLOR_PAIR(5)); // purple

		// downship
		//mvprintw (downship[0]  ,downship[1], downship_wipe[0]);
		//mvprintw (downship[0]+1,downship[1], downship_wipe[1]);
		//mvprintw (downship[0]+2,downship[1], downship_wipe[2]);
		//mvprintw (downship[0]+3,downship[1], downship_wipe[3]);

		// move
		if((downship[0]+3)<maxy) {
			downship[0]+=semi_rand(2)+1;
			downship[1]+=semi_rand(3)-1;

			if(fifth()) downship[2]+=semi_rand(3)-1;

			if(fifth()) mvprintw(downship[0]+5,downship[1]-1,"o");
			if(fifth()) mvprintw(downship[0]+5,downship[1]+5,"o");
		}

		mvprintw (downship[0],downship[1], "F");
		mvprintw (downship[0]+downship[2],downship[1]+downship[2], "J");

		attroff(COLOR_PAIR(5)); // end purple
		refresh();
		sleep(1); // 1 second
		//usleep(250000); // 0.25 seconds
	}
	/* blow up
	d=c;
	while(c<maxy) {
		mvprintw (c-1, halfx, "      ");
		mvprintw (c,   halfx, "  /");
		mvprintw (c+3+(c-d),   halfx, "\\ ");
		mvprintw (c+1, halfx, " /");
		mvprintw (c+2+4+(c-d), halfx, "\\");
		mvprintw (c+2, halfx, " |[");
		mvprintw (c+2+3+(c-d), halfx, "]| ");
		mvprintw (c+3, halfx," \\_");
		mvprintw (c+3+3+(c-d), halfx,"_/ ");
		refresh();
		sleep(1);
		c++;
	}*/
	sleep(10);
	/* End ncurses mode */
	endwin();
	return 0;
}

