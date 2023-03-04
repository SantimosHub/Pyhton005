# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def num_degree(f_num, s_num):
    if s_num == 1:
        return f_num
    else:
        return f_num * num_degree(f_num, s_num - 1)


first_number = int(input('Ввведите 1 число: '))
second_number = int(input('Ввведите 2 число: '))

print(f'{first_number} в степени {second_number} = {num_degree(first_number, second_number)}')
