/* This is written for the sake of learning C
 * But perhaps it can turn into a good abstract game player and/or AI eventually!
 *
 * Joseph Grimer June-July 2018 */

#include <stdio.h>
#include <stdlib.h> // rand()
#include <time.h> // time()

// constants
#define BLACK_MAN 1
#define WHITE_MAN 2
#define BLACK_LION 3
#define WHITE_LION 4

#define MAX_ROUNDS 8192
#define EXPECTED_WINNERS 16 // should be roughly ROUNDS/2048

#define INVALID_MOVE -1
#define NO_RESULT 0
#define BLACK_WINS 1
#define WHITE_WINS 2

// global variables
static int turn = 0;
static int board[10][9];
static int black_pieces = 12;
static int white_pieces = 12;
static int winners[EXPECTED_WINNERS][90];
static int p_winners; // dodgy pointer to winners

// function declerations - in old-fashioned order
void setup_game();
int game_over(int x, int y);
int count_line(int x,int y,int chX,int chY);
int lion_scan(int *x, int *y, int *dx, int *dy);
int play_turn(int x, int y, int nx, int ny);
void print_board();
void get_human_input(int *x1, int *y1, int *x2, int *y2);
int human_v_human();
void make_simple_bot(int bot[], int seed); // generates preference board
int bot_v_bot(int *botA, int *botB);
int bot_v_human(int *botA);
char *current_player(); // returns string

main() {

	printf("\nWelcome to Ergo bot runner.\n");

	// The Human game

//	int resultA = human_v_human();
//	printf("Result: %d",resultA);
//	return;

	// the bot game

	// prepare the seed
	srand(time(0)%90);

	// Initiating the bots
	int bot1[90], bot2[90];
	make_simple_bot(bot1,5);
	make_simple_bot(bot2,97);

	// play a game
	int game_result = bot_v_human(bot1);//bot_v_bot(bot1,bot2);
	printf("Result: %d", game_result);
	print_board();

	printf("\n\nEnd of Program.\n");
}

///////////////////////// primary functions //////////////////////////////////

int bot_v_human(int *botA) {

	int handA = 0, turn_result = 0;
	int x=-1,y=-1,dx=-1,dy=-1;
	setup_game();
	printf("Bot vs human game initiated\n");

	for (turn=0;turn<100;turn++) { // <100 is a failsafe...

		if(turn%2==0) { // bot's turn
			if (handA >= 90) handA = 0; // loop hand - rare?
			x = *(botA + handA)/9;
			y = *(botA + handA)%9; // 9 is correct

			if(board[x][y]!=0 && board[x][y]%2==turn%2) {
				dx = *(botA + handA)/9;
				dy = *(botA + handA)%9;
			}

			int turn_result = play_turn(x,y,0,0);

			// increment hand
			handA++;
		} else { // human
			print_board();

			// user input
			if(turn%2) printf("White's move (x,y): ");
			else printf("Black's Move (x,y): ");

			get_human_input(&x,&y,&dx,&dy);

			turn_result = play_turn(x,y,dx,dy);
		}

		if(turn_result>0) return turn_result; // Game Over
		else if (turn_result<0) turn--;

		// I don know why this is neccessary... but it seems to be
		if(black_pieces<0 || white_pieces <0) return 0;
	}
}

int human_v_human() {

	setup_game();
	printf("Human v human game initiated\n");

	for (turn=0;turn<100;turn++) { // <100 is a failsafe...

		int x=-1,y=-1,dx=-1,dy=-1;
		print_board();

		// user input
		if(turn%2) printf("White's move (x,y): ");
		else printf("Black's Move (x,y): ");

		get_human_input(&x,&y,&dx,&dy);

		int turn_result = play_turn(x,y,dx,dy);

		if(turn_result>0) return turn_result; // Game Over
		else if (turn_result<0) turn--;
	}
}

int bot_v_bot(int *botA, int *botB) {

	setup_game();

	int handA = 0;
	int handB = 0;

	// the loop
	for(turn=0;turn<24;turn++) {

		int x,y;
		if (handA < 90 && handB < 90) {
			if(turn%2 == 0){
				x = *(botA + handA)/9;
				y = *(botA + handA)%9; // 9 is correct
			} else {
				x = *(botB + handB)/9;
				y = *(botB + handB)%9;
			}
		} else return 0; // ran out of hand

		int turn_result = play_turn(x,y,0,0);

		// check for win
		if (turn>8 && game_over(x,y)) {
			return ((turn%2)*2)-1; // -1 or 1
		}
		// increment hand
		if(turn%2 == 0) handA++;
		else handB++;

		// I don know why this is neccessary... but it seems to be
		if(black_pieces<0 || white_pieces <0) return 0;
	} // next turn
	// End of Game. nobody won!");
	return 0;
}

int play_turn(int x, int y, int nx, int ny) { // uses board

	// validation
	if(x<0|| x>9 || y<0 || y>8) {
		return INVALID_MOVE;
	} else if (board[x][y]!=0) { // something's there
		if(board[x][y]%2!=turn%2) { // it's yours
			int destination = board[nx][ny];
			if (destination!=0 || nx<0 || nx>9 || ny<0 || ny>8)
				return INVALID_MOVE; // destination off-board
			else if (board[x][y]>2 && board[nx][ny]==0 && lion_scan(&x,&y,&nx,&ny)) {
				board[nx][ny] = board[x][y]; // lion-move - possible upgrade
				board[x][y]=0;
			} else if ((abs(x-nx)>1 || abs(y-ny)>1) || (abs(x-nx)==0 && abs(y-ny)==0))
				return INVALID_MOVE; // out of proximity
			else if (board[x][y]<3 && (x!=nx && y!=ny))
				return INVALID_MOVE; // not for a man
			else { // lion - or valid
				if(nx==0 || ny==0 || x==8 || y==9) board[nx][ny] = (turn%2)+3; // lion
				else board[nx][ny] = board[x][y]; // whatever it previously was
				board[x][y]=0;
			}
		} else return INVALID_MOVE; // not your piece
	} else if(((turn%2)==1 && white_pieces==0) ||
		   ((turn%2)==0 && black_pieces==0)) {
		return INVALID_MOVE;
	} else {
//		printf("You entered: %d and %d\n\n",x,y);
		if(x==0||y==0||x==9||y==8) board[x][y] = (turn%2)+3; // place lion
		else board[x][y] = (turn%2)+1; // place man
		// remove piece
		if((turn%2)==1) white_pieces--;
		else black_pieces--;
	}
	// check for win
	if (turn>7 && game_over(x,y)) {
		print_board();
		printf("Game Over... %s wins!",current_player());
		return (turn%2)+1; // 1 or 2
	}
	// else
	return 0;
}

//////////////////////////////// secondary functions ///////////////////////////

int lion_scan(int *x, int *y, int *dx, int *dy) {
	int sx = *x, sy = *y; // scanner position
	//return 1;
	if((*x!=0 && *x!=9 && *y!=0 && *y!=8) || // not even in the right place
	   (*dx!=0 && *dx!=9 && *dy!=0 && *dy!=8) ) // or going there
	   {printf("neither here nor there(%d,%d>%d,%d)\n",*x,*y,*dx,*dy);return 0;}
	while(1) { // clockwise
			 if(*x==9 && *y<=8) sy=*x+1; // 
		else if(*x==0 && *y>=0) sy=*y+1; // up
		else if(*x<=9 && *y==8) sx=*y-1; // 
		else if(*x>=0 && *y==0) sx=*x-1; // 
		printf(" (scanning %d,%d) ",sx,sy);
		break;
	}
	return 1;
}

// expects pointers - todo ignore multiple spaces
void get_human_input(int *x1, int *y1, int *x2, int *y2) {
	int last_char,i;
	int coords[4];
	int p_coords = 0;

	for(i=0;i<4;i++) coords[i]=0; // defaulting moves to 0,0

	do {
		last_char = getchar();
		if(last_char>47 && last_char < 58)
			coords[p_coords] = coords[p_coords]*10+(last_char-48);
		else p_coords++;
	} while (last_char!=10 && p_coords<4);

	// effectively returning:
	*x1 = coords[0];
	*y1 = coords[1];
	*x2 = coords[2];
	*y2 = coords[3];
//	printf("end\n");
}

void make_simple_bot(int bot[], int seed) {
	int k;

	for(k=0;k<90;k++) bot[k] = k;

	for(k=0;k<255;k++) { // 90 min... more than 256 probably overkill
		int randy1 = abs( (rand()+seed)%(90) );
		int randy2 = abs( (rand()+seed)%(90) );

		int temp = bot[randy1];

		bot[randy1] = bot[randy2];
		bot[randy2] = temp;
		if(randy1<0 || randy1 > 90 || randy2 < 0 || randy2 > 90) {
			printf("DIE PROGRAM!! DIE!!! %d,%d",randy1,randy2);
			return;
		}
	}
}

void setup_game() {

	// reset turn
	turn = 0;

	// reset pieces
	black_pieces = 12;
	white_pieces = 12;

	// reset board
	int x,y;
	for(x=0;x<10;x++) {
		for(y=0;y<9;y++) {
			board[x][y] = 0;
		}
	}
}

// possibly working
int game_over(int x, int y) { // and turn
	//int colour = board[x][y];
	if( (count_line(x+1,y-1,1,-1) + count_line(x-1,y+1,-1, 1) > 3) ||
		(count_line(x+0,y+0,1, 0) + count_line(x-1,y+0,-1, 0) > 3) ||
		(count_line(x+0,y+1,0, 1) + count_line(x+0,y-1, 0,-1) > 3) ||
		(count_line(x+1,y+1,1, 1) + count_line(x-1,y-1,-1,-1) > 3) )
		return 1;
	else return 0;
}
// check a line for 5 in a row - a recursive function
int count_line(int x,int y,int chX,int chY) {
//	printf("(s:%d,t:%d)",board[x][y]%2,(turn+1)%2);
	if (!(x < 0 || x > 9 || y < 0 || y > 8) &&
		board[x][y]>0 && board[x][y]%2 == (turn+1)%2 ) {
		return count_line(x+chX,y+chY,chX,chY)+1;
	} else return 0;
}

char * current_player() {
	char * playerName;
	if(turn%2==0) playerName = "black";
	else playerName = "white";
	return playerName;
}

// print board
void print_board() {

	int i,j;

	// white pieces left
	printf("\n/ ");
	for(i=0;i<white_pieces;i++) {
		if(i==white_pieces-1 && turn%2==1) printf("O"); // last column
		else printf("o");
		if(i==2 || i==5 || i==8) printf(" "); // halfway
	}
	for (i=0;i<((12-white_pieces)+(12-white_pieces)/3);i++) printf(" ");
	printf(" \\\n");

	// print board
	for(j=8;j>=0;j--) {
		for(i=0;i<10;i++) {

			switch (board[i][j]) {
				case 0:
					if(i==0 || i==9) printf("|");
					else if(j==0 || j==8) printf("~");
					else printf(".");
					break;
				case BLACK_MAN:
					printf("x");
					break;
				case BLACK_LION:
					printf("X");
					break;
				case WHITE_MAN:
					printf("o");
					break;
				case WHITE_LION:
					printf("O");
					break;
			}
			printf(" ");
		}
		printf("\n");
	}

	// black pieces left
	printf("\\ ");
	for(j=0;j<black_pieces;j++) {
		if(j==black_pieces-1 && turn%2==0) printf("X"); // last column
		else printf("x");

		if(j==2 || j==5 || j==8) printf(" "); // halfway
	}
	for (j=0;j<12-black_pieces;j++)	printf(" ");
	printf(" /\n");
}


