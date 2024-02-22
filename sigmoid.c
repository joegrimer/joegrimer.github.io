#include <stdio.h>

int sigmoid(int a) {
 int res=a*a*a/100;
 res += 500;
 if (res < 1) return 1;
 else if (res > 999) return 999;
 else return res;
}

int main() {
 int examples[] = {-999,-200,-80,-20,-4,-3,-2,-1,0,4,6,40,56,122,567,1234};
 for (int i=0;i < 16; i++) {
  int val=examples[i];
  printf("%d -> %d\n", val, sigmoid(val));
 }
}
