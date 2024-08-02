#include <stdio.h>

void record_to_memory_if_new(char *line);

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
    }

    return 0;
}

void record_to_memory_if_new(char *line) {

    FILE *fp = fopen("memory.txt", "r");

    char *lineP = line;
    for (;*fp!=EOF;fp++) {
    }

    fclose(fp);

    FILE *fp2 = fopen("memory.txt", "a");

    fputs(line, fp2);

    fclose(fp2);
}
