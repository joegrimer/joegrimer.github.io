#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void record_to_memory(char *line);
void random_phrase_from_memory(char *_retort);
void generate_markov_word_phrase(char *_retort);

void pf(char *_s) {printf("%s\n",_s); 	fflush(stdout);}
void scan_dozen(char *_s) {
	printf("dozen: \"");
	for (int i=0;i<12;i++)
		if (_s[i]=='\0') printf("$");
		else printf("%c",_s[i]);
	printf("\"\n");
}

int main() {

	pf("Start");
	char retort[100];
	pf("about to generate");
	generate_markov_word_phrase(retort);
	printf("retort £ %s\n", retort);
	exit(0);
	// Create a string
	char user_input[300];

	while (1) {
		// Ask the user to input some text
		printf("$ ");

		// Get and save the text
		fgets(user_input, 100, stdin);

		if (*(user_input+1) == EOF) break;

		record_to_memory(user_input);

		// Output the text
		// printf("> \n");
		user_input[0] = EOF;
		user_input[1] = EOF;

		random_phrase_from_memory(retort);
		record_to_memory(retort);
		printf("£ %s\n", retort);
	}

	pf("end");
	return 0;
}

short rand_clock = 0;
long semi_rand(long mod) {
	rand_clock+=97;
	//~ printf("t:%d\nr:%d\nc:%d\n",time(NULL),rand(),rand_clock);
	// labs is like abs but for longs
	unsigned long res = labs(rand()+time(NULL)+(673*rand_clock++))%mod;
	return res;
}

long get_line_count() {
	FILE *fp = fopen("memory.txt", "r");
	char file_char = '?';
	long int line_count=0;
	while (file_char != EOF) {
		file_char=getc(fp);
		if ( file_char=='\n' ) line_count++;
	}
	fclose(fp);
	return line_count;
}

void read_word(char *word_buf, char *text_ptr) {
	short int max_out=50;
	while( *text_ptr != ' ' && *text_ptr != '\0' && *text_ptr != '\n') {
		printf("read word char to >%c<\n", *text_ptr);
		*word_buf = *text_ptr;
		text_ptr++;
		word_buf++;
		max_out--;
		if (max_out==0) {
			printf("This should not happen. Maxed out reading new word!");
			exit(1);
		}
	}
	pf("read word adding end");
	*word_buf = '\0';
}

unsigned long strlenj(char *word) {
	short int max_out=50;
	unsigned int w_len=0;
	while (*word != '\0') {
		w_len++;
	max_out--;
	if (max_out==0) {
	 printf("This should not happen. Maxed out jstrlen word!");
	 exit(1);
	}
	word++;
	}
  return w_len;
}

void generate_markov_word_phrase(char *retort) {
	pf("about to init");
	char file_char = '?';
	char file_buffer[99999];
	char *_file_buffer = file_buffer;
	char last_word[50];
	char this_word[50];
	char new_word[50];
	char *_last_word = last_word;
	char *_retort = retort;
	//unsigned short looped_count = 0;

	/* process:
	- get random line first word
	- find folllowups to that first word - including dollar
	- pick one
	- follow
	- finish eventually
	*/
	long line_count = 0;

	pf("about to read memory");
	FILE *fp = fopen("memory.txt", "r");
	while (1) {
		*_file_buffer = getc(fp);
		if (*_file_buffer == '\n') line_count++;
		if (*_file_buffer == EOF) break;
		_file_buffer++;
	}
	fclose(fp);

	pf("memory loaded");
	// reset pointer
	_file_buffer = file_buffer;

	printf("no of lines %ld", line_count);
	long choice = semi_rand(line_count);
	printf("no of lines %ld and I want %ld\n", line_count, choice);
	do {
		if (choice == 0) {
			read_word(_last_word, _file_buffer);
			break;
		} else if ( *_file_buffer=='\n' ) {
			choice--;
		}
		_file_buffer++;
	} while (*_file_buffer != EOF);
	printf("first word >%s<\n", last_word);

	// n.b. Resetting file_buffer. Not necessary?
	_file_buffer = file_buffer;

	do {
		if (*_file_buffer != ' ' && *_file_buffer != '\n' && *_file_buffer != EOF) {
			pf("file buffer before read word");
			scan_dozen(_file_buffer);
			read_word(this_word, _file_buffer);
			_file_buffer += strlenj(this_word); // either way
			printf("after %ld lenj", strlenj(this_word));
			scan_dozen(_file_buffer);
			printf("checkthis word like last word >%s< >%s<\n", this_word, last_word);
			if(strcmp(this_word, last_word) == 0) {
				printf("this word IS like last word >%s< >%s<\n", this_word, last_word);
				// skip a space if there is one
				if (*_file_buffer == ' ') _file_buffer++;
				if (*_file_buffer == '\n' || *_file_buffer == EOF) {
					pf("end of line or file. break");
					break;
				}
				read_word(new_word, _file_buffer);
				printf("new word is: >%s<\n", new_word);
				read_word(last_word, new_word);
				printf("last word is: >%s< \n", last_word);
			}
		}
		_file_buffer++;
	} while (*_file_buffer != EOF);
}

void random_phrase_from_memory(char *_retort) {
	FILE *fp = fopen("memory.txt", "r");

	char file_char = '?';
	long line_count=0;
	while (file_char != EOF) {
		file_char=getc(fp);
		if ( file_char=='\n' ) line_count++;
	}
	fclose(fp);
	fp = fopen("memory.txt", "r");
	long choice = semi_rand(line_count);
	//printf("max %ld and choice %ld\n", line_count, choice);
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
				*_retort = EOF;
				break;
			}
			line_count++;
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

