# Отчет 
## Задание
Сложность:
  Rare
    
    1. Напишите программу по своему варианту.
    2. Оформите отчёт в README.md. Отчёт должен содержать:
          2.1 Задание
          2.2 Описание проделанной работы
          2.3 Скриншоты результатов
          2.4 Ссылки на используемые материалы

## Этапы работы
### 1. Задание по Варианту №4
`
Максимально эффективно по используемой памяти сформировать массив из элементов, встречающихся в обоих массивах A и B.
`

### 2. Код
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int n, int a[]) {
    for (int i = 0; i < n; i++)
        a[i] = rand() % 11;
}

void findCommonElements(int n, int A[], int B[], int C[], int *sizeC) {
    *sizeC = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (A[i] == B[j]) {
                C[*sizeC] = A[i];
                (*sizeC)++;
                break;
            }
        }
    }
}

int main() {
    srand(time(NULL));
    int n;
    printf("size A and B: ");
    scanf("%d", &n);

    int A[n], B[n], C[n];
    
    printf("A:\n");
    fill(n, A);
    for (int i = 0; i < n; i++)
        printf("%5d", A[i]);
    printf("\n");

    printf("B:\n");
    fill(n, B);
    for (int i = 0; i < n; i++)
        printf("%5d", B[i]);
    printf("\n");

    int sizeC;
    findCommonElements(n, A, B, C, &sizeC);
    
    printf("C:\n");
    for (int i = 0; i < sizeC; i++) {
        printf("%5d", C[i]);
    }
    printf("\n");

    return 0;
}

```

## Результат работы программы:
![image](https://github.com/zbtka/programming/assets/144006033/ab05e778-c049-47c5-bb46-8ca093deca74)


## 4. Список использованных источников
* https://www.youtube.com/watch?v=GJFqT6Kz9NE
* https://www.youtube.com/watch?v=Zpml91CY8jY
* https://metanit.com/c/tutorial/2.13.php
