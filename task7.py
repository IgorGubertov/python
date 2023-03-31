"""
Задание 7.*
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = 'a + b * y'

    def __add__(self, other):
        print(f'Сумма x1 и x2 равна')
        return f'x = {self.a + other.a} + {self.b + other.b} * y'

    def __mul__(self, other):
        print(f'Произведение x1 и x2 равно')
        return f'x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * y'

    def __str__(self):
        return f'x = {self.a} + {self.b} * y'


x_1 = MyComplex(3, -8)
x_2 = MyComplex(5, 6)
print(x_1)
print(x_1 + x_2)
print(x_1 * x_2)