# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primfacs(num):
     list1 = []
     i = 2
     while num > 1:
         if num % i == 0:
             list1.append(i)
             num /= i
         else:
             i += 1
     print('Список простых множителей:', list1)

primfacs(int(input('Укажите число N: ')))