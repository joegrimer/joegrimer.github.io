#include <stdio.h>
#include <string.h>

#define uint unsigned int

/* TODO
 * find double quotes
 * ing
 * quite
 *
 *
 */

int main() {

    uint c;;
    char word[50];
    char * pword = word;
    uint line_no = 1, char_no = 0;

    while ((c=getchar()) != EOF) {
        if (c=='\n') line_no++, char_no = 0;
        if (c == ' ' || c == '.' || c == ',' || c == '\n') {
            *pword = '\0';
            if (strcmp(word, "very")==0 ||
                strcmp(word, "trying")==0 ||
                strcmp(word, "may")==0 ||
                strcmp(word, "might")==0 ||
                strcmp(word, "hoping")==0 ||
                strcmp(word, "probably")==0 ||
                strcmp(word, "fairly")==0) printf("'%s' on line %d char %d\n", word, line_no, char_no);
            // reset word
            pword = word;
        } else {
            *pword++ = c;
        }
        char_no++;
    }
    return 0;
}
