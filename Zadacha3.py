# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.

from random import choices

def num_list(count):
    list2 = choices(range(10), k = count)
    return list2

def get_unique_numbers(numbers):
    uni_list = []
    for number in numbers:
        if number in uni_list:
            continue
        else:
            uni_list.append(number)
    return uni_list
    
my_list = num_list(int(input('Укажите количество элементов в списке: ')))
print(my_list)
print(get_unique_numbers(my_list))














