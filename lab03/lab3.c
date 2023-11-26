#include <stdio.h>

int main() {
    int arrA[] = {1, 7, 4, 3, 7};
    int arrB[] = {2, 4, 7, 7, 3};
    int sizeA = sizeof(arrA) / sizeof(arrA[0]);
    int sizeB = sizeof(arrB) / sizeof(arrB[0]);
    int maxSize;

    if (sizeA > sizeB) {
        maxSize = sizeA;
    } else {
        maxSize = sizeB;
    }

    int arrC[maxSize];

    int indexC = 0;
    for (int i = 0; i < sizeA; i++) {
        for (int j = 0; j < sizeB; j++) {
            if (arrA[i] == arrB[j]) {
                arrC[indexC] = arrA[i];
                indexC++;
                break;
            }
        }
    }

    printf("C (A and B):\n");
    for (int i = 0; i < indexC; i++) {
        printf("%d ", arrC[i]);
    }
    printf("\n");

    return 0;
}
