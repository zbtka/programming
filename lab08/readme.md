# Лабораторная работа №8
## Задание 

1. Решите обе задачи своего варианта.
2. Примените декоратор к замыканию.
3. Оформите отчёт в README.md. Отчёт должен содержать:
- Условия задач
- Описание проделанной работы
- Скриншоты результатов
- Ссылки на используемые материалы


### Вариант 4
* Замыкание, отбирающее только уникальные значения из переданных.
* Декоратор, который будет ограничивать количество вызовов функций.

### Вариант кода замыкания:
```py
def unique_values_closure():
    unique_values = set()

    def inner(*args):
        nonlocal unique_values
        unique_values.update(args)
        return list(unique_values)

    return inner
#пример
unique_values = unique_values_closure()
print(unique_values(1, 2, 3, 2, 4, 5, 3, 6))
print(unique_values(5, 6, 7, 8, 1, 2, 3, 4))
```
### Результат работы программы:

![image](https://github.com/zbtka/programming/assets/144006033/1ec62143-2802-483a-b985-ce079114f954)

### Вариант кода декоратора:
```py
import functools

def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                return "Максимальное количество вызовов превышено"
        return wrapper
    return decorator

@limit_calls(3)
def limited_function():
    print("Функция была вызвана")
#пример
limited_function()  
limited_function()  
limited_function() 
limited_function()  
```
### Результат работы программы:

![image](https://github.com/zbtka/programming/assets/144006033/57ca1184-f4d2-4107-be8d-c395507e8b7d)

### Декоратор к замыканию 
```py
import functools

def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                return "Максимальное количество вызовов превышено!"
        return wrapper
    return decorator

def unique_values_closure():
    unique_values = set()

    @limit_calls(2)
    def inner(*args):
        nonlocal unique_values
        unique_values.update(args)
        return list(unique_values)

    return inner

# пример использования
unique_values = unique_values_closure()
print(unique_values(1, 2, 3, 2, 4, 5, 3, 6))
print(unique_values(5, 6, 7, 8, 1, 2, 3, 4))
print(unique_values(9, 1, 2, 3, 4, 5, 6))
``` 
### Результат работы программы:

![image](https://github.com/zbtka/programming/assets/144006033/9d1a2761-83ce-4296-91c6-6c62697b8998)
