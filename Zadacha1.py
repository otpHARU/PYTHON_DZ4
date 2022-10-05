# Вычислить число c заданной точностью d

num = float(input('Введите число: '))
d = int(input('Укажите точность: '))

num_with_precision = '{:.' + str(d) + 'f}'
print(num_with_precision.format(num))