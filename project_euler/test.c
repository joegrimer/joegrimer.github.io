/* at top */
#include <stdlib.h>
#include <stdio.h>
#include <gmp.h>

int main() {
/* definition */
mpz_t *A;

/* initialization of A */
A = (mpz_t *) malloc(10000 * sizeof(mpz_t));
if (NULL == A) {
    printf("ERROR: Out of memory\n");
        return 1;
        }

        /* no longer need A */
        free(A);
        }
