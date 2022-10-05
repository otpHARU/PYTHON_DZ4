# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.

from random import choices

def num_list(count):
    if count <= 0:
        return 'Ошибка!'
    list1 = choices(range(10), k = count)
    return list1

def get_unique_numbers(numbers):
    uni_list = []
    for number in numbers:
        if numbers.count(number) == 1:
            uni_list.append(number)
    return uni_list
    
list2 = num_list(int(input('Укажите количество элементов в списке: ')))
if list2 != 'Ошибка!':
    print ('Последовательность чисел:', list2)
    print('Список неповторяющихся элементов:', get_unique_numbers(list2))
else:
    print('Ошибка! Повторите запрос!')














