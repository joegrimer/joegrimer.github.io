#include <stdio.h>

int sigmoid(int a) {
 int res=a*a*a/100;
 res += 500;
 if (res < 1) return 1;
 else if (res > 999) return 999;
 else return res;
}

int main() {
 for (int i=-240;i < 240; i++) {
  printf("%d -> %d\n", i, sigmoid(i));
 }
}
