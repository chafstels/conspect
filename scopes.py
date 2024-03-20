# '==================================Области видимости============================'
# # LEGB - Local Enclosed Global Build-in

# # def func(a):
# #     b =10
# #     print(a)
# # print(b)

# '=================================BUILD IN============================='
# # встроенное пространство имен (list, sum, print, input ..........)

# '===================================Global=============================='
# # все переменные, которые мы создали внутри одного файла(модуля) чтобы посмотреть глобальные переменные можно использовать globals
# a = 1
# b = 2
# # print(globals())
# '===================================Encloused (nonlocal)==============================='
# # Замкнутое пространство имен - локальное пространство, у которого есть внутреннее локальное пространство.

# var = 'globals'

# def func():
#     var = 'enclosed'
#     def inner_func():
#         var = 'local'
#         print(var)
#     print(var)
#     inner_func()

# print(var)
# func()

# '===============================Local=================================='
# # Локальное пространство имен - переменные, созданные внутри функции(можно посмотреть с помощью locals())
# # a = 10
# # def func(a,b):
# #     print('Globals: ', globals())
# #     print('Locals: ', locals())
# #     print(a,b)
# # func(5,6)

# # count1 = 1
# # def count_():
# #     print(count1)
# #     count1 += 1
# # count_()
# # print(count1)
# # #UnboundLocalError: cannot access local variable 'count1' where it is not associated with a value

# count_1 = 0
# def count_():
#     global count_1 #доступ на изменение переменной глобального пространства
#     count_2 = 0
#     for i in range(5):
#         count_1 += 1
#     def inner_func():
#         nonlocal count_2
#         print(count_2)
#         count_2 = 100
#     inner_func()
#     print(count_2)
# # print(count_1)
# count_()
# # print(count_1)


"""
1) Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.
"""
# matreshka = 100
# def func(matreshka1):
#     global matreshka
#     matreshka = matreshka + matreshka1
#     def inner_func(matreshka2):
#         global matreshka
#         matreshka = matreshka + matreshka2
#     inner_func(1)
# func(10)
# print(matreshka)

"""
2) Дана глобальная переменная num со значением 3. Напишите функцию mul которая будет возвращать квадрат этой переменной и записывать результат в глобальную переменную num. Вызовите функцию три раза, и распечатайте переменную num.
"""
# num = 3
# def mul(number):
#     global num
#     num = number**2
#     return num

"""
2) Есть глобальная переменная, которая содержит пустой список. Вам необходимо написать функции, одна из которых add() - добавляет в этот список имена, которые вводит пользователь. А другая функция remove() - удаляет эти имена из списка по индексу, который вводит пользователь. Вызовите функции в рандомном порядке 10 раз и в конце выведите список.
"""
# list_ = []

# def add():
#     global list_
#     users = map(str, input('Введите имена юзеров: ').split())
#     for name in users:
#         list_.append(name.capitalize())
#         print(f'Юзер с именем - {name}, был добавлен')
#     return list_

# def remove():
#     global list_
#     try:
#         ind = int(input("Введитн номер юзера, которого хотите удалить: "))
#         user = list_.pop(ind)
#         print(f'Юзер, {user} удален')
#     except ValueError:
#         print("Введите число!")
#     except IndexError:
#         print("Такого юзера нету")
#     return list_

# def random_func(number):
#     import random
#     for _ in range(number):
#         ran = random.randint(0,1)
#         if ran == 0:
#             add()
#         else:
#             remove()
#     return list_

# print(random_func(10))

# names = ['Beka', 'Alymbek', 'Aziz', 'Nursultan', 'Timur', 'Dastan', 'ISA', 'Emir', 'Ilim']
# list_ = []
# import random
# for i in range(3):
#     list_.append(random.choice(names))



# import sys
# # print(sys.platform)
# a = input()
# b = input()
# print(a if sys.getsizeof(a)>sys.getsizeof(b) else b)

# n = int(input())
# list_ = []
# for i in range(n):
#     import random
#     list_.append(str(random.randint(1,10)))

# print(''.join(list_))

# import random

# def get_choice():
#     choices = ['Камень', 'Ножницы', 'Бумага']
#     return random.choice(choices)

# def game(player, comp):
#     if player == comp:
#         print('Ничья')
#     elif player == "Ножницы" and comp == "Бумага" or \
#         player == 'Камень' and comp == "Ножницы" or \
#         player == 'Бумага' and comp == "Камень":
#         print("Вы выиграли!")
#     else:
#         print('Вы проиграли')

# player = input()
# computer = get_choice()
# game(player, computer)


min, max = max, min
spisok = [i for i in range(10)]
print(max(spisok))
