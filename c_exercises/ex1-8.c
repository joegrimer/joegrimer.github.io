#include <stdio.h>

/*count blanks, tabs and newlines - expects to be handed a file*/
main() {
	int c;

	while((c = getchar()) != EOF) {
		if (c=='\t'){
			putchar('\\');
			putchar('t');
		}else
			putchar(c);
	}
//	printf("%d\n",n1);
}
