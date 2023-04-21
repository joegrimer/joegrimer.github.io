#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void println(char *string) {
  printf(string,"\n");
}

int seed = 97;
int randin(int clock) {
  seed = seed + 97;
  int number = ((int)time(NULL)-seed)%clock;
  if (number>0) return number;
  else return -number;
}

char material_adjectives[][10] = {"metallic","fabric","plastic","wooden","paper","glass","stone","leather","fleshy","hairy"};
char thing_names[][10] = {"statue","tree","creature","book","desk","bed","shelf","skeleton","sphere","apple","chair","door"};

int main() {
  println("Begginning of the generator\n");
  printf("a ");
  printf("%s",material_adjectives[randin(10)]);
  printf(" ");
  printf("%s",thing_names[randin(10)]);
  printf(" stands before you\n");
}
