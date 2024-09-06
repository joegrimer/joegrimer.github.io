#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void record_to_memory(char *line);
void random_phrase_from_memory(char *_retort);
void generate_markov_word_phrase(char *_retort);

void pf(char *_s) {printf("%s\n",_s); }
int main() {

	char retort[100];
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

		if (*(user_input+1) == '\0') break;

		record_to_memory(user_input);

		// Output the text
		// printf("> \n");
		user_input[0] = '\0';
		user_input[1] = '\0';

		random_phrase_from_memory(retort);
		record_to_memory(retort);
		printf("£ %s\n", retort);
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
	char *_word_buf = word_buf;
	while( *text_ptr != ' ' && *text_ptr!='\0') {
		*_word_buf = *text_ptr;
		text_ptr++;
		_word_buf++;
	}
	*_word_buf = '\0';
}

void generate_markov_word_phrase(char *retort) {
	char file_char = '?';
	char file_buffer[99999];
	char *_file_buffer = file_buffer;
	char last_word[50];
	char this_word[50];
	char new_word[50];
	char *_last_word = last_word;
	char *_this_word = this_word;
	char *_new_word;
	char *_retort = retort;

	/* process:
	- get random line first word
	- find folllowups to that first word - including dollar
	- pick one
	- follow
	- finish eventually
	*/
	long line_count = get_line_count(); // could make this use buffer and be faster

	FILE *fp = fopen("memory.txt", "r");
	while (1) {
		*_file_buffer = getc(fp);
		if (*_file_buffer == EOF) break;
		_file_buffer++;
	}
	fclose(fp);

	// reset pointer
	_file_buffer = file_buffer;

	long choice = semi_rand(line_count);
	do {
		if (choice == 0) {
			read_word(_retort, _file_buffer);
			break;
		} else if ( *_file_buffer=='\n' ) {
			choice--;
		}
		_file_buffer++;
	} while (*_file_buffer != EOF);
	printf("First word: %s\n", retort);

	// reset pointer
	_file_buffer = file_buffer;

	printf("Up to here\n");
	do {
		_new_word = new_word;
	    if (*_file_buffer != ' ' && *_file_buffer != '\n') {
			pf("About to read word");
			read_word(_new_word, _file_buffer);
			_file_buffer += strlen(_new_word);
			printf("words: %s %s", new_word, retort);
			if(strcmp(new_word, retort) == 0) {
				pf("The same, they are");
				break;
			}
		}
		_file_buffer++;
	} while (*_file_buffer != EOF);
	printf("Next word: %s\n", retort);
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
				*_retort = '\0';
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
