<h2 style="text-align: center;">Бюджетное учреждение высшего образования Ханты-Мансийского автономного округа – Югры</h2>

<h1 style="text-align: center;">«СУРГУТСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»</h1>

<h2 style="text-align: center;">Политехнический институт</h2>

<p style="text-align: center;">Кафедра прикладной математики</p>

<p style="text-align: center;">Миронов Роман Алексеевич</p>

<h1 style="text-align: center;">Функции одной перемнной. Предел и непрерывность функции.</h1>

<p style="text-align: center;">Дисциплина «Математический анализ»</p>

<p style="text-align: center;">направление 01.03.02 «Прикладная математика и информатика»</p>

<p style="text-align: center;">направленность (профиль): «Технологии программирования и анализ данных»</p>

<pre>

</pre>

<p style="text-align: right;">Преподаватель: Ряховский Алексей Васильевич  </p>

<p style="text-align: right;">Доцент</p>

<p style="text-align: right;">Студент гр. № 601-31</p>

<p style="text-align: right;">Миронов Роман Алексеевич</p>

<pre>

</pre>

<p style="text-align: center;">Сургут 2023 г.</p>

<h3 style="text-align: center;">Лабораторная работа №2. Функции одной перемнной. Предел и непрерывность функции.</h3>
<h3 style="text-align: center;">Вариант №14</h3>

#### Задание

2.1. Аналитически найти область определения функций, а затем построить их
графики, используя графические пакеты Python. Для каждой из функций
график построить на отдельном рисунке.

2.2. Вычислить пределы данных функций двумя способами: аналитически и
используя библиотеки Python для символьных вычислений. Используя
графические пакеты Python, построить графики функций, иллюстрирующие
поведение функций в окрестностях тех точек, в которых вычисляется предел.
Если предел существует, построить на соответствующем рисунке точку,
изображающую предел данной функции.

2.3. Найти (аналитически и используя библиотеки Python для символьных
вычислений) точки разрыва функции и определить их тип. Используя
графические пакеты Python построить графики функций, иллюстрирующие
поведение функций в окрестностях точек разрыва.

#### Аналитическое решение 2.1.1

$f(x) = \frac{x^2}{x-1}$
Найдем область определения:

$x - 1 \neq 0$

$x \neq 1$

Область определения:

$D(f)=(- \infty;1)\cup(1; \infty)$


            -           1            +
         ---------------|----------------
                        

Ответ: $D(f)=(-\infty;1)\cup(1;\infty)$

#### Программное решение 2.1.1

```python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 / (x-1)

x = np.linspace(-10, 10, 400) 
y = f(x)

plt.plot(x, y, linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid(True)
plt.show()

```
#### Аналитическое решение 2.1.2

$g(x) = \arccos \frac{1}{x + 4}$

Обратный косинус определен для значений $x$ в диапазоне от -1 до 1, включая крайние значения.

Поэтому в данном случае область определения функции $g(x)$ будет состоять из всех значений $x$, таких, что $\frac{1}{x + 4}$ находится внутри диапазона [-1, 1].

Для нашей функции это значит, что $\frac{1}{x + 4}$ должно находиться внутри этого диапазона:

$-1 \leq \frac{1}{x + 4} \leq 1$

Решая неравенство $\frac{1}{x + 4} \geq -1$, получаем:

   
$\frac{1}{x + 4} \geq -1$

$x + 4 \leq -1$

$x \leq -5$

Решая неравенство $\frac{1}{x + 4} \leq 1$, получаем:
   
$\frac{1}{x + 4} \leq 1$

$x + 4 \geq 1$

$x \geq -3$

Область определения:

$D(g)= (-\infty, -5] \cup [-3, \infty)$.

           +     -5     -    -3      +
        ----------|-----------|----------
Ответ:$D(g)= (-\infty, -5] \cup [-3, \infty)$.

#### Программное решение 2.1.2

```python
import matplotlib.pyplot as plt
import numpy as np
from math import acos

def g(x):
    y = np.empty_like(x) 

    for i, val in enumerate(x):
        if val >= -4:
            y[i] = np.arccos(1 / (val + 4))
        else:
            y[i] = np.nan  

    return y

x = np.linspace(-5, 100, 1000)

y = g(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('График функции g(x) = arccos(1 / (x + 4))')
plt.grid(True)
plt.show()
```

#### Иллюстрация решения

![image](https://github.com/zbtka/programming/assets/144006033/31dd8d75-0c86-4451-a8a4-77c26b996144)

<p style="text-align: center;">Рис. 2.1.1. Иллюстрация решения задачи.</p>

![image](https://github.com/zbtka/programming/assets/144006033/65571833-c90f-49e7-9c8e-4ab9c6c52158)

<p style="text-align: center;">Рис. 2.1.2. Иллюстрация решения задачи.</p>

#### Аналитическое решение 2.2

$\lim\limits_{x\rightarrow3}\frac{x^2 - 9}{x\cdot\sin\pi x} = \frac{3^2 - 9}{3\cdot\sin 3 \pi} = [\frac{0}{0}]$

$\lim\limits_{x\rightarrow3}\frac{(x^2-9)'}{(x\sin\pi x)'}=\lim\limits_{x\rightarrow3}\frac{2x}{(x)'\cdot\sin\pi x+x\cdot(\sin\pi x)'} = \lim\limits_{x\rightarrow3}\frac{2x}{\sin\pi x + x \cdot\cos\pi x \cdot\pi}$
                        
$\lim\limits_{x\rightarrow3}\frac{2\cdot 3}{\sin3\pi + 3\cos3\pi\cdot\pi} = \frac{6}{-3\pi} = -\frac{2}{\pi}$

```python
import matplotlib.pyplot as plt
import numpy as np
import sympy as smp

x = smp.symbols('x')

def f(x):
    return (x**2 - 9) / (x * smp.sin(smp.pi * x))

def plot_points():
    x_values = np.linspace(2.9, 3.1, 1000)
    y_values = [f(n) for n in x_values]

    plt.plot(x_values, y_values, label='f(x)')
    
    lim = smp.limit(f(x), x, 3)
    
    plt.plot(3, lim, 'o', color='orange', label='Limit')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.legend()
    plt.grid()
    plt.show()

plot_points()

f = (x**2 - 9) / (x * smp.sin(smp.pi * x))

lim = smp.limit(f, x, 3)
print(f'Предел: {lim}')
```

#### Иллюстрация решения

![image](https://github.com/zbtka/programming/assets/144006033/7bad2972-5c51-42a1-880d-99b57d300b7a)

<p style="text-align: center;">Рис. 2.2. Иллюстрация решения задачи.</p>

![image](https://github.com/zbtka/programming/assets/144006033/a59d58be-834a-4654-8199-5d128ed973cb)

<p style="text-align: center;">Рис. 2.2. Вывод программы в терминале.</p>

#### Аналитическое решение 2.3

$$f(n) =
  \begin{cases}
   3^x + 1,    &\quad \text{ если } x < 0\\
   2^x - 1,    &\quad \text{ если } x \geq 0
   \end{cases}
   \$$

Давайте исследуем точку $x_0=0$

Найдем предел справа и слева:

$\lim\limits_{x\rightarrow{x_0-0}}3^x + 1 = 3^0 + 1 = 1 + 1 = 2$

$\lim\limits_{x\rightarrow{x_0+0}}2^x - 1 = 2^0 - 1 = 0$

Пределы существуют и равны разным значениям, поэтому точка x=0 - это точка разрыва второго рода.

$f(0) = 0$

#### Программное решение 2.3
```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')

f1 = 3**x + 1
f2 = 2**x - 1

lim_left = sp.limit(f1, x, 0, dir='-')

lim_right = sp.limit(f2, x, 0, dir='+')

print(f"Точка разрыва в x = 0")
print(f"Левосторонний предел: y = {lim_left}")
print(f"Правосторонний предел: y = {lim_right}")
print("")

if lim_left == lim_right:
    type_of_discontinuity = "Первого рода"
else:
    type_of_discontinuity = "Второго рода"

print(f"Тип разрыва: {type_of_discontinuity}")
print("")

x_vals = np.linspace(-1, 1, 1000)
f1_vals = [sp.N(f1.subs(x, val)) for val in x_vals]
f2_vals = [sp.N(f2.subs(x, val)) for val in x_vals]

plt.plot(x_vals, f1_vals, label='f(x) = 3^x + 1, x < 0')
plt.plot(x_vals, f2_vals, label='f(x) = 2^x - 1, x >= 0')
plt.axvline(x=0, color='red', linestyle='--', label='Точка разрыва: x = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графики функций')
plt.legend()
plt.grid()
plt.show()
```

#### Иллюстрация решения

![image](https://github.com/zbtka/programming/assets/144006033/6b51f874-eca2-47af-9db2-fb350a8a60e9)


<p style="text-align: center;">Рис. 2.3. Иллюстрация решения задачи.</p>

![image](https://github.com/zbtka/programming/assets/144006033/cc28d40c-2502-418a-be48-96a316f7137c)

<p style="text-align: center;">Рис. 2.3. Вывод программы в терминале.</p>












