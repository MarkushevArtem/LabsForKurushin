from pyDatalog import pyDatalog
import random

"""
Задание 1
Посчитать сумму ряда
"""


pyDatalog.create_terms('Kol, summa')

summa[Kol] = Kol + summa[Kol-1]
summa[1] = 1

print(Kol == summa[100])


"""
Задание 2 - Вычислить среднее значение ряда
"""

pyDatalog.create_terms('Kol, averageValue')

averageValue[Kol] = (Kol+1)/2

print(Kol == averageValue[100])

"""
Задание 3 - Вычислить произведение 100 случайных чисел в диапазоне от 1 до 100
"""


pyDatalog.create_terms('Kol, productRandomNumbers')

productRandomNumbers[Kol] = random.randint(1,100) * productRandomNumbers[Kol-1]
productRandomNumbers[0] = 1

print(Kol == productRandomNumbers[100])


"""
Задание 4 - Вычислить медиану 100 случайных чисел в диапазоне от 1 до 100
"""


pyDatalog.create_terms('Kol, median')

median[Kol] = (random.randint(1,100) + median[Kol-1]) / 2
median[0] = 1


print(Kol == median[100])