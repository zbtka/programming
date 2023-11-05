# Лабораторная работа №2
## Задания для самостоятельного выполнения
### Сложность:     Rare
    1. Напишите программу по варианту, используя оператор цикла while (нечётные варианты) или do while (чётные варианты).
    2. Напишите программу, используя оператор цикла for.
    3. Постройте график с использованием gnuplot.
    4. Составьте блок-схемы.
    5. Оформите отчёт в README.md. Отчёт должен содержать:
        5.1 Задание
        5.2 Описание проделанной работы
        5.3 Скриншоты результатов
        5.4 Блок-схемы
        5.5 График функции
        5.6 Ссылки на используемые материалы

## Этапы работы
 ## Вариант - 4
![image](https://github.com/zbtka/programming/assets/144006033/23b13133-2f28-4dcb-8b7d-1fd2f7efd386)
 ### 1. Напишите программу по варианту, используя оператор цикла while (нечётные варианты) или do while (чётные варианты).
 ```c
#include <stdio.h>
#include <math.h>

int main() {
    double x = 0.0, y;
    double eps;
    double h;
    scanf("%lf", &h);
    eps = h / 2.0;
    printf("x\t\ty\n");

    do {
        if (x >= 0.0 && x <= 1.0 + eps) {
            y = sqrt(x + 1) - sqrt(x) - 0.5;
        } else if (x > 1.0 + eps && x <= 2.0 + eps) {
            y = exp(-x - 1 / x);
        } else {
            y = 0.0;
        }

        printf("%f\t%f\n", x, y);
        x = x + h;
    } while (x >= 0.0 && x <= 2.0 + eps);

    return 0;
}
 ```
 ### 2. Напишите программу, используя оператор цикла for.
```c
#include <stdio.h>
#include <math.h>

int main() {
    double x, y;
    double eps;
    double h;
    scanf("%lf", &h);
    eps = h / 2.0;

    printf("x\t\t\ty\n");

    for (x = 0.0; x <= 2.0 + eps; x += h) {
        if (x >= 0.0 && x <= 1.0 + eps) {
            y = sqrt(x + 1) - sqrt(x) - 0.5;
        } else if (x > 1.0 + eps && x <= 2.0 + eps) {
            y = exp(-x - 1 / x);
        } else {
            y = 0.0;
        }

        printf("%.6f\t%.6f\n", x, y);
    }

    return 0;
}
 ```
### Результат программы
![image](https://github.com/zbtka/programming/assets/144006033/372b4656-2b20-4932-b87f-2b53fdb95ced)
### 3. Постройте график с использованием gnuplot.
![image](https://github.com/zbtka/programming/assets/144006033/2746fc74-ab23-4e76-a97d-2d45ff5ecc34)

### 4. Составьте блок-схемы.
![image](https://github.com/zbtka/programming/assets/144006033/21e54a74-250a-4c88-ad69-01b254b59a19)
#### Блок схемы для двух программ идентичны.
### Список использованных источников.
1. https://habr.com/ru/companies/ruvds/articles/517450/
2. https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
3. https://en.wikibooks.org/wiki/LaTeX/Mathematics
4. https://programforyou.ru/block-diagram-redactor

