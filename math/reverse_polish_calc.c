#include <stdio.h>
//#include <stlib.h>
# include <math.h>

main() {
	printf("Welcome to my reverse Polish Calculator\n");
	char input_string[] = "4 5 + 8 4 + 4 5 6 * / + *";
	printf("Our input string is '%s'\n\n",input_string);
	printf("Calculating...\n\n");

//	short input_string_len = strlen(input_string);
	short i, bp, sp, j;
	short big_stack[10];
	short small_stack[10];

	// intiialise the stacks
	for(i=0;i<10;i++) big_stack[i]=0;
	for(i=0;i<10;i++) small_stack[i]=0;
	bp = sp = 0; // index's

	// main logic
	for(i=0;i<100;i++) {
		char this_char= input_string[i];
		if(this_char=='\0') {
			printf("end of string\n");
			break;
		} else if(this_char==' ') {
			if(sp>0) {
				short new_number = 0;
				for(j=0;j<sp;j++) {
					new_number += small_stack[j]*pow(10,sp-j-1);
					small_stack[j]=0; // reset val - possibly unneccessary
				}
				big_stack[bp++] = new_number;

				// reset small stack
				sp = 0;
			}
		} else if ('0' <= this_char && this_char <= '9') {
			small_stack[sp++] = this_char - '0';
		} else if (this_char == '+') {
			big_stack[bp-2] += big_stack[bp-1];
			big_stack[bp-1]=0; // possibly unnccessary
			bp--;
		} else if (this_char == '-') {
			big_stack[bp-2]-= big_stack[bp-1];
			big_stack[bp-1]=0; // possibly unnccessary
			bp--;
		} else if (this_char == '*') {
			big_stack[bp-2] *= big_stack[bp-1];
			big_stack[bp-1]=0; // possibly unnccessary
			bp--;
		} else if (this_char == '/') {
			big_stack[bp-2] /= big_stack[bp-1];
			big_stack[bp-1]=0; // possibly unnccessary
			bp--;
		}	else printf("I don't recognise '%c'\n",this_char);
	}
	printf("\nbig stack: ");
	for(i=0;i<bp;i++) printf("%d,",big_stack[i]);

	printf("\nsmall stack: ");
	for(i=0;i<sp;i++) printf("%d,",small_stack[i]);

	printf("\n\nEnd of program.\n");
}
