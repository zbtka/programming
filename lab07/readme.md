# Лабораторная работа №7
## Задание 

1. Напишите две функции для решения задач своего варианта - с использованием рекурсии и без.
2. Оформите отчёт в README.md. Отчёт должен содержать:
- Условия задач
- Описание проделанной работы
- Скриншоты результатов
- Ссылки на используемые материалы
## Вариант 4 
* Функция для преобразования вложенных списков в строку:
```py
>>> to_str([1, [2, [3, [4, [5]]]]])
'1 -> 2 -> 3 -> 4 -> 5 -> None'
```

### Вариант кода с использования рекурсии.
```py
def to_str_recursive(lst):
    if isinstance(lst, list):
        if len(lst) == 0:
            return "None"
        else:
            return str(lst[0]) + " -> " + to_str_recursive(lst[1:])
    else:
        return str(lst) + " -> None"

nested_list = [1, [2, [3, [4, [5]]]]]
string_recursive = to_str_recursive(nested_list)
print(string_recursive)
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/85e635b7-8e08-4180-ad61-8b4cdcf8660a)

* Функция для расчёта
$a_i = a_{i-2}+\frac{a_{i-1}}{a^{a-1}}. a_0=a_1=1$

### Вариант кода без использования рекурсии.
```py
def calculate_sequence(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    
    a_i_minus_2 = 1
    a_i_minus_1 = 1
    a_i = 0

    for i in range(2, n + 1):
        a_i = a_i_minus_2 + a_i_minus_1 / (a_i_minus_1 ** (a_i_minus_1 - 1))
        a_i_minus_2 = a_i_minus_1
        a_i_minus_1 = a_i
    
    return a_i

result = calculate_sequence(10)
print(result)
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/5d3df323-c4be-4fde-a01e-32793ec8aab8)


## Используемые источники
* https://www.youtube.com/watch?v=IJDJ0kBx2LM
* https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23
* https://habr.com/ru/articles/337030/
