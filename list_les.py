'============================LIST========================='
# Cписок(list) - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке.

list1 = [1,2,3,4,'hello',[2,3,4,5],None,True]
list1[4] # hello
list1[5] # [2,3,4,5]
list1[5][-1] # 5

list2 = list('ada') # ['a', 'd', 'a']
list3 = list(range(1,11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# range - генетор какого-нибудь диапазона range(start,end,step)

list_sum = list2 + list3 # ['a','d', 'a', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list4 = [4] * 5 # 4, 4, 4, 4, 4]

'==========================Методы списка========================='
# print(dir(list))

#append - добавляет элемент в конец списка
name = 'Anton'
list1 = []
list1.append(2)
list1.append('ada')
list1.append(2/2)
list1.append(name)
list1.append({2,2,2,2,2,2,3,4})
print(list1)

# pop - удаляет элемент из списка по индексу и возращает этот удаленный элемент, если не указть индекс то он удалит последний элемент

list1 = [1,2,3,4,5,6,'ada', 'ada']
# list1.pop(1)
# list1.pop()
# print(list1)

# remove - удаляет элемент из списка по значению
# list1.remove('ada')
# print(list1)

#count - считает количество принятого элемента в списке
# print(list1.count('ada'))

#index - возращает индекс первого вхождения принятого элемента
# print(list1.index('ada'))
ada = list1.index('ada')
# list1.pop(ada)
# print(list1)

#insert - добавляет элемент в список по индексу
# list2 = [1,2,4,5,6]
# list2.insert(2,[2,4,4,5])
# print(list2)

# extand - расширяет список засчет другого списка
list1 = [0,0,0]
list2 = [1,1,1]
# list1.append(list2)
list1.extend(list2)
print(list1)

# reverse - изменяет список, раставляя его элементы в обратном порядке
list_1 = [3,2,1,5,6,8]
# list_1.reverse()
# print(list_1)

# sort - cортирует список, состоящий из элементов одного типа данных
# list_1.sort()
# print(list_1)
## sort (key=функций с логикой сортировки, reverse = True либо False)
# list_1.sort(reverse=True)
# print(list_1)


# clear - очищение списка
# list_1.clear()
# print(list_1)

# a,b,c,d = [[123],'adad',{'a':1},4] # множественное присвоение
# print(a,b,c,d)

list1 = list('helloworld')
list2 = ''.join(list1) # склеивание списка в строку
print(*list1) # распаковка списка
print(list2)

# hello = list1
# list1.pop()
# print(hello)

# copy - метод для копирования данных внутри списка
# hello = list1.copy()
# list1.pop()
# list1.append('122345')
# print(hello)
# print(list1)

# name, age, prof = ['Anton', 25, 'Mentor']
# print(f'Привет, меня зовут {name}, я {prof}, мне {age} лет')

# list_ = [1,2,3,4,5,6,7]
# vedro = []
# for i in list_:
#     print(f"Почистил картошку {i}")
#     vedro.append(i)
# print(vedro)


'''
На вход программе подается одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].'''

# n = int(input())
# list_ = list(range(1,n+1))
# print(list_)
# print(len(list_))


'=====================Оператор принаджлежности in============='
# numbers = [2,4,6,8,10]
# if 2 in numbers:
#     print("список содержит число 2")
# else:
#     print(" нету числа 2")


'======================Max() Min() Sum()======================'

# numbers = [12,2323,56,333,444,2,4,6,8,10]
# print(sum(numbers)) # сумма всех элементов списка
# print(min(numbers)) # минимальный элемент списка
# print(max(numbers)) # максимальных элемент списка

# numbers[1] = 13
# print(numbers)

'=========================Кортеж(tuple)======================'
# tuple_ = (1,2,3) # Кортеж
# tuple_ = (1) # int
# tuple_ = (1,) # tuple
# tuple_ = () # tuple
# tuple_ = 1, # tuple
# tuple_ = tuple('hello world')
# print(dir(tuple))

# spisok = [(),(),()]

# spisok = []
# for i in range(3):
#     spisok.append(())
# print(spisok)

spisok = [(1,2),(3,),(5,)]
for i in spisok:
    print(spisok.index(i))


# spisok.append(str)
# spisok.append(int)
# spisok.append(float)
# spisok.append(bool)
# spisok.append(None)
# print(spisok)

# names = ['Anton', 'Alina', 'Adilet', 'Ainazik', 'Max']
# new_string = ' '.join(names)
# print(new_string)


# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 'Дополните приведенный код так, чтобы он вывел среднее арифметическое элементов списка evens.'
# summa = sum(evens)
# count = len(evens)
# print(summa/count)

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# '[2, 3, 5, 7, 11, 13]'

# print(primes[:6])

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
'''
Дополните приведенный код так, чтобы элемент списка имеющий значение Green заменился на значение Зеленый, а элемент Violet на Фиолетовый. Далее необходимо вывести полученный список.'''
# rainbow[3] = 'Зеленый'
# rainbow[-1] = 'Фиолетовый'
# print(rainbow)


languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
languages[::-1]
print(languages)

# '''
# На вход программе подается натуральное число n. Напишите программу, которая создает список, состоящий из делителей введенного числа.
# '''

# number = int(input())
# spisok = []
# for i in range(1,number+1):
#     if number % i == 0:
#         spisok.append(i)

# print(spisok)


# list_ = []
# list_.append('25')
# list_.append('Anton')
# list_.append('Python')
# print(list_)

# l = [1, 2, 5, 3]
# a = 1
# for i in l:
#     a *= i

# print(a)
# String № 1
s = 'Integers 1,2,3 Floats 44 Strings 5 Lists 10Tuples'
numbers = []
letters = []
for i in s:
    if i.isdigit():
        numbers += i
    elif i.isalpha():
        letters += i
print(''.join(numbers))
print(''.join(letters))

l = ['integer', 'float', 'string', 'list', 'loop', 'tuple', 'while', 'for']
# print(l.pop(0), l.pop(0), l.pop(0))
# l1 =[l.pop(0), l.pop(1), l.pop(2)]
# count = 0
# for i in l:
#     if count <3:
#         print(i)
#         count +=1
# print(l[0:3])


# '''
# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных строк список и выводит его.'''

# number = int(input())
# spisok = []
# for i in range(number):
#     string = input('напишите свой элемент списка: ')
#     spisok.append(string)
# print(spisok)


'''
Напишите программу, выводящую следующий список:
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...26z]'''
# a = 'abcdefhijklmnopqrstuvwxyz'
# l = []
# for i in range(0,len(a)):
#     l.append(a[i] * (i+1))

# print(l)

'''
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает список из символов всех строк, а затем выводит его.
'''

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# number = int(input())
# spisok = []
# for i in range(number):
#     string = list(input('напишите свой элемент списка: '))
#     spisok.extend(string)
# print(spisok)

# number = int(input())
# spisok = []
# for i in range(number):
#     string = input('напишите свой элемент списка: ')
#     spisok.extend(string)
#     a = list(spisok)
# print(a)
