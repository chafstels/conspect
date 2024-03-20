# '======================Двумерные массивы=============='
# # n = 3
# # m = 2
# # array = []
# # i = 0
# # while i < n:
# #     array.append([])
# #     j = 0
# #     while j < m:
# #         array[i].append(0)
# #         j += 1
# #     i += 1
# # print(array)

# # n = 3
# # m = 2
# # array = []
# # for i in range(n):
# #     array.append([])
# #     for j in range(m):
# #         array[i].append(0)
# # print(array)

# # n = 3
# # m = 5
# # array = list(range(n))

# # for i in range(n):
# #     array[i] = list(range(m))
# # print(array)

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# n = len(array)
# m = len(array[0])
# # i = 0
# # while i < n:
# #     j = 0
# #     while j < m:
# #         print(array[i][j], end=' ')
# #         j += 1
# #     print()
# #     i += 1
# # for i in range(n):
# #     for j in range(m):
# #         print(array[i][j], end=' ')
# #     print()

# # n = 3
# # m = 3
# # array = list(range(n))
# # for i in range(n):
# #     array[i] = list(range(m))
# #     for j in range(m):
# #         text = f'Введите элемент в {i}x{j} позицию: '
# #         el = input(text)
# #         array[i][j] = el

# # print(array)

# '============================Comperhensions========================='
# # Генетор - с помощью которого мы можем создать последовательность используя цикл for в одну строку
# # Результат for элемент in последовательность
# # Результат for элемент in последовательность if фильтр
# # Результат if условие else тело for элемент in последовательность
# # Результат if условие else тело for элемент in последовательность if фильтр

# comperhensions = (i for i in range(1,6))
# # print(type(comperhensions))

# # Генератор - это итерируемый обьект, который не хранит в себе полностью всю последовательность данных, а создает их когда требуется
# # print(next(comperhensions))
# # print(next(comperhensions))
# # print(next(comperhensions))
# # print(next(comperhensions))
# # print(next(comperhensions))
# # print(next(comperhensions)) # StopItration
# # next - функция, которая запрашивает у генератора текуший элемент и генератор создает следущий элемент

# '=========================Синтаксический сахар===================='
# #list comperhension
# # list_comp = list(i ** 2 for i in range(1,6))
# list_comp = [i ** 2 for i in range(1,6)]
# # print(list_comp)

# # list_ = []
# # for i in range(1,6):
# #     list_.append(i**2)

# new_list = [1, 'heloo', 2, True, 2, 2, False, 'string']
# new = [i for i in new_list if type(i) == str]
# print(new)

# '==========================Dict comperhension================'
# # dict_ = dict((i, i **2) for i in range(10))
# dict_ = {i:i**2 for i in range(10)}
# # print(dict_)

# dict_ = {'a': [1,2,3,4,11], 'b': [1,2,3], 'c': [2,3,4,5]}
# new = {key: sum(value)  for key, value in dict_.items()}
# # print(new)

# example = [['helloworld' for i in range(5)] for i in range(3)]
# # print(example)

# '==================Set comperhension===================='
# set_ = {1,2,3,4,5,1}
# set_1 = {i for i in set_}
# # print(set_1)

# '====================Вложенные comperhension==============='
# # dict_ = {v: [i for i in range(1, v+1)] for v in range(1,6)}
# # print(dict_)

# dict_ = {k: list(range(1,k+1))for k in range(1,6) }
# # print(dict_)

# dict_ = {k: {v: [l for l in range(1,v+1)] for v in range(1, k+1)} for k in range(1,6)}
# # print(dict_)


# '========================Random======================'
# import random

# a = random.randint(0,10)
# a = random.randrange(0,10,2)

# # print(a)
# again = 'д'
# while again.lower() == 'д':
#     print("Бросаем кубики....")
#     print("Значение граней: ")
#     print(random.randint(1,6))
#     print(random.randint(1,6))
#     again = input("Бросить кубики еще раз? (д = да, н = нет)")


n = 3
m = 4
array = list(range(n))
for i in range(n):
    array[i] = list(range(m))
    for j in range(m):
        array[i][j]

# for i in range(n):
#     for j in range(m):
#         print(array[i][j], end=' ')
#     print()

# matrix = [[i + j * 3 + 1 for j in range(3)] for i in range(3)]

# for row in matrix:
#     print(*row, end=' ')
#     print()

# for i in range(1,6):
    # for j in range(1,6):
        # print(f'{i} * {j} = {i*j}', end='\t')
    # print()

# size = 8

# for i in range(size):
#     for j in range(size):
#         symvol = '*' if (i + j) % 2 == 0 else '.'
#         print(symvol, end=' ')
#     print()

# a = [ 12, 22 ,4,5, 6, 1, 50]
# b = [ i for i in a if i > 5]
# print(b)

# years = [i for i in range(1900,2024) if (i % 4 == 0 and i % 100 !=0) or (i %400 ==0)]
# print(f'Год високосный: ', *years)

# number = int(input('Введите число: '))

# for i in range(1,11):
    # print(f'{number} * {i} = {number * i}')

# a = 1
# sum_numbers = 0
# while a <= 30:
#     sum_numbers += a
#     a += 1
# print(sum_numbers)
# list_ = [10,30,40,100]
# if 20 in list_:
#     b = list_.index(20)
#     list_[b] = 200
# print(list_)


# spisok = [11,44,22,32,1,2,3]
# # a = [i ** 2 for i in spisok]
# # print(a)
# index = len(spisok) -1
# new_spisok = []
# while index >= 0:
#     new_spisok.append(spisok[index])
#     index -= 1
# print(new_spisok)


# dict_ = {k: k ** 3 for k in range(1,11)}
# print(dict_)
# a = 3
# b = -11
# c = -2
# possitive = len([num for num in [a,b,c] if num > 0])
# print(possitive)

# months = int(input())
# years = int(input())

# total_days = months * 30 + years * 365
# print(total_days)

print(dir(list))

list_ =[]
print(list_.append(1))
print(list_.count(1))
