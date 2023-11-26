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

```

## Результат работы программы:
![image](https://github.com/zbtka/programming/assets/144006033/0c88c0cd-0769-4144-962e-a5555e1ce85e)

## 4. Список использованных источников
* https://www.youtube.com/watch?v=GJFqT6Kz9NE
* https://www.youtube.com/watch?v=Zpml91CY8jY
* https://metanit.com/c/tutorial/2.13.php
