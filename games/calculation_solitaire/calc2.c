/*****************************************************
 * Calculation Solitaire
 * Joseph Grimer
 * November 2018
 * This is translated from a python program into C
 * to simulate a solitaire cardgame called calculation
 * and perhaps to solve it in some sense
 * or atleast win it once!
 * 
 * n.b. I am defining functions in order instead of predeclaring them.
 * */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define DECK_LENGTH 48 // 52 minus the four starter cards (A,2,3,4)
#define MAX_INITIAL_GAMES 999999999 // the number of random sequences that will be first tried to find promising solutions
#define MINIMUM_SCORE 40 // quality control out of 52 - lower is better
#define FIRST_BATCH 1023 // max 32767
#define dprint(expr) printf(#expr " = %d\n", expr)
#define SHUFFLE_SWAPS 48

void print_ary(int things[], int max);
int precedes(int card_A, int card_B);
int succedes(int card_A, int card_B);
int play_to_top (int (*bottom_row)[48], int *bottom_row_indexes, int *top_row);
int play_out_game(int *sequence, int* deck);
int play_out_game_a(int *sequence, int* deck);
int play_out_game_b(int* deck);
void print_board(int* deck, int deck_index, int* top_row, int (*bottom_row)[48], int* bottom_row_indexes);
int is_hopeful(int* top_row, int (*bottom_row)[48], int* bottom_row_indexes);
int semi_rand(int mod);
int normalise_sequence(int *sequence);
int break_finder(int *sequence, int * deck);
int sequence_tweaker(int *sequence, int *deck);
int is_hopeful_move(int* top_row, int (*bottom_row)[48], int* bottom_row_indexes, int card, int bottom_row_column);

int main() {
    printf("--------------------------------------------------------\n");
    printf("Calculation Solitaire Simulator\n"
    "Please await results (lower is better, 4-52)\n\n");
    
    int h,i,j,k,result,success_stories = 0, total = 0, best = 52;

    int deck[DECK_LENGTH] = {
        11,1,5,6,3,2,5,2,13,12,
        9,13,1,6,8,6,4,10,11,8,
        12,13,4,7,11,12,10,7,13,9,
        9,8,4,11,10,9,3,2,10,6,
        3,12,5,1,8,7,7,5};

    int sequence[DECK_LENGTH] = {0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3}; // 39 (28)
    //~ int success_sequences[FIRST_BATCH][DECK_LENGTH];

    printf("raw score: %d\n",play_out_game_b(deck));
    
    printf("\nEnd of program.\n--------------------------------------------------------\n");
    return 0;
}

void shuffle_deck(int *deck_pointer) {
    for(i=0;i<SHUFFLE_SWAPS;i++) {
        semi_rand(48)
    }
}

int sequence_tweaker(int *sequence, int *deck) {
    printf("Starting Break Finder\n");

    int augmented_sequence[DECK_LENGTH] = {0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0};
    int i, j, k, l, result,column;
    for(l=0;l<99999999;l++) {
        for(k=0;k<DECK_LENGTH;k++) {
            if(semi_rand(5)) augmented_sequence[k]=semi_rand(4);
            else augmented_sequence[k] = sequence[k];
        }
        result = play_out_game(augmented_sequence,deck);

        if(result<23) {
            printf("it could be %d\n",result); // i, deck[i]
            for(i=0;i<DECK_LENGTH;i++) printf("%d",augmented_sequence[i]);
            printf("\n");
        }
    }

    printf("Ending Break Finder\n");
}

int break_finder(int *sequence, int *deck) {
    printf("Starting Break Finder\n");

    int augmented_sequence[DECK_LENGTH] = {0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0};
    int i, j, k, l, result,column,best_index = -1,best_value = -1,best_score = 52;
    for(l=0;l<10;l++) {
        for(i=0;i<DECK_LENGTH;i++) {
            column = 0;
            for(j=0;j<4;j++) {
                for(k=0;k<DECK_LENGTH;k++) {
                    if(k==i) augmented_sequence[k]=j;
                    else augmented_sequence[k] = sequence[k];
                }
                result = play_out_game(augmented_sequence,deck);
                column += result;
                if(result<=best_score) { // err towards end of sequence 0 i.e. Change early moves if equally useful
                    best_score = result;
                    best_index = i;
                    best_value = j;
                }
                //~ for(k=0;k<result;k++) printf(".");
                //~ printf("(%d=>%d) ",j,result);
            }
            //~ for(j=0;j<column;j++) printf(".");
            //~ printf("%d\n",column); // i, deck[i]
        }
        printf("changing column %d to %d will achieve score %d\n",best_index,best_value,best_score); // i, deck[i]
        sequence[best_index] = best_value;
    }

    printf("Ending Break Finder\n");
}

int splice_sequences(int **sequences,int sequences_i) {
    int sequence_b = 0, splice_point = 0, spare = 0, h, i;
    for(h=0;h<sequences_i;h++) {
        sequence_b = (h+(sequences_i/2))%sequences_i;
        //~ printf("a: %d b: %d, ",h,sequence_b);
        splice_point = 5+semi_rand(40);
        
        for(i=0;i<splice_point;i++) {
            if(semi_rand(26)==0) spare = semi_rand(4); // random mutation
            else spare = sequences[h][i];
            sequences[h][i] = sequences[sequence_b][i];
            sequences[sequence_b][i] = spare;
        }
    }
}
int play_out_game_b(int * deck) {
    int i, j, k; // miscallenious variables

    // reset the game with the pre-shuffled deck
    int deck_index = 47; // pointing at last member of deck
    int top_row[] = {1,2,3,4}; // the top row of cards - always starts ace to four
    int bottom_row[4][48]; // the bottom row of cards
    for(i=0;i<(48*4);i++) bottom_row[i/48][i%48]=0; // initialise bottom row
    int bottom_row_indexes[] = {0,0,0,0};
    int placement_column, column_result, drawn_card, column_picked; // used later
    //~ int preferences[13][4] = {
        //~ 1: [2, 3, 4, 5],
        //~ 2: [3, 4, 5, 6],
        //~ 3: [4, 5, 6, 7],
        //~ 4: [5, 6, 7, 8],
        //~ 5: [6, 7, 8, 9],
        //~ 6: [7, 8, 9, 10],
        //~ 7: [8, 9, 10, 11],
        //~ 8: [9, 10, 11, 12],
        //~ 9: [10, 11, 12, 0],
        //~ 10: [11, 12, 0, 1],
        //~ 11: [12, 0, 1, 2],
        //~ 12: [0, 1, 2, 3]
    //~ }

    // simulate the game - 96 max turns
    for(i=0;i<=61;i++){
        printf("a. %d+",i);
        column_result = play_to_top(bottom_row,bottom_row_indexes,top_row);

        if(column_result>0) {
            j = (column_result-1)/4;
            k = (column_result-1)%4;

            top_row[k] = bottom_row[j][bottom_row_indexes[j]-1]; // copy the card to top
            bottom_row[j][bottom_row_indexes[j]-1] = 0; // empty that slot - just in case
            bottom_row_indexes[j]--; // move its index
            continue;
        }
        printf("b. %d+",i);
        
        // if we got this far, then we have placed what cards we can, and may as well draw a card
        drawn_card = deck[deck_index];
        placement_column = 0; // by default
        int bottom_row_priorities[] = {132,132,132,132};

        column_picked = 0;

        // first stregegy - by most important card in each stack
        unsigned int col_iterator, col;
        int ranks_used[] = {4,4,4,4,4,4,4,4,4,4,4,4,4};
        
        // first count up the cards that we've used
        for (j=0;j<4;j++) {
            
            col = top_row[j];
            ranks_used[col-1] -= 1;
            col_iterator = j+1;
            

            while (col != col_iterator) {
                col = ((col-col_iterator)%13);
                ranks_used[col-1] -= 1;
            }
        }
        
        printf("c. %d+",i);

        printf("Ranks Used : ");
        for(j=0;j<13;j++) printf("%d,",ranks_used[j]);
        
        for(j=0;j<4;j++)
            for(k=0;k<bottom_row_indexes[j];k++)
                //~ if(ranks_used[bottom_row[j][bottom_row_indexes[k]]]<bottom_row_priorities[j])
                bottom_row_priorities[j] -= ranks_used[bottom_row[j][bottom_row_indexes[k]]];
        // second strategy - by top card pairing
        if(column_picked<1) {
            for(j=0;j<4;j++) {
                printf("drawn is %d and top bot is %d? ",drawn_card, bottom_row[j][bottom_row_indexes[j]-1]);
                if((bottom_row[j][bottom_row_indexes[j]-1] - drawn_card+13)%13 < 4) {
                    
                    column_picked = 1;
                    placement_column = j;
                    printf("yes\n");
                } else printf("no\n");
            }
        }
        // third strategy - by number of cards in a stack
        if(column_picked<1) {
            int max = 48;
            for(j=0;j<4;j++) {
                //~ printf("bri:%d\n",bottom_row_indexes[j]);
                if(bottom_row_indexes[j]<max) {
                    //~ printf("j:%d, bri:%d, max:%d\n",bottom_row_indexes[j],max,j);
                    placement_column = j;
                    max = bottom_row_indexes[j];
                }
            }
            column_picked = 2;
        }
        
        // finally, total up values
        printf("Bottom row priorities : ");
        int max = 0;
        for(j=0;j<4;j++) {
            if(bottom_row_priorities[j]>max) {
                max = bottom_row_priorities[j];
                placement_column = j;
                column_picked = 1;
            }
            printf("%d,",bottom_row_priorities[j]);
        }
        print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);

        bottom_row[placement_column][bottom_row_indexes[placement_column]] = drawn_card;
        bottom_row_indexes[placement_column]++;
        deck_index--; // card has been removed from deck
        
        if(deck_index<0) {
            //~ printf("Ran out of cards, or sequence. Breaking...\n");
            break;
        }
        //~ else if (!is_hopeful(top_row, bottom_row, bottom_row_indexes)) {
            //~ printf("Ran out of hope. Breaking...\n");
            //~ print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
            //~ break;
        //~ }
        printf("y. %d+",i);
        print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
        printf("z. %d+",i);
    }
    //~ printf("association:%d; least:%d;",strategies_used[0],strategies_used[1]);

    // score the game based on cards played to sets
    int result = 52 - (
        bottom_row_indexes[0] +
        bottom_row_indexes[1] +
        bottom_row_indexes[2] +
        bottom_row_indexes[3] );

    //~ if(result<MINIMUM_SCORE) print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
    
    return result;
}

int play_out_game_a(int *sequence, int * deck) {
    int i, j, k; // miscallenious variables

    // reset the game with the pre-shuffled deck
    int deck_index = 47; // pointing at last member of sequence
    int sequence_index = 47; // pointing at last card in deck
    int top_row[] = {1,2,3,4}; // the top row of cards - always starts ace to four
    int bottom_row[4][48]; // the bottom row of cards
    for(i=0;i<(48*4);i++) bottom_row[i/48][i%48]=0; // initialise bottom row
    int bottom_row_indexes[] = {0,0,0,0};
    int placement_column, column_result; // used later

    // simulate the game - 96 max turns
    for(i=0;i<=96;i++){
        //~ printf("%d+",i);
        //~ fflush(stdout);
        //~ if(column_result = play_to_top(bottom_row,bottom_row_indexes,top_row)) {
        column_result = play_to_top(bottom_row,bottom_row_indexes,top_row);

        if(column_result>0) {
            j = (column_result-1)/4;
            k = (column_result-1)%4;

            top_row[k] = bottom_row[j][bottom_row_indexes[j]-1]; // copy the card to top
            bottom_row[j][bottom_row_indexes[j]-1] = 0; // empty that slot - just in case
            bottom_row_indexes[j]--; // move its index
            continue;
        }
        
        sequence[sequence_index] = 0;
        int max = 48;
        for(j=0;j<4;j++) {
            //~ printf("bri:%d\n",bottom_row_indexes[j]);
            if(bottom_row_indexes[j]<max) {
                //~ printf("j:%d, bri:%d, max:%d\n",bottom_row_indexes[j],max,j);
                sequence[sequence_index] = j;
                max = bottom_row_indexes[j];
            }
        }

        // if we got this far, then we have placed what cards we can, and may as well draw a card
        placement_column = sequence[sequence_index];
        bottom_row[placement_column][bottom_row_indexes[placement_column]] = deck[deck_index];
        bottom_row_indexes[placement_column]++;
        deck_index--; // card has been removed from deck
        sequence_index--; // card has been placed on column from sequence
        
        if(deck_index<0 || sequence_index<0) {
            //~ printf("Ran out of cards, or sequence. Breaking...\n");
            break;
        }
        //~ else if (!is_hopeful(top_row, bottom_row, bottom_row_indexes)) {
            //~ printf("Ran out of hope. Breaking...\n");
            //~ print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
            //~ break;
        //~ }
        //~ print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
    }
    print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);

    // score the game based on cards played to sets
    int result = 52 - (
        bottom_row_indexes[0] +
        bottom_row_indexes[1] +
        bottom_row_indexes[2] +
        bottom_row_indexes[3] );

    //~ if(result<MINIMUM_SCORE) print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
    
    return result;
}

int play_out_game(int *sequence, int * deck) {
    int i, j, k; // miscallenious variables

    // reset the game with the pre-shuffled deck
    int deck_index = 47; // pointing at last member of sequence
    int sequence_index = 47; // pointing at last card in deck
    int top_row[] = {1,2,3,4}; // the top row of cards - always starts ace to four
    int bottom_row[4][48]; // the bottom row of cards
    for(i=0;i<(48*4);i++) bottom_row[i/48][i%48]=0; // initialise bottom row
    int bottom_row_indexes[] = {0,0,0,0};
    int placement_column, column_result; // used later

    // simulate the game - 96 max turns
    for(i=0;i<=96;i++){
        //~ printf("%d+",i);
        //~ fflush(stdout);
        //~ if(column_result = play_to_top(bottom_row,bottom_row_indexes,top_row)) {
        column_result = play_to_top(bottom_row,bottom_row_indexes,top_row);

        if(column_result>0) {
            j = (column_result-1)/4;
            k = (column_result-1)%4;

            top_row[k] = bottom_row[j][bottom_row_indexes[j]-1]; // copy the card to top
            bottom_row[j][bottom_row_indexes[j]-1] = 0; // empty that slot - just in case
            bottom_row_indexes[j]--; // move its index
            continue;
        }

        // if we got this far, then we have placed what cards we can, and may as well draw a card
        placement_column = sequence[sequence_index];
        bottom_row[placement_column][bottom_row_indexes[placement_column]] = deck[deck_index];
        bottom_row_indexes[placement_column]++;
        deck_index--; // card has been removed from deck
        sequence_index--; // card has been placed on column from sequence
        
        if(deck_index<0 || sequence_index<0) {
            //~ printf("Ran out of cards, or sequence. Breaking...\n");
            break;
        }
        //~ else if (!is_hopeful(top_row, bottom_row, bottom_row_indexes)) {
            //~ printf("Ran out of hope. Breaking...\n");
            //~ print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
            //~ break;
        //~ }
        //~ print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
    }

    // score the game based on cards played to sets
    int result = 52 - (
        bottom_row_indexes[0] +
        bottom_row_indexes[1] +
        bottom_row_indexes[2] +
        bottom_row_indexes[3] );

    //~ if(result<MINIMUM_SCORE) print_board(deck,deck_index,top_row,bottom_row,bottom_row_indexes);
    
    return result;
}

void print_board(int* deck, int deck_index, int* top_row, int (*bottom_row)[48], int* bottom_row_indexes) {
    int i = 2, j, loop_again = 1;
    printf("\n    %02d|%02d|%02d|%02d\n",top_row[0],top_row[1],top_row[2],top_row[3]);
    printf("%02d  %02d %02d %02d %02d\n",deck[deck_index],
    bottom_row[0][bottom_row_indexes[0]-1],
        bottom_row[1][bottom_row_indexes[1]-1],
        bottom_row[2][bottom_row_indexes[2]-1],
        bottom_row[3][bottom_row_indexes[3]-1]);
    while(loop_again) {
        printf("looping again %d",i);
        loop_again=0;
        printf("    ");
        for(j=0;j<4;j++) {
            printf("inner loop %d",j);
            if(bottom_row_indexes[j]>=i) {
                printf("%02d ",bottom_row[j][bottom_row_indexes[j]-i]);
                loop_again = 1;
            } else printf("   ");
        }
        printf("\n");
        
        printf("end of loop %d",i);
        i++;
    }
}

// this function will detirmine if any card can be played from the bottom row to the top
int play_to_top(int (*bottom_row)[48] , int *bottom_row_indexes, int *top_row) {
    int j, k, next_top_card, bottom_card;
    
    //~ for(j=0;j<4;j++) for(k=0;k<48;k++) printf("%i|",bottom_row[j][k]);
    //~ printf("\n");

    for(j=0;j<4;j++) { // for j in bottom row
        if(bottom_row_indexes[j]>0) {
            for(k=0;k<4;k++) { // for k in top row
                bottom_card = bottom_row[j][bottom_row_indexes[j]-1];
                next_top_card = (top_row[k]+k+1)%13; // todo bug: this could carry on playing after 0!
                if (next_top_card==bottom_card) {
                    if(next_top_card==0) {
                        printf("A column has died. Long live the column. NOW FIX THIS LOOPHOLE!");
                        exit(0);
                    }
                    //~ printf("j is %i and k is %i, so encoded is %i",j,k,((j*4)+(k))+1);
                    return ((j*4)+(k))+1; // thereby encoding values of j and k into response
                }
            }
        }
    }
    return 0;
}

// any given sequence will be rotationally equivalent to about 12 different sequences.
// this function seeks to normalise this, thus resulting in less sequences.
// this function takes a pointer, and edits the source array.
int normalise_sequence(int *sequence) {
    int i, normalisation_counter = 0,current_number;
    int normalisation_switchboard[4] = {-1,-1,-1,-1};
    
    //~ printf("orient sequence before: ");
    //~ for(i=0;i<DECK_LENGTH;i++) {
        //~ printf("%d,",sequence[i]);
    //~ }
    for(i=0;i<DECK_LENGTH;i++) {
        current_number = sequence[i];
        if (normalisation_counter<4 && normalisation_switchboard[current_number]==-1) {
            normalisation_switchboard[current_number]=normalisation_counter;
            normalisation_counter++;
        }
        sequence[i] = normalisation_switchboard[current_number];
    }
    //~ printf("\norient sequence after: ");
    //~ for(i=0;i<DECK_LENGTH;i++) {
        //~ printf("%d,",sequence[i]);
    //~ }
    //~ printf("\nEOF\n");
}

// this function is used to establish whether the game has definetly reached a point where it's unwinnable
int is_hopeful(int* top_row, int (*bottom_row)[48], int* bottom_row_indexes) {
    //~ printf("Checking for hopelessness");
    //~ fflush(stdout);
    int i, j, k, precedes_result;
    unsigned int col_iterator, col;
    int ranks_used[] = {0,0,0,0,0, 0,0,0,0,0, 0,0,0};
    
    // first count up the cards that we've used
    for (i=0;i<4;i++) {
        //~ printf("%d&",i);
        //~ fflush(stdout);
        
        col = top_row[i];
        ranks_used[col-1] += 1;
        col_iterator = i+1;
        
        //~ printf("col is %d and coli is %d.",col,col_iterator);
        //~ fflush(stdout);

        while (col != col_iterator) {
            col = ((col-col_iterator)%13);
            //~ printf("col is %d and coli is %d.",col,col_iterator);
            //~ fflush(stdout);
            ranks_used[col-1] += 1;
        }
    }
    //~ for(i=0;i<13;i++) printf("%d, ",ranks_used[i]);
    //~ exit(0);
    
    
    // then go through bottom_row comparing cards to cards lower on the stack
    for(i=0;i<4;i++) {
        //~ printf("X");
        for(j=0;bottom_row_indexes[i]-j>0;j++) {
            //~ printf("R");
            for(k=j+1;bottom_row_indexes[i]-k>0;k++) {
                precedes_result = precedes(bottom_row[i][bottom_row_indexes[i]-j-1],
                        bottom_row[i][bottom_row_indexes[i]-k-1]);
                if(precedes_result>(4-ranks_used[ bottom_row[i][bottom_row_indexes[i]-j-1] -1])) {
                    //~ printf("%d preceedes %d? %d.\n ",
                        //~ bottom_row[i][bottom_row_indexes[i]-j-1],
                        //~ bottom_row[i][bottom_row_indexes[i]-k-1],
                        //~ precedes_result
                        //~ );
                    return 0; //exit(0);
                }
            }
        }
    }
    return 1;
}

// this function is used to establish whether a move will render the game unwinnable
int is_hopeful_move(int* top_row, int (*bottom_row)[48], int* bottom_row_indexes, int card, int bottom_row_column) {
    //~ printf("Checking for hopelessness");
    //~ fflush(stdout);
    int i, j, k, precedes_result;
    unsigned int col_iterator, col;
    int ranks_used[] = {0,0,0,0,0, 0,0,0,0,0, 0,0,0};
    
    //~ printf("Counting use\n");
    // first count up the cards that we've used
    for (i=0;i<4;i++) {
        //~ printf("i: %d\n",i);
        //~ printf("%d&",i);
        //~ fflush(stdout);
        
        col = top_row[i];
        ranks_used[col-1] += 1;
        col_iterator = i+1;
        
        //~ printf("col is %d and coli is %d.",col,col_iterator);
        j = 0;

        while (col != col_iterator) {
            //~ printf("c:%d,ci:%d,\n",col,col_iterator);

            col = ((col-col_iterator+13)%13);
            //~ fflush(stdout);
            ranks_used[col-1] += 1;
            if (++j>11) {
                printf("TSNH... col: %d, coli: %d",col, col_iterator);
                exit(0);
            }
        }
    }
    //~ for(i=0;i<13;i++) printf("%d, ",ranks_used[i]);
    //~ exit(0);
    
    // then go through bottom_row comparing cards to cards lower on the stack
    i = bottom_row_column;
    printf("i=%d\n",i);
    printf("starting loop\n");
    for(j=0;bottom_row_indexes[i]-j>0;j++) {
        //~ printf("R");
        for(k=j+1;bottom_row_indexes[i]-k>0;k++) {
            precedes_result = precedes(bottom_row[i][bottom_row_indexes[i]-j-1],
                    bottom_row[i][bottom_row_indexes[i]-k-1]);
            if(precedes_result>(4-ranks_used[ bottom_row[i][bottom_row_indexes[i]-j-1] -1])) {
                //~ printf("%d preceedes %d? %d.\n ",
                    //~ bottom_row[i][bottom_row_indexes[i]-j-1],
                    //~ bottom_row[i][bottom_row_indexes[i]-k-1],
                    //~ precedes_result
                    //~ );
                printf("giving up\n");
                return 0; //exit(0);
            }
        }
    }
    printf("giving hope\n");
    return 1;
}

int precedes(int card_A, int card_B) { // only 13*12=166 combos
    int matches = 0;
    card_B %= 13;
    int column, card_C;
    for (column=1;column<=4;column++) {
        card_C = card_A%13;
        while (card_C!=0) {
            card_C = (card_C + column)%13;
            if (card_C==card_B) {
                matches++;
                break;
            }
        }
    }
    return matches;
}

int succedes(int card_A, int card_B) {
    return 4-precedes(card_A,card_B); // exception for 12 and such?
}

short rand_clock = 0;
int semi_rand(int mod) {
    rand_clock+=97;
    //~ printf("t:%d\nr:%d\nc:%d\n",time(NULL),rand(),rand_clock);
    unsigned int res = abs(rand()+time(NULL)+(673*rand_clock++))%mod;
    return res;
}
/*
int play_out_games(int **sequences,int *deck) {
    for(h=0;h<MAX_INITIAL_GAMES;h++) {
        for(i=0;i<DECK_LENGTH;i++) {
            sequence[i] = semi_rand(4);
        }
        result = play_out_game(sequence, deck);
        if(result<MINIMUM_SCORE) {
            if(result<best) best = result;
            
            total+=result;

            normalise_sequence(sequence);
            
            for(k=0;k<DECK_LENGTH;k++) success_sequences[success_stories][k] = sequence[k];

            success_stories++;
            if(success_stories>=FIRST_BATCH) break;
        }
    }

    printf("I played out %d games.\n%d were below %d"
    "(52 is worst... 0 is a win)\n"
    "The average was %d. The best was %d\n\n",
        h,success_stories,MINIMUM_SCORE,(total/success_stories),best);
    
}*/

/* best sequences for deck {
        11,1,5,6,3,2,5,2,13,12,
        9,13,1,6,8,6,4,10,11,8,
        12,13,4,7,11,12,10,7,13,9,
        9,8,4,11,10,9,3,2,10,6,
        3,12,5,1,8,7,7,5};
 * are 
 * {
//~ 0,1,2,3,1,2,2,2,1,2,
//~ 1,3,1,3,1,0,1,1,1,2,
//~ 1,3,3,1,1,1,2,1,0,1,
//~ 3,1,1,1,0,3,2,1,0,3,
//~ 1,2,1,0,0,0,0,0}; // ?

//~ int sequence[DECK_LENGTH] = {
//~ 0,1,2,3,0,1,2,3,0,1,2,3,
//~ 0,1,2,3,0,1,2,3,0,1,2,3,
//~ 0,1,2,3,0,1,2,3,0,1,2,3,
//~ 0,1,2,3,0,1,2,3,0,1,2,3}; // ?
 * 
    //~ int sequence[DECK_LENGTH] = {3,1,1,1,1,0,1,2,2,1,2,3,1,0,2,1,1,0,2,2,2,3,1,0,0,2,0,0,3,3,0,2,1,0,3,2,1,2,0,3,2,2,3,0,0,3,0,3}; // 31 (31)
    //~ int sequence[DECK_LENGTH] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}; // 48 (23)
    //~ int sequence[DECK_LENGTH] = {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,}; // (27)
 * 32={2,1,2,3,2,0,1,3,1,2,0,0,1,1,1,3,0,1,0,3,0,1,3,0,0,2
 * ,1,0,2,1,0,0,1,0,2,0,1,3,2,0,0,1,2,3,1,1,2,2}; // 32
 * 
 * 31 ={3,1,1,1,1,0,1,2,2,1,2,3,1,0,2,1,1,0,2,
 * 2,2,3,1,0,0,2,0,0,3,3,0,2,1,0,3,2,1,2,0,3,2,2,3,0,0,3,0,3}; // 31
 * 
 * b:31=233301202301333121003120323211010231003112300333
 * b:31=011220020303333030111030320220101223332333200022
 * 
*/
