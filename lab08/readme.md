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

    @limit_calls(3)
    def inner(*args):
        nonlocal unique_values
        unique_values.update(args)
        return list(unique_values)

    return inner

# пример
unique_values = unique_values_closure()
print(unique_values(1, 2, 3, 2, 4, 5, 3, 6))  # Результат: [1, 2, 3, 4, 5, 6]
print(unique_values(5, 6, 7, 8, 1, 2, 3, 4))  # Результат: [1, 2, 3, 4, 5, 6, 7, 8]
print(unique_values(9, 1, 2, 3, 4, 5, 6))
```

### Результат работы программы:
![image](https://github.com/zbtka/programming/assets/144006033/8691ac01-ea37-4944-a410-2065e8aa168d)
