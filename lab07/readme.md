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
def to_str(input_list):
    if not input_list:  
        return 'None'

    if isinstance(input_list[0], list):  
        return to_str(input_list[0]) + ' -> ' + to_str(input_list[1:])   
    else:
        if len(input_list) == 1:  
            return str(input_list[0]) + ' -> None'  
        else:
            return str(input_list[0]) + ' -> ' + to_str(input_list[1:]) 
nested_list = [1, [2, [3, [4, [5]]]]]
result_str = to_str(nested_list)
print(result_str)
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/4e419ea7-a18a-40cc-9806-160555591241)


### Вариант кода без использования рекурсии.
```py
def to_str(input_list):
    result = " "
    for item in input_list:
        if isinstance(item, list):
            result += to_str(item) + ' -> '
        else:
            result += str(item) + ' -> '
    result += 'None'
    return result

nested_list = [1, [2, [3, [4, [5]]]]]
result_str = to_str(nested_list)
print(result_str)

```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/d7db4d0a-277a-481a-988c-6d89421fdfea)


* Функция для расчёта
$a_i = a_{i-2}+\frac{a_{i-1}}{a^{a-1}}. a_0=a_1=1$

### Вариант кода без использования рекурсии.
```py
def calculate_recursive(expression):
    if isinstance(expression, list):
        operand1 = calculate_recursive(expression[1])
        operand2 = calculate_recursive(expression[2])
        operator = expression[0]
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
    else:
        return expression

# пример
expr = ['+', 5, ['*', 3, 2]]  # результат: 11
result = calculate_recursive(expr)
print(result)

```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/0a3cb15f-81dd-423f-973f-a1debc8971e8)


### Вариант кода c использованием рекурсии.
```py
def calculate_recursive(expression):
    if isinstance(expression, list):
        operand1 = calculate_recursive(expression[1])
        operand2 = calculate_recursive(expression[2])
        operator = expression[0]
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
    else:
        return expression

# пример
expr = ['+', 5, ['*', 3, 2]]  # результат: 11
result = calculate_recursive(expr)
print(result)
```
### Результат работы программы
![image](https://github.com/zbtka/programming/assets/144006033/dfe48246-be54-4811-93e0-1e539713a718)



## Используемые источники
* https://www.youtube.com/watch?v=IJDJ0kBx2LM
* https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23
* https://habr.com/ru/articles/337030/
