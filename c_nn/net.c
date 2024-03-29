#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

#define NO_INPUTS 3
#define NO_LAYERS 3
#define NO_PERLAYER 3
#define PER_NEURON_NO 2
#define NO_OUTPUTS 2
#define NN_MAX 144

int inputs[NO_INPUTS] = {};
// each neuron has in weight, gate, and out weight
int neurons[NO_LAYERS][NO_PERLAYER][PER_NEURON_NO] = {};
int outputs[NO_OUTPUTS] = {};

void init_nn();
void print_nn();

int main() {

   srand(time(NULL));   // Initialization, should only be called once.
   int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.

   printf("rand max is %d\n", RAND_MAX);
   printf("rand is %d\n", r);
   init_nn();
   print_nn();
   printf("Fin\n");
}

void init_nn() {
   int i, j, k;
    for (i=0; i<NO_INPUTS;i++) {
       inputs[i] = 0;
    }
    for (i=0; i<NO_LAYERS;i++) {
    for (j=0; j<NO_PERLAYER;j++) {
        neurons[i][j][0] = rand() % NN_MAX;
        neurons[i][j][1] = rand() % NN_MAX;
    }
    }
    for (i=0; i<NO_OUTPUTS;i++) {
       outputs[i] = 0;
    }
}

void print_nn() {
   printf("\n---\n");
   int i, j, k;
    for (i=0; i<NO_INPUTS;i++) {
       printf("V%dV ", inputs[i]);
    }
    printf("\n");
    for (i=0; i<NO_LAYERS;i++) {
    for (j=0; j<NO_PERLAYER;j++) {
       printf("(%d>>%d) ",
             neurons[i][j][0],
             neurons[i][j][1]
             );
    }
    printf("\n");
    }
    for (i=0; i<NO_OUTPUTS;i++) {
       printf(">%d< ", outputs[i]);
    }
   printf("\n---\n\n");
}
