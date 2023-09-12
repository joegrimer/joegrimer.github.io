#include <stdio.h>

#include <time.h>
#include <stdlib.h>

#define NO_OF_LAYERS 3
#define NEURONS_PER_LAYER 10

struct neuron
{
    int power;
    struct neuron *next;
};

int main()
{

    srand(time(NULL)); // Initialization, should only be called once.
                       //     int random_no = rand();      // Returns a pseudo-random integer between 0 and RANDMAX
                       //     printf("random number %d\n", random_no);

    struct neuron brain[NO_OF_LAYERS][NEURONS_PER_LAYER];

    for (int i = 0; i < NO_OF_LAYERS; i++)
    {
        for (int j = 0; j < NEURONS_PER_LAYER; j++)
        {
            brain[i][j].power = rand() % 200;

            printf("%d, ", brain[i][j].power);

            if (i + 1 == NO_OF_LAYERS)
                brain[i][j].next = 0; // dodgy?
            else
                brain[i][j].next = &brain[i + 1][rand() % NEURONS_PER_LAYER];
        }
        printf("\n");
    }
    //     printf("the next of neuron %d has the power %d\n", 0, brain[0][0].next->power);

    int random_input[NEURONS_PER_LAYER];
    for (int i = 0; i < NEURONS_PER_LAYER; i++)
        random_input[i] = rand() % 200;

    printf("\nRandom input is: ");
    for (int i = 0; i < NEURONS_PER_LAYER; i++)
        printf("%d, ", random_input[i]);

    int output[NEURONS_PER_LAYER];
    for (int i = 0; i < NEURONS_PER_LAYER; i++)
    {
        output[i] = random_input[i];
        printf("Path of neuron starts at %d\n", output[i]);
        struct neuron *first_neuron = &brain[0][i];
        for (int j = 0; j < NO_OF_LAYERS; j++)
        {
            printf("Now encounters %d\n", first_neuron->power);
            output[i] = (output[i] * first_neuron->power);
            printf("So is %d\n", output[i]);
            first_neuron = first_neuron->next;
        }
        break;
    }

    printf("\nOutput is: ");
    for (int i = 0; i < NEURONS_PER_LAYER; i++)
        printf("%d, ", output[i]);

    puts("\nend of program");
}
