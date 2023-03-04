# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def num_summer(f_num, s_num):
    if s_num == 0:
        return f_num
    else:
        return num_summer(f_num, s_num - 1) + 1


first_number = int(input('Ввведите 1 число: '))
second_number = int(input('Ввведите 2 число: '))

print(f'{first_number} + {second_number} = {num_summer(first_number, second_number)}')
