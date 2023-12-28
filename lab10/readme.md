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


#___________________________________________________________________________#

def calculate_a_iterative(n):
    a = [1, 1]
    for i in range(2, n+1):
        a.append(a[i-2] + a[i-1] / (2**(i-1)))
    return a[n]

```

##### Лабораторная работа №8
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
    @limit_calls(1)

    def inner(*args):
        nonlocal unique_values
        unique_values.update(args)
        return list(unique_values)

    return inner
```

##### Лабораторная работа №9
```py
import itertools

def generate_combinations(*args):
    for combination in itertools.product(*args):
                yield combination
```

#### 2.Напишите запускающий модуль на основе Typer, который позволит выбирать и настраивать параметры запуска логики из пакета.
```py
import typer

from moduls import dec_zam, gen, rec

app = typer.Typer()


@app.command()
def gen1(seq: str):
    args = eval(seq)
    print(gen.generate_combinations(*args))
for 

@app.command()
def rec(a: str):
    print(a)


if __name__ == "__main__":
    app()
```




