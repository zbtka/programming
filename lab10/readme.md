# Лабораторная работа №10
## Задание 
###Сложность: Rare
### 1.Создайте пакет, содержащий 3 модуля на основе лабораторных работ №№ 7-9
### 2.Напишите запускающий модуль на основе Typer, который позволит выбирать и настраивать параметры запуска логики из пакета.
### 3.Оформите отчёт в README.md. Отчёт должен содержать:
* Условия задач
* Описание проделанной работы
* Скриншоты результатов
* Ссылки на используемые материалы

#### Создание пакета модулей
![image](https://github.com/zbtka/programming/assets/144006033/ac6fc796-ad3f-4fb7-8632-62c7db04b565)


##### Лабораторная работа №7
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

##### Лабораторная работа №8
```py

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

##### Лабораторная работа №9
```py
import itertools

def unique_combinations_generator(*iterables):
    for combination in itertools.product(*iterables):
        yield combination

sequence1 = [1, 2, 3]
sequence2 = ['a', 'b', 'c']
sequence3 = ['x', 'y']

combinations = unique_combinations_generator(sequence1, sequence2, sequence3)
for combo in combinations:
    print(combo)
```

#### 2.Напишите запускающий модуль на основе Typer, который позволит выбирать и настраивать параметры запуска логики из пакета.
```py
import typer

from moduls import 7, 8, 9

app = typer.Typer()


@app.command()
def ca_lc(operator: str, initial: int):
    print(f'operator: {operator}, initial: {initial}\n', calculator.make_calc(operator, initial))


@app.command()
def foo(n: int):
    print(f'n: {n}\n', function.calculate_xi(n))


@app.command()
def rand(min_val: int, max_val: int):
    print(f'min_value: {min_val}, max_value: {max_val}\n', random_num_gen.generate_random_number(min_val, max_val))


if __name__ == "__main__":
    app()
```




