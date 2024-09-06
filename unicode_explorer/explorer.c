#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void pf(char *_s) {printf("%s\n",_s); }
int main() {

	char manchar=0;
	for (int i=0;i<=258;i++) {
		printf("%c \n", manchar);
		manchar++;
	}

}
