#include <stdio.h>

// Read at most `n` characters (newline included) into `str`.
// If present, the newline is removed (replaced by the null terminator).
void s_gets(char* str, int n)
{
    char* str_read = fgets(str, n, stdin);
    if (!str_read)
        return;

    int i = 0;
    while (str[i] != '\n' && str[i] != '\0')
        i++;

    if (str[i] == '\n')
        str[i] = '\0';
}

int main()
{
    char my_string[100];
    s_gets(my_string, 100);
    char line1[100], line2[100], line3[100];
    char *p1 = line1, *p2 = line2, *p3=line3;


    for (char *a = my_string;*a!='\0';a++) {
        printf("%c ", a[0]);
        if (a[0] == 'a') {
            *p1++='('; *p1++='-'; *p1++=')';
            *p2++='I'; *p2++='-'; *p2++='I';
            *p3++='I'; *p3++=' '; *p3++='I';
        } else if (a[0] == 'b') {
            *p1++='I'; *p1++='D'; *p1++=' ';
            *p2++='I'; *p2++=' '; *p2++=' ';
            *p3++='I'; *p3++='D'; *p3++=' ';
        } else if (a[0] == 'c') {
            *p1++='I'; *p1++='-'; *p1++='-';
            *p2++='I'; *p2++=' '; *p2++=' ';
            *p3++='I'; *p3++='_'; *p3++='_';
        } else if (a[0] == 'd') {
            *p1++='I'; *p1++='-'; *p1++=' ';
            *p2++='I'; *p2++=' '; *p2++=')';
            *p3++='I'; *p3++='-'; *p3++=' ';
        } else if (a[0] == 'e') {
            *p1++='I'; *p1++='-'; *p1++='-';
            *p2++='I'; *p2++='-'; *p2++=' ';
            *p3++='I'; *p3++='-'; *p3++='-';
        } else if (a[0] == 'h') {
            *p1++='I'; *p1++=' '; *p1++='I';
            *p2++='I'; *p2++='-'; *p2++='I';
            *p3++='I'; *p3++=' '; *p3++='I';
        } else if (a[0] == 'l') {
            *p1++='I'; *p1++=' '; *p1++=' ';
            *p2++='I'; *p2++=' '; *p2++=' ';
            *p3++='I'; *p3++='_'; *p3++='_';
        } else if (a[0] == 'o') {
            *p1++=' '; *p1++='-'; *p1++=' ';
            *p2++='I'; *p2++=' '; *p2++='I';
            *p3++=' '; *p3++='-'; *p3++=' ';
        } else if (a[0] == 'w') {
            *p1++='|'; *p1++=' '; *p1++='|';
            *p2++='|'; *p2++='|'; *p2++='|';
            *p3++=' '; *p3++='W'; *p3++=' ';
        } else if (a[0] == 'r') {
            *p1++='|'; *p1++='-'; *p1++=')';
            *p2++='|'; *p2++='/'; *p2++=')';
            *p3++='|'; *p3++=' '; *p3++='\\';
        } else if (a[0] == 'l') {
            *p1++=' '; *p1++=' '; *p1++=' ';
            *p2++=' '; *p2++=' '; *p2++=' ';
            *p3++=' '; *p3++=' '; *p3++=' ';
        } else if (a[0] == 'l') {
            *p1++=' '; *p1++=' '; *p1++=' ';
            *p2++=' '; *p2++=' '; *p2++=' ';
            *p3++=' '; *p3++=' '; *p3++=' ';
        } else {
            *p1++=' '; *p1++=' '; *p1++=' ';
            *p2++=' '; *p2++=' '; *p2++=' ';
            *p3++=' '; *p3++=' '; *p3++=' ';
        }
        *p1++=' ';
        *p2++=' ';
        *p3++=' ';
    }
    printf("my_string = %s\n", my_string);
    printf("---\n");
    *p1='\0';
    *p2='\0';
    *p3='\0';
    printf("%s\n", line1);
    printf("%s\n", line2);
    printf("%s\n", line3);
}
