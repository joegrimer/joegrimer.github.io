#include <stdio.h>

void record_to_memory_if_new(char *line);
const char *random_phrase_from_memory();

int main() {
    // Create a string
    char user_input[300];

    while (1) {
        // Ask the user to input some text
        printf(": ");

        // Get and save the text
        fgets(user_input, 100, stdin);

        if (*(user_input+1) == '\0') break;

        record_to_memory_if_new(user_input);

        // Output the text
        printf("> \n");
        user_input[0] = '\0';
        user_input[1] = '\0';

        const char *response = random_phrase_from_memory();
        printf("%s", response);
    }

    return 0;
}

const char *random_phrase_from_memory() {
    FILE *fp = fopen("memory.txt", "r");

    char file_char = '?';
    long int linecount=0;
    while (file_char != EOF) {
        file_char=getc(fp);
        if ( file_char=='\n' ) linecount++;
    }
    printf("lc %ld\n", linecount);
    fclose(fp);

    char * phrase= "bob";
    return phrase;
}

void record_to_memory_if_new(char *line) {

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

    fclose(fp);

    FILE *fp2 = fopen("memory.txt", "a");

    fputs(line, fp2);

    fclose(fp2);
}
