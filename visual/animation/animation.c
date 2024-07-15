#include <stdio.h>
#include <ncurses.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>


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
	// int halfx = maxx/2;
	int quartx = maxx/4;

	/* prepare bubbles */
	int bubble[3][2] = {semi_rand(4)*4-10,quartx+(semi_rand(quartx*2)),
						semi_rand(4)*4-10,quartx+(semi_rand(quartx*2)),
						semi_rand(4)*4-10,quartx+(semi_rand(quartx*2))};

	/* prepare cleaners */
	int cleaner[3][2] = {
		{1, 1},
		{1, 1},
		{1, 1},
	};

	//printf("%d,%d",maxx,maxy);

	// prepare the colours
	start_color();
	init_pair(4,4,0); // blue
	init_pair(5,7,0); // purple - white

	//return true;
	while (true) {
		// erase();
		attron(COLOR_PAIR(4)); // blue
		// cleaners - these do some of the erasing
		for(d=0;d<3;d++) {
			mvprintw(cleaner[d][0]+0,cleaner[d][1],"        ");
			mvprintw(cleaner[d][0]+1,cleaner[d][1],"        ");
			mvprintw(cleaner[d][0]+2,cleaner[d][1],"        ");
			mvprintw(cleaner[d][0]+3,cleaner[d][1],"        ");
			mvprintw(cleaner[d][0]+4,cleaner[d][1],"        ");
			mvprintw(cleaner[d][0]+5,cleaner[d][1],"        ");

			cleaner[d][0]+=((bubble[d][0]-cleaner[d][0])/3);
			cleaner[d][1]+=((bubble[d][1]-cleaner[d][1])/3);

			mvprintw(cleaner[d][0]+0,cleaner[d][1],"        ");
			mvprintw(cleaner[d][0]+1,cleaner[d][1],"  8888  ");
			mvprintw(cleaner[d][0]+2,cleaner[d][1]," 8    8 ");
			mvprintw(cleaner[d][0]+3,cleaner[d][1]," 8    8 ");
			mvprintw(cleaner[d][0]+4,cleaner[d][1],"  8888  ");
			mvprintw(cleaner[d][0]+5,cleaner[d][1],"        ");
		}
		attroff(COLOR_PAIR(4)); // end blue
		attron(COLOR_PAIR(5)); // purple
		// ships
		for(d=0;d<3;d++) {
			/* Print at row 0, col 0 */
			mvprintw (bubble[d][0]  ,bubble[d][1]+1,"/\\");
			mvprintw (bubble[d][0]+1,bubble[d][1], "/  \\");
			mvprintw (bubble[d][0]+2,bubble[d][1], "|[]| ");
			mvprintw (bubble[d][0]+3,bubble[d][1],"\\__/ ");

			if(fifth()) mvprintw(bubble[d][0]+5,bubble[d][1]-1,"o");
			if(fifth()) mvprintw(bubble[d][0]+5,bubble[d][1]+5,"o");

			bubble[d][0]+=semi_rand(2)+1;
			bubble[d][1]+=semi_rand(3)-1;
			if(bubble[d][0]>maxy) {
				bubble[d][0]=-4;
				// bubble[d][1]=quartx+(semi_rand(quartx*2));
			}
		}
		attroff(COLOR_PAIR(5)); // end purple
		refresh();
		sleep(1);
		//usleep(750000); // 0.75 seconds
	}/* blow up
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

