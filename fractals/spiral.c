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

	short current_color = 1; // red
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
		mvprintw (thing[0],thing[1],"Q");

			 if((c/2)+1%4==0)	thing[0]+=1;
		else if((c/2)%4==1) thing[1]+=1;
		else if((c/2)%4==2) thing[0]-=1;
		else				thing[1]-=1;

		refresh();
		//sleep(1);
		usleep(100000);
		c++;
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
