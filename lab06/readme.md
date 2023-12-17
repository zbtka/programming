# Лабораторная работа №6
## Задание 

1.   Напишите программу для решения задач своего варианта.
2.   Оформите отчёт в README.md. Отчёт должен содержать:
- Условия задач
- Описание проделанной работы
- Скриншоты результатов
- Ссылки на используемые материалы

## Условия задач:

Настя составляет 6-буквенные коды из букв Н, А, С, Т, Я. Каждая допустимая гласная буква может входить в код не более одного раза. Сколько кодов может составить Настя?
```py
import itertools

alp = "НАСТЯ"
ar = itertools.product(alp, repeat=6)
arl = []
for i in ar:
    arl.append(''.join(i))

count = 0
for e in arl:
    if e.count('А') > 1 or e.count('Я') > 1:
        continue
    if e.startswith('А') or e.startswith('Я'):
        continue
    if e.endswith('А') or e.endswith('Я'):
        continue
    flag = True
    for i in range(len(e) - 1):
        if (e[i] == 'А' and e[i + 1] == 'Я') or (e[i + 1] == 'А' and e[i] == 'Я'):
            flag = False
            break
    if flag:
        count += 1

print(count)
```
### Скриншот результата:
![image](https://github.com/zbtka/programming/assets/144006033/3c7e1dde-1df8-439c-a176-e7bc046c99bc)


- Значение арифметического выражения $16^{18}+4^{10}-46−16$ записали в системе счисления с основанием 4. Сколько цифр 3 содержится в этой записи?

```py
n = 16**18 + 4**10 - 46 - 16
s = ""  

while n > 0:
    d = n % 4
    s = str(d) + s
    n = n // 4

print(s.count('3'))
```
### Скриншот результата:
![image](https://github.com/zbtka/programming/assets/144006033/8b567664-7358-4d95-a53c-dcdafd6f604c)


- Пусть M  — сумма минимального и максимального натуральных делителей целого числа, не считая единицы и самого числа. Если таких делителей у числа нет, то считаем значение M равным нулю. Найдите целые числа, большие 452 021, в порядке возрастания, такие, для которых значение M при делении на 7 даёт в остатке 3. Вывести первые 5 найденных чисел и соответствующие им значения M.

```py
def get_znam(n):
    znam = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            znam.append(i)
            if i != n // i: 
                znam.append(n // i)
    return znam
count = 0
number = 452022
while count < 5:
    znam = get_znam(number)
    m = sum(znam) if znam else 0
    if m % 7 == 3:
        print(f"Число: {number}, M: {m}")
        count += 1
    number += 1   
```
### Скриншот результата:
![image](https://github.com/zbtka/programming/assets/144006033/63d7b2b5-e962-4da0-b92f-cf90584fef69)


### Ссылки на используемые материалы:
https://evil-teacher.on.fleek.co/prog_pm/lab06/

https://habr.com/ru/companies/otus/articles/529356/
