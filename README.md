# modul_arithmetic

При написании программы не использовались сторонние или встроенные в Python библиотеки, которые реализуют функционал задания. 

Быстрое возведение в степень по модулю работает как для отрицательной степени так и для основания.

Для решения уравнения вида ax ≡ b mod m в программе есть 2 функции. *solve_equation_euler()* решает уравнение,
когда gcd(a, m) = 1 и следовательно находит единственный x. *solve_equation()* находит все натуральные корни уравнения.

Для проверки на простоту числа в программе также реализовано 2 функции: перебор делителей до sqrt(n) и тест Миллера-Рабина.

Также реализована функция для нахождения обратного по модулю числа - *modular_multiplicative_inverse()*

Для тестирования программы написаны тесты, которые для проверки используют встроенную в Python функцию pow().

