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
	for (int i=0;i<12;i++) {
		if (_s[i]=='\0') printf("$");
		else if (_s[i]==EOF) printf("X");
		else printf("%c",_s[i]);
		}
	printf("\"\n");
}

int main() {

	pf("Start");
	char retort[300];
	pf("about to generate");
	generate_markov_word_phrase(retort);
	printf("retort £ %s\n", retort);
	exit(0);
	// */
	// Create a string
	char user_input[300];
	*user_input = '\0';

	while (1) {
		// Ask the user to input some text
		printf("$ ");

		// Get and save the text
		fgets(user_input, 299, stdin);

		// I don't know why, but this works!
		if (*(user_input) == '\n') break;

		record_to_memory(user_input);

		generate_markov_word_phrase(retort);
		// random_phrase_from_memory(retort);
		record_to_memory(retort);
		printf("£ %s\n", retort);
	}

	pf("end");
	return 0;
}

short rand_clock = 0;
long semi_rand(long mod) {
	if (mod<2) return 0;
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
		*word_buf = *text_ptr;
		text_ptr++;
		word_buf++;
		max_out--;
		if (max_out==0) {
			printf("This should not happen. Maxed out reading new word!");
			exit(1);
		}
	}
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
	char file_buffer[99999];
	char *_file_buffer = file_buffer;
	char last_word[50];
	char this_word[50];
	char *_last_word = last_word;
	int entropy = 5;

	/* process:
	- get random line first word
	- find folllowups to that first word - including dollar
	- pick one
	- follow
	- finish eventually
	*/
	long line_count = 0;

	FILE *fp = fopen("memory.txt", "r");
	while (1) {
		*_file_buffer = getc(fp);
		if (*_file_buffer == '\n') line_count++;
		if (*_file_buffer == EOF) break;
		_file_buffer++;
	}
	fclose(fp);

	// reset pointer
	_file_buffer = file_buffer;
	int line_number = 1;

	// Will only pick first word from even lines
	// To prevent bot learning from it's own mistakes
	long choice = semi_rand(line_count/2)*2;
	do {
		if (choice == 0) {
			read_word(_last_word, _file_buffer);
			_file_buffer += strlenj(last_word);
			break;
		} else if ( *_file_buffer=='\n' ) {
			line_number++;
			choice--;
		}
		_file_buffer++;
	} while (*_file_buffer != EOF);
	//printf("first word >%s<\n", last_word);
	//printf("%s ", last_word);
	sprintf(retort, "%s", last_word);
	retort += (strlenj(last_word));

	/*
	for(;*_file_buffer!=EOF;_file_buffer++) {
		printf("%c", *_file_buffer);
		if (*_file_buffer=='\n') {
			line_number++;
			printf("%d. ", line_number);
		}
	}
	return;*/

	// n.b. Resetting file_buffer. Not necessary?
	// _file_buffer = file_buffer;

	printf("before main loop ln is %d, but choice was %ld\n", line_number, choice);
	int loop_max=19;
	while (loop_max > 0) {
		if (*_file_buffer == EOF) {
			loop_max--;
			_file_buffer = file_buffer;
			pf("Resetting line number");
			line_number = 1;
		}
		printf(".");
		if (*_file_buffer == '\n') {
			line_number++;
			printf("%d-", line_number);
		}
		if (*_file_buffer != ' ' && *_file_buffer != '\n' && *_file_buffer != EOF) {
			read_word(this_word, _file_buffer);
			_file_buffer += strlenj(this_word); // either way
			if(strcmp(this_word, last_word) == 0) {
				if (entropy && semi_rand(2)==0) {
					entropy--;
					continue;
				}
				// skip a space if there is one
				if (*_file_buffer == ' ') _file_buffer++;
				if (*_file_buffer == '\n' || *_file_buffer == EOF) {
					//pf("end of line or file. break");
					break;
				}
				read_word(last_word, _file_buffer);
				//printf("%s ", last_word);
				sprintf(retort, " %s", last_word);
				retort += (strlenj(last_word)+1); // to include space
				//pf("file buffer before increment");
				//scan_dozen(_file_buffer);
				_file_buffer += strlenj(last_word); // brings just after end of word
				//pf("file buffer after increment");
				//scan_dozen(_file_buffer);
			}
			continue; // if we got here, we already incrememted
		}
		_file_buffer++;
	}
	sprintf(retort, "\n");
	if (loop_max <= 0) pf("ERROR: loop maxed out");
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

