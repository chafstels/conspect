'=======================Числовой тип(integer)==============='
'''Основные операции с числами
В языке Python, как и в матиматике, над числами можно совершать арифметические операции

Операторы      Описание
   +           Сложение
   -           Вычитание
   *           Умножение
   /           Деление
   //          Деление, без остатка
   %           Деление, остаток от деления
   **          Ввозведение в степень
   25 ** 0.5   Нахождение квадратного корня числа
'''
a = 5
b = 1
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# print(a+b*a-b)
# 9

# print((a+a)-b*a)
# 5

# num1 = 2 + 3 * 4
# num2 = (2 + 3) * 4
# num1 = 14
# num2 = 20

# num1 = '12'
# num2 =  6
# print(num1-num2)

# int = целое число
# float = вещественное число
# decimal = точное вещественное число
# bin = бинарное число
# complex = комплексное число


# from decimal import Decimal
# b = Decimal('0.1')
# b = 0.1
# print(b+b+b+b+b+b+b+b+b+b)
# print(bin(2796202))
# print(complex(1, 5))


# # модуль числа = положительное число | -5 | | 5 | = 5
# print("Модуль числа:",abs(-5))

# # round - округление числа
# print(round(5.5))
# print(round(5.4))
# print(round(5.432456234, 4))

# from math import sqrt
# print(sqrt(25))

# #pow
# # 1. Возводит в степень
# # 2. Находит остаток от делаения на третье число
# print(pow(2,3)) # = 2 ** 3 = 8
# print(pow(2,3,3))# = 2 ** 3 % 3 = 2


# number = 12345
# print(number % 100 // 10 )

# '''
# Написать программу, в которой рассчитывается сумма и произведение цифр положительного трехзначного числа
# '''
# a=int(input("Введите трехзначное число"))
# n1 = a % 10
# n2 = (a % 100) // 10
# n3 = a // 100
# print(n1,n2,n3)
# print('Cумма чисел:', n1+n2+n3)
# print('Проиведение чисел:', n1*n2*n3)


a = '123'
print(type(a))
a = 123
print(type(a))
a = [123]
print(type(a))
