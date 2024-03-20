'==============================Условия============================'
# Логические операторы - это выражения, которые возращают True, если выражение верно и false - если не верно

"равенство"
5 == 5 # True
4 == 5 # False

"не равенство"
4 != 5 # True
4 != 4 # False

"больше"              "больше или равно"
5 > 4 # True       5 >= 10 # False
5 > 10 # False     5 >= 4 # True
5 > 5 # False      5 >= 5 # True

"меньше"              "меньше или равно"
5 < 4 # False      5 <= 10 # True
5 < 10 # True      5 <= 4 # False
5 < 5 # False      5 <= 5 # True

'===========================AND, OR, NOT============================'
# and = и
# or = или
# not = нет

a = 5
b = 6
# AND
# print(a == 5 and b == 6) #True
# print(a == 5 and b == 7) #False
# print(a == 1 and b == 1) #False

# если все выражения возращают True, то вернется True
# если хотябы одно выражение или все выражения возращают False, то вернется False

# OR
# print(a == 5 or b == 6) # True
# print(a == 5 or b == 2) # True
# print(a == 1 and b == 1) # False

# если хотя бы одно выражение возращает True, то вернется True

# NOT
not True # False
not False # True

"========================Boolean Type========================="
# булевый тип данных имеет только 2 значения True, False
bool(1) #True
bool(0) #False
bool([[]]) #True
bool([]) #False

'=========================None Type=========================='
# None - неизменямый тип данных с одним значением None, который используется для обозначения отсутствия значения, для обозначения пустоты
bool(None) # False
bool('None') # True

'==========================Условные операторы======================'
# условные операторы - конструкция, которая используется для того чтобы создать структуру условий для входных данных, для разных событий
# number = input('Put your number: ')
# if number.isdigit():
#     number = int(number)
#     if number == 1:
#         print("вы ввели число 1")
#     elif number == 2:
#         print("вы ввели число 2")
#     elif number == 3:
#         print("вы ввели число 3")
#     else:
#         print("вы ввели число больше 3")
# else:
#     print(input("Введите число: "))

# в одной конструкции может быть только один if
# в одной конструкции может быть много elif либо вообще не быть
# в одной конструкции может быть лишь один else либо вообще не быть

'======================Цепочки сравнений================='
# age = int(input())
# if 3 <= age <= 6: # 3 <= age and age <= 6
#     print("Вы ребенок")

# a=4
# b=1
# c=4
# if a == b == c:
#     print("числа равны!")
# if a != b and a != c and b != c:
#     print("числа не равны")

'''
При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
'''
# passw1 = input("Введите пароль:")
# passw2 = input("Введите повторно пароль:")
# if passw1 == passw2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

'===========================Тернарный оператор===================='
# тернарный оператор - это условие в одну строку
# num = int(input())
# result = 'Hello' if num == 5 else 'Buy'
# print(result)

# number = int(input())
# if 0 <= number <= 21 or 57 <= number <= 100:
#     print("Разрешен")
# else:
#     print("Неразрешен")

# number = int(input())
# is_chet = 'Четное' if number % 2 == 0 else "Нечетное"
# a = "Число делится на 3"    if number % 3 == 0 else "Число не делится на 3 без отстатка"
# b = "Число больше 1000"  if number ** 2 > 1000 else "Число меньше 1000"
# print(is_chet,a,b, sep='\n')

# age = int(input())
# if age < 0 or age > 120:
#     print("Не допустимый возраст")
# elif age >= 18:
#     print("Cовершеннолетний")
# elif 0 <= age <= 4:
#     print("Ребенок")
# elif 4 < age < 18:
#     print("Несовершеннолетний")
# print("Не допустимый возраст" if age < 0 or age > 120 else "Cовершеннолетний" if age >= 18 else "Ребенок" if age <= 4 else "Несовершеннолетний")


# year = int(input())
# if 2024 == year:
#     print("Текуший год")
# elif 2024 < year:
#     print("Год еще не наступил")
# else:
#     print("Год прошел")

# a = 1
# b = 2
# c = 3
# if a > b > c:
#     print(a, "больше а")
#     if b < c:
#         print(b, "меньшее число")
#     else:
#         print(c, "меньшее число")
# elif b > a and b > c:
#     print(b, "больше b")
#     if a < c:
#         print(a, "меньшее число")
#     else:
#         print(c, "меньшее число")
# else:
#     print(c, "больше c")
#     if a < b:
#         print(a, "меньшее число")
#     else:
#         print(b, "меньшее число")


# a = 17391
# b = 546
# c = 934
# a1 = 17391 % 17
# b1 = 546 % 17
# c1 = 934 % 17
# if a1 > b1 > c1:
#     print(c)
# elif c1 > a1 > b1:
#     print(b)
# else:
#     print(a)

# number = int(input())
# if number % 6 == 0:
#     print("число делится на 6", number/6)
# else:
#     print("не делится")

# a = int(input())
# b = int(input())
# c = int(input())
# if a > 10 and b > 10 and c > 10:
#     print("yes")
# else:
#     print('no')

# a = int(input())
# b = int(input())
# multi = int(input())
# print("Произведение чисел:", a*b)
# if a*b == multi:
#     print("Вы посчитали правильно!")
# else:
#     print("Вы ошиблись")

# month_number = int(input())

# if 1 <= month_number <= 2 or month_number == 12:
#     season = 'За окном падал белый снег'
# elif 3 <= month_number <=5:
#     season = 'Птицы пели прекрасные песни'
# elif 6 <= month_number <=8:
#     season = 'Солнце светило ярче, чем когда-либо'
# elif 9 <= month_number <=11:
#     season = 'Урожай был невероятным'
# else:
#     season = 'Такого месяца не существует'

# print(season)

# a = int(input())
# if 0 < a < 5:
#     print("Верно")
# else:
#     print("Неверно")

# a = int(input())
# b = int(input())
# if a <= 1 and b >= 3:
#     print(a+b)
# else:
#     print(a-b)

# a = int(input())
# b = int(input())
# if 2 < a < 11 or 6 <= b < 14:
#     print("верно")
# else:
#     print("неверно")


# apartment = int(input())

# if 1 <= apartment <= 20:
#     print("Подьезд 1")
# elif 21 <= apartment <= 48:
#     print("Подьезд 2")
# elif 49 <= apartment <= 90:
#     print("Подьезд 3")
# else:
#     print("Такого подьезда не существует")

# finger_number = int(input("Введите номер пальца руки:"))

# if finger_number == 1:
#     print("Большой палец")
# if finger_number == 1:
#     print("указательный")
# if finger_number == 1:
#     print("средний")
# if finger_number == 4:
#     print("безымянный")
# else:
#     print("мизинец")

# number = int(input())

# if number % 2 == 0:
#     print('число делится на 2')
# else:
#     print("число не делится на 2")

# if number % 4 == 0:
#     print('число делится на 4')
# else:
#     print("число не делится на 4")

# if number % 6 == 0:
#     print('число делится на 6')
# else:
#     print("число не делится на 6")

# angle1 = int(input())
# angle2 = int(input())
# angle3 = int(input())

# if angle1 + angle2 + angle3  == 180 and angle1>0 and angle2>0 and angle3>0:
#     print("треугольник существует")
# else:
#     print("треугольник невалиден")

# a = int(input())
# b = int(input())
# c = int(input())

# d = b**2 - 4*a*c

# from math import sqrt
# root1 = (-b +sqrt(d)) / (2*a)
# root2 = (-b -sqrt(d)) / (2*a)
# print(root1)
# print(root2)


# a = int(input())
# result = "Любит" if a % 2 ==0 else "Не Любит"
# print(result)


# temp_C = int(input("Напишите температуру в цельсиях: "))
# f = temp_C * 9/5 - 32
# print("Температура в Фаренгейтах: ", f)

# print('Выберите операцию ')
# print("Введите 1 для конвертации Фаренгейта в Цельсий")
# print('Введите 2 для конвертации Цельсия в Фаренгейт')
# choice = int(input('Ваш выбор: '))

# if choice == 1:
#     fareng = int(input())
#     c = fareng * 5/9 + 32
#     print(c)
# elif choice ==2:
#     celsius = int(input())
#     f = celsius * 9/5 - 32
#     print(f)
# else:
#     print("Error")


