<h2 style="text-align: center;">Бюджетное учреждение высшего образования Ханты-Мансийского автономного округа – Югры</h2>  

<h1 style="text-align: center;">«СУРГУТСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»</h1>

<h2 style="text-align: center;">Политехнический институт</h2>

<p style="text-align: center;">Кафедра прикладной математики</p>

<p style="text-align: center;">Миронов Роман Алексеевич</p>

<h1 style="text-align: center;">Числовые последовательно</h1>

<p style="text-align: center;">Дисциплина «Математический анализ»</p>

<p style="text-align: center;">направление 01.03.02 «Прикладная математика и информатика»</p>

<p style="text-align: center;">направленность (профиль): «Технологии программирования и анализ данных»</p>

<pre>

</pre>

<p style="text-align: right;">Преподаватель:  </p>

<p style="text-align: right;">Доцент,  Ряховский Алексей Васильевич</p>

<p style="text-align: right;">Студент гр. № 601-31</p>

<p style="text-align: right;">Миронов Роман Алексеевич</p>

<pre>

  
</pre>

<p style="text-align: center;">Сургут 2023 г.</p>

<h3 style="text-align: center;">Лабораторная работа №1. Числовые последовательности.</h3>

#### Задание

Вычислить пределы данных числовых последовательностей двумя способами: 

- аналитически 
- используя библиотеки Python для символьных вычислений. 

<p style="text-align: justify;">Для каждой числовой последовательности $\{x_k\}_{k=1}^\infty$ на одном рисунке построить (используя графические пакеты Python) следующие множества точек ($k = 1, \ldots, m$):</p>

- (k, 0) – синий цвет
- (0, $x_k$) – зеленый цвет
- (k, $x_k$) – красный цвет

<p style="text-align: justify;">В случае, если последовательность сходится, построить на соответствующем рисунке точку (оранжевый цвет) изображающую предел последовательности $\{x_k\}_{k=1}^\infty$.</p> 

<p style="text-align: justify;">В задаче 1 для сходящихся последовательностей, для заданного $\varepsilon>0$ найти такой номер $n(\varepsilon)$, начиная с которого $|x_k-A|<\varepsilon, \forall k\geq n(\varepsilon)$ </p>

#### Аналитическое решение1

Рассмотрим предел: $\lim\limits_{n \to \infty} \frac{\sin n + n^2}{2n^2+n+1}$

Найдем пределы числителя и знаменателя: 
- $\lim\limits_{n\rightarrow\infty}\sin n + n^2 = \infty$ 
- $\lim\limits_{n\rightarrow\infty}2n^2+n+1 = \infty$

<p style="text-align: justify;">Поскольку выражение $\frac{\infty}{\infty}$ является неопределенностью, преобразуем его, деля каждое слагаемое в числителе и знаменателе на старшую степень, в данном случае это $n^2$:</p>

$\lim\limits_{n\rightarrow\infty}\frac{\frac{sin n}{n^2}+\frac{n^2}{n^2}}{\frac{2n^2}{n^2}+\frac{n}{n^2}+\frac{1}{n^2}} = \lim\limits_{n\rightarrow\infty}\frac{\frac{sin n}{n^2}+1}{2+\frac{1}{n}+\frac{1}{n^2}}$

Вычислим предел числителя, вычисляя предел каждого слагаемого:

$\lim\limits_{n\rightarrow\infty}\frac{sin n}{n^2}=0$

$\lim\limits_{n\rightarrow\infty} =1$

Следовательно:
$\lim\limits_{n\rightarrow\infty}({\frac{sin n}{n^2}+1})=1$

Аналогично для знаменателя:
$\lim\limits_{n\rightarrow\infty}(2+\frac{1}{n}+\frac{1}{n^2}) = 2$

Таким образом, предел числителя равен 1, а предел знаменателя равен 2.

$\lim\limits_{n \to \infty} \frac{\sin n + n^2}{2n^2+n+1} = \frac{1}{2}$

Ответ: $\frac{1}{2}$

Найдем номер $n(\varepsilon)$

$\lim\limits_{n \to \infty} \frac{\sin n + n^2}{2n^2+n+1} = \frac{1}{2}$

$|\frac{\sin n + n^2}{2n^2 + n + 1} -\frac{1}{2}| $




  









