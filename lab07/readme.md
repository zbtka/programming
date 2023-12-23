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
def to_str(input_list, is_outer=True,):
    if not input_list:
        return "None"
    elif isinstance(input_list, list):
        result = [to_str(item, False) for item in input_list]
        if is_outer:
            return ' -> '.join(result) + ' -> None' 
        else:
            return ' -> '.join(result)
    else:
        return str(input_list) if input_list is not "None" else 'None'


result = to_str([1, [2, [3, [4, [5]]]]])
result2 = to_str([])
result3 = to_str([1, [2]])


print(result)
print(result2)
print(result3)
      
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/90a297b2-3fc8-4874-acb6-e1613cee6b2b)





### Вариант кода без использования рекурсии.
```py
def to_str(lst):
    if not lst: 
        return "None" 

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
print(to_str([]))
print(to_str([1, [2]]))

```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/6ebd7db4-2c22-4b04-8f93-5df5c43b67b1)



* Функция для расчёта
$a_i = a_{i-2}+\frac{a_{i-1}}{2^{i-1}}. a_0=a_1=1$

### Вариант кода без использования рекурсии.
```py

def calculate_sequence(n):
    a = [1, 1]
    for i in range(2, n + 1):
        a_i = a[i - 2] + a[i - 1] / (2 ** (i - 1))
        a.append(a_i)
    return a[-1]  

result = calculate_sequence(5)
print(result)
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/4200d0d5-f618-49bf-b79a-4ca178219b20)




### Вариант кода c использованием рекурсии.
```py
def calculate_a_iterative(n):
    a = [1, 1]
    for i in range(2, n+1):
        a.append(a[i-2] + a[i-1] / (2**(i-1)))
    return a[n]
result_iterative = calculate_a_iterative(5)
print(result_iterative)
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/1b89d765-07d0-4388-a9aa-4a7b7f3fd71f)



## Используемые источники
* https://www.youtube.com/watch?v=IJDJ0kBx2LM
* https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23
* https://habr.com/ru/articles/337030/
