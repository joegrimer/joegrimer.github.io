#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void record_to_memory(char *line);
void random_phrase_from_memory(char *_retort);

int main() {
    // Create a string
    char user_input[300];

    while (1) {
        // Ask the user to input some text
        printf("$ ");

        // Get and save the text
        fgets(user_input, 100, stdin);

        if (*(user_input+1) == '\0') break;

        record_to_memory(user_input);

        // Output the text
        // printf("> \n");
        user_input[0] = '\0';
        user_input[1] = '\0';

        char retort[100];
        random_phrase_from_memory(retort);
        record_to_memory(retort);
        printf("> %s", retort);
    }

    return 0;
}

short rand_clock = 0;
long semi_rand(long mod) {
    rand_clock+=97;
    //~ printf("t:%d\nr:%d\nc:%d\n",time(NULL),rand(),rand_clock);
    // labs is like abs but for longs
    unsigned int res = labs(rand()+time(NULL)+(673*rand_clock++))%mod;
    return res;
}

void random_phrase_from_memory(char *_retort) {
    FILE *fp = fopen("memory.txt", "r");

    char file_char = '?';
    long int linecount=0;
    while (file_char != EOF) {
        file_char=getc(fp);
        if ( file_char=='\n' ) linecount++;
    }
    fclose(fp);
    fp = fopen("memory.txt", "r");
    long choice = semi_rand(linecount);
    //printf("max %ld and choice %ld\n", linecount, choice);
    do {
        //printf("w");
        file_char=getc(fp);
        if (choice == 0) {
            *_retort = file_char;
            _retort++;
            //printf("a.[%c]", file_char);
        }
        if ( file_char=='\n' ) {
            if (choice <=0) {
                *_retort = '\0';
                break;
            }
            linecount++;
            choice--;
            //printf("dc");
        }
    } while (file_char != EOF);
    fclose(fp);
}

void record_to_memory(char *line) {

    /*
    FILE *fp = fopen("memory.txt", "r");

    char *line_ptr = line;
    char file_char = '?';
    while (file_char != EOF) {
        file_char=getc(fp);
        if ( *line_ptr != file_char ) {
            line_ptr = line;
            while (file_char != '\n' && file_char != EOF) {
                file_char=getc(fp);
            }
        } else if ( file_char=='\n' ) {
            line_ptr = line; // reset
            printf("That line was found in memory! %s\n", line);
        } else
            line_ptr++;
    }

    fclose(fp);*/

    FILE *fp2 = fopen("memory.txt", "a");

    fputs(line, fp2);

    fclose(fp2);
}
