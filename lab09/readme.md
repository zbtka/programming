# Лабораторная работа №9
## Задание 
Сложность: Rare

* Решите задачу своего варианта.
* Оформите отчёт в README.md. Отчёт должен содержать:
* Условия задач
* Описание проделанной работы
* Скриншоты результатов
* Ссылки на используемые материалы


### Вариант 4
* Генератор, создающий все возможные уникальные комбинации элементов из нескольких последовательностей.

### Вариант кода:
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

### Результат работы программы:

![image](https://github.com/zbtka/programming/assets/144006033/254d59d3-ef7e-4a71-8241-a2e7def1dcfb)


