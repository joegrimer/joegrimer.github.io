#include <stdio.h>

typedef struct CELL *LIST;
struct CELL {
    int element;
    LIST next;
};

int main() {
    printf("sart\n");

    struct CELL item = {23, 0};
    struct CELL item2 = {9, &item};
    struct CELL item3 = {2, &item2};
    struct CELL item4 = {24, &item3};
    
    struct CELL ptr = item4;
    printf("init ptr element %d\n", ptr.element);
    while(ptr.next != 0) {
        printf("item val %d\n", ptr.element);
        ptr = *ptr.next;
    }

    printf("item 4 after all this is %d\n", item4.element);
    printf("esart\n");
}
