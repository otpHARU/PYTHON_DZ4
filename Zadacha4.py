# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.

from random import randint
import itertools

k = randint(2, 9)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

number = int(input('Укажите количество многочленов, которые нужно записать в файл: '))
with open('result1.txt', 'w') as data:
    data.write('Polynominals:\n')
while number > 0:
     ratios = get_ratios(k)
     polynom1 = get_polynomial(k, ratios)
     print ('Список чисел:', ratios)
     print('Полученный многочлен:', polynom1)
     data = open('result1.txt', 'a')
     data.write(f'{polynom1}\n')
     number -= 1
print('Данные записаны!')








