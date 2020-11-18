/*
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n=40, 40^2 + 40 + 41 = 40(40+1)+41 is divisible by 41, and certainly when n=41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int run_formula(int n, int a, int b) {
    // n^2 + an + b
    return pow(n, 2) + (a*n) + b;
}

int is_prime(int subject) {
    if(subject<0) return -1; // negative numbers can't be prime, apparently
    for(int p_factor = 2;p_factor<subject;p_factor++) {
        int quotient = subject/p_factor; // will remove remainder
        int product = quotient*p_factor;
        if (product==subject) // then it's a factor
            return p_factor; // not prime
        if (p_factor*p_factor >= subject) // eliminating innefficiency
            break;
    }
    return 1; // prime
}

int main() {
    printf("Start of Program.\n\n"); 
   
    int best_a=0, best_b=0, best_n=0;
    int a=-999, b=61;
    for (a=-999;a<=999;a++) { for (b=-1000;b<=1000;b++) {
    for (int n=0;1;n++) {
        int result = run_formula(n, a, b);
        //printf("%d^2 + %d*%d + %d = %d (prime? %d)\n", n, a, n, b, result, is_prime(result));
        if (is_prime(result)!=1) {

            //printf("max for a=%d and b=%d was %d\n", a, b, (n-1));
            if ((n-1)>best_n) {
                best_a=a;
                best_b=b;
                best_n=(n-1);
            }
            break;
        }
    }
    }}
    printf("best_a %d best_b %d best_n %d\n", best_a, best_b, best_n);
    printf("product of a and b is: %d\n",(best_a*best_b));


    printf("\nEnd of Program.\n"); 
}

