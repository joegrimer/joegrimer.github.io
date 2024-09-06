#include <stdio.h>
#include <stdio.h>
#include <wchar.h>
#include <locale.h>

void pf(char *_s) {printf("%s\n",_s); }
int main() {

	pf("Ascii");
	char manchar=0;
	for (int i=0;i<=258;i++) {
		printf("%c ", manchar);
		manchar++;
	}
	pf("\nUnicoder");

	printf("\xE2\x98\xA0 \xE2\x98\xA0 bob");
	pf("end");

}
