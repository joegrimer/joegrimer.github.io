// Hello there... this is a small program I wrote using ncurses as a graphics framework
// it's called growth... and should show you a rather nice animation of a something being drawn// enjoy!
// Joseph Grimer - September 2018

#include <stdio.h>
#include <ncurses.h>
#include <stdlib.h>

int semi_rand(int mod);

int main (void) {
	/* compile with gcc -lncurses file.c */
	int c = 0,
		d = 0;
	/* Init ncurses mode */
	initscr ();
	/* Hide cursor */
	curs_set (0);

	int maxx = 0;
	int maxy = 0;
	getmaxyx(stdscr, maxx,maxy);
	int halfx = maxx/2;
	int quartx = maxx/4;

	/* prepare thing */
	int thing[2] = {halfx,maxy/2};
	int symbol = 0;

	/*colours*/
	// 0 = black
	// 1 = red
	// 2 = green
	// 3 = yellow
	// 4 = blue
	// 5 = purple
	// 6 = cyan
	// 7 = white
	start_color();

	short current_color = 4; // blue
	init_pair(1,1,0);
	init_pair(2,2,0);
	init_pair(3,3,0);
	init_pair(4,4,0);
	init_pair(5,5,0);
	init_pair(6,6,0);
	init_pair(7,7,0);
	attron(COLOR_PAIR(current_color));
	while (true) {
		/* Print at row 0, col 0 */
		mvprintw (thing[0],thing[1],"%d",symbol++);

		thing[0]+=((semi_rand(2))*2)-1;
		thing[1]+=((semi_rand(2))*2)-1;
		if(thing[0]>maxx)	thing[0]=0;
		if(thing[0]<0)		thing[0]=maxx;
		if(thing[1]>maxy)	thing[1]=0;
		if(thing[1]<0)		thing[1]=maxy;

		refresh();
		//sleep(1);
		usleep(100000);
		if(semi_rand(37)==0) {
			attroff(COLOR_PAIR(current_color));
			//current_color=(current_color+1)%7+1; // avoiding black
			if(semi_rand(2)) current_color=4; //blue
			else if(semi_rand(2)) current_color=2; // green
			else if(semi_rand(2)) current_color=3; // yellow
			else if(semi_rand(2)) current_color=6; // cyan
			else if(semi_rand(2)) current_color=7; // white
			else if(semi_rand(2)) current_color=5; // purple
			else current_color=1; // red
			attron(COLOR_PAIR(current_color));
		}
	}
	attroff(COLOR_PAIR(current_color));
	sleep(10);
	/* End ncurses mode */
	endwin();
	return 0;
}

short rand_clock = 0;
int semi_rand(int mod) {
	unsigned int res = abs(rand()+time(NULL)+(97*rand_clock++))%mod;
	return res;
}
