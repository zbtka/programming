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
def to_str(input_list, is_outer=True):
    if isinstance(input_list, list):
        result = [to_str(item, False) for item in input_list]
        if is_outer:
            return ' -> '.join(result) + ' -> None'
        else:
            return ' -> '.join(result)
    else:
        return str(input_list) if input_list is not None else 'None'
result = to_str([1, [2, [3, [4, [5]]]]])
print(result)
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/fd12cf4c-d0ab-4ff3-a3f2-22efbfbf8d85)



### Вариант кода без использования рекурсии.
```py
def to_str(lst):
    result = []
    stack = [lst]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            if current:
                stack.extend(reversed(current[1:]))
                stack.append(current[0])
            else:
                result.append("None")  
        else:
            result.append(str(current))
    result.append("None") 
    return " -> ".join(result)
nested_list = [1, [2, [3, [4, [5]]]]]
print(to_str(nested_list))

```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/6ebd7db4-2c22-4b04-8f93-5df5c43b67b1)



* Функция для расчёта
$a_i = a_{i-2}+\frac{a_{i-1}}{2^{i-1}}. a_0=a_1=1$

### Вариант кода без использования рекурсии.
```py
def calculate_a_iterative(i, a):
    if i < 2:
        return 1
    a_values = [1, 1] 
    for n in range(2, i+1):
        a_n = a_values[n-2] + (a_values[n-1] / (a ** (a-1)))
        a_values.append(a_n)
    return a_values[i]
i_value = 5
a_value = 2
result = calculate_a_iterative(i_value, a_value)
print(f"i={i_value} и a={a_value} = {result}")

```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/f58bfe2f-733a-4129-bb76-1910209f7f73)



### Вариант кода c использованием рекурсии.
```py
def calculate_a(i, a):
    if i < 2:
        return 1
    else:
        return calculate_a(i-2, a) + (calculate_a(i-1, a) / (a ** (a-1)))

i_value = 5
a_value = 2
result = calculate_a(i_value, a_value)
print(f"i={i_value} и a={a_value} = {result}")
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/6b8db666-f14a-4805-833b-3c59eba3bb28)



## Используемые источники
* https://www.youtube.com/watch?v=IJDJ0kBx2LM
* https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23
* https://habr.com/ru/articles/337030/
