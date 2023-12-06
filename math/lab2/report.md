<h2 style="text-align: center;">Бюджетное учреждение высшего образования Ханты-Мансийского автономного округа – Югры</h2>

<h1 style="text-align: center;">«СУРГУТСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»</h1>

<h2 style="text-align: center;">Политехнический институт</h2>

<p style="text-align: center;">Кафедра прикладной математики</p>

<p style="text-align: center;">Гркикян Мисак Эдикович</p>

<h1 style="text-align: center;">Функции одной перемнной. Предел и непрерывность функции.</h1>

<p style="text-align: center;">Дисциплина «Математический анализ»</p>

<p style="text-align: center;">направление 01.03.02 «Прикладная математика и информатика»</p>

<p style="text-align: center;">направленность (профиль): «Технологии программирования и анализ данных»</p>

<pre>

</pre>

<p style="text-align: right;">Преподаватель: Ряховский Алексей Васильевич  </p>

<p style="text-align: right;">Доцент</p>

<p style="text-align: right;">Студент гр. № 601-31</p>

<p style="text-align: right;">Гркикян Мисак Эдикович</p>

<pre>

</pre>

<p style="text-align: center;">Сургут 2023 г.</p>

<h3 style="text-align: center;">Лабораторная работа №2. Функции одной перемнной. Предел и непрерывность функции.</h3>
<h3 style="text-align: center;">Вариант №7</h3>

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

$f(x) = \sqrt{5 + 4x - x^2}$

Найдем область определения:

$5 + 4x - x^2 \geq 0$

$x^2 - 4x - 5 \leq 0$

$D = b^2 - 4ac = 16 + 20 = 36 = 6^2$

$x_{1, 2} = \frac{-b \pm \sqrt{D}}{2a} = \frac{4 \pm 6}{2} = -1 ; 5$

$(x + 1) * (x - 5) \leq 0$ 

Область определения:

$D(f)=[-1; 5]$



           +     -1     -     5      +
        ----------|-----------|----------
                        

ОТВЕТ: $D(f)=[-1; 5]$

#### Программное решение 2.1.1

```python
import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import *

# Определение функции
def f(x):
    return sqrt(5 + 4 * x - x ** 2)

# Создание массива значений x
x = np.linspace(-1, 5, 200)

# Вычисление значений y для каждого значения x
y = []
for i in x:
    y.append(f(i))

# Построение графика
plt.plot(x, y, linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid()
plt.show()
```

#### Аналитическое решение 2.1.2

$g(x) = lnsinx$

Найдем область определения:

$sinx > 0$

Следовательно: 

$D(g)=[2 \pi n;\pi + 2 \pi n]$ , $n \in Z$

ОТВЕТ: $D(g)=[2 \pi n;\pi + 2 \pi n]$ , $n \in Z$

#### Программное решение 2.1.2

```python
import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *

# Определение функции
def f(x):
    return np.log(np.sin(x))

# Создание массива значений x
x = np.linspace(0, np.pi, 300)

# Вычисление значений y для каждого значения x
y = f(x)

# Построение графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid()
plt.show()
```

#### Иллюстрация решения

![Image text](график2.1.png)

<p style="text-align: center;">Рис. 2.1.1. Иллюстрация решения задачи.</p>

![Image text](график2.2.png)

<p style="text-align: center;">Рис. 2.1.2. Иллюстрация решения задачи.</p>

#### Аналитическое решение 2.2

Вычислим предел данной функции:

$\lim\limits_{x\rightarrow0}{(1 + 7x)^{3ctgx}}$ 

Второй замечательный предел выглядит так:

$\lim\limits_{u\rightarrow0}{(1 + u)^{\frac{1}{u}}} = e$

Вычисляем:

$\lim\limits_{x\rightarrow0}{[(1 + 7x)^{\frac{1}{7x}}]^{21*x*ctgx}}$

$e^{\lim\limits_{x\rightarrow0}{(21*x*ctgx)}}$ 

$\lim\limits_{x\rightarrow0}{(21*x*ctgx)} = \lim\limits_{x\rightarrow0}{(21*x*\frac{cosx}{sinx})}$

По первому замечательному пределу:

$\lim\limits_{x\rightarrow0}{\frac{x}{sinx}} = 1$

Далее:

$\lim\limits_{x\rightarrow0}{21*cosx} = 21$

Отсюда следует:

$\lim\limits_{x\rightarrow0}{(1 + 7x)^{3ctgx}} = e^{21}$ 

ОТВЕТ: $e^{21}$

#### Программное решение 2.2

```python
import matplotlib.pyplot as plt
import numpy as np
import sympy as smp

x = smp.symbols('x')

# Объявляем функцию
def f(x):
    return (1 + 7 * x) ** (3 * smp.cot(x))

def plot_points():
    x_values = np.linspace(-0.1, 0.1, 300)  
    y_values = [f(n) for n in x_values]

    # Строим график
    plt.plot(x_values, y_values, label='f(x)')
    
    # Вычисление предела
    lim = smp.limit(f(x), x, 0)
    
    # Изображаем предел точкой
    plt.plot(0, lim, 'o', color='orange', label='Limit')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.legend()
    plt.grid()
    plt.show()

plot_points()


# Определение функции
f = (1 + 7 * x) ** (3 * smp.cot(x))

# Вычисление предела
lim = smp.limit(f, x, 0)
print(f'Limit: {lim}')
```

#### Иллюстрация решения

![Image text](график2.3.png)

<p style="text-align: center;">Рис. 2.2. Иллюстрация решения задачи.</p>

![Image text](вывод2.3.png)

<p style="text-align: center;">Рис. 2.2. Вывод программы в терминале.</p>

#### Аналитическое решение 2.3

$f(x) = xsin\frac{1}{x}$ 

Давайте исследуем точку $x_0=0$

Найдем предел справа и слева:

$\lim\limits_{x\rightarrow{x_0+0}}{xsin\frac{1}{x}} = 0$ 

$\lim\limits_{x\rightarrow{x_0-0}}{xsin\frac{1}{x}} = 0$ 

Теперь определим значение функции в точке $x_0$:

$f(0) = 0 * sin\frac{1}{0}$ - функция в данной точке не определена

Пределы слева и справа равны, а функция не определена. Отсюда следует, что данная точка является точкой устранимого разрыва $I$-го рода.

#### Программное решение 2.3
```python
import matplotlib.pyplot as plt
import numpy as np
from math import * 
from sympy import *

# Определение символа x
x = Symbol ('x')

# Объявляем функцию
def f(x):
    return x * np.sin(1 / x)

# Создание массива значений x около точки разрыва
x0 = np.linspace(-0.125 * np.pi, 0.125 * np.pi, 100)
y0 = f(x0)

# Построение графика
plt.plot(x0, y0)
plt.axvline(x=0, color='red', linestyle='--', label='x=0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции f(x) = x * sin(1/x)')
plt.legend()
plt.grid()
plt.show()


# определение символьного выражения, соответствующего функции x*sin(1/x)
f = x * sin(1 / x)

# вычисление предела слева в нуле
lim_left = limit(f, x, 0, dir='-')


# по умолчанию вычисляется предел справа
lim_right = limit(f, x, 0)

print(f'Предел слева в точке x=0: {lim_left}')
print(f'Предел справа в точке x=0: {lim_right}')
```

#### Иллюстрация решения

![Image text](график2.4.png)

<p style="text-align: center;">Рис. 2.3. Иллюстрация решения задачи.</p>

![Image text](вывод2.4.png)

<p style="text-align: center;">Рис. 2.3. Вывод программы в терминале.</p>






