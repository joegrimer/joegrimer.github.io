#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>

#define RANDOM_NUMBERS 200000
#define GRAPH_SIZE 80
#define GRAPH_CUT_SIZE GRAPH_SIZE/3

int main() {

    printf("Start\n");

    srand(time(NULL));   // Initialization, should only be called once.
    int r;

    int graph[GRAPH_SIZE];
    for (int i = 0; i < GRAPH_SIZE; i++) graph[i] = 0;

    for (int i=0; i < RANDOM_NUMBERS; i++) {
        r = (rand() % GRAPH_CUT_SIZE) + (rand() % GRAPH_CUT_SIZE) + (rand() % GRAPH_CUT_SIZE);
        graph[r+1]++;
        // printf("random number %d\n", r);
    }
    for (int i=0; i < GRAPH_SIZE; i++) {
        int max = graph[i] / 100;
        for(int j=0;j< max;j++) printf("x");
        printf("\n");
    }

    printf("End\n");
    return 0;
}