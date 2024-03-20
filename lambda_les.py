'================================Lambda==============================='
hello = lambda:'hello'
# print(hello())
# sum_kvad = lambda a,b : a**2 + b**2
# print(sum_kvad(1,10))

# Анонимная функция - функция с телом, но без имени
# Общий формат определения : lambda список_параметров: выражение

f1 = lambda x,y,z: x+y+z
f2 = lambda x,y,z=3: x+y+z
f3 = lambda *args: sum(args)
f4 = lambda **kwargs: sum(kwargs.values())
f5 = lambda x, *, y=0, z=0: x+y+z
# обязательные именнованныве аргументы (*)

# print(f1(1,2,3))
# print(f2(1,2))
# print(f3(1,2,3,4,5,6,7,8,9,10))
# print(f3(1,2))
# print(f4(one=1,two=2,three=3))
# print(f5(1))
# print(f5(1, y=5, z=3))

# 1. Однократное использование функции
# 2. Передача функций в качестве аргументов другим функциям
# 3. Возращение функции в качестве результата другой функции


# strings = ['a','b','c','d','e']
# numbers = [3,2,1,4,5]
# new_strings = list(map(lambda x,y: x*y, strings, numbers))
# print(new_strings)


# numbers = [-1, 2, -3, 4, 0, 10, 30, 50, 100, -90]

# positive_numbers = list(filter(lambda x: x>0, numbers))
# large_numbers = list(filter(lambda x: x>50, numbers))
# even_numbers = list(filter(lambda x: x%2==0, numbers))
# # print(positive_numbers, large_numbers, even_numbers, sep='\n')

# even_numbers2 = list(map(lambda x: 'even' if x %2==0 else 'odd', numbers))
# print(even_numbers2)

# def recursion(x):
#     print(x)
#     recursion(x+1)

# recursion(1)


# def increase(start,end):
#     print(start)
#     if start == end:
#         return start
#     else:
#         increase(start+1,end)

# increase(1,10)

'===================================Рекурсия==========================='
# Рекурсивная функция - это функция, которая вызывает сама себя, и при каждом очередном вызове использует данные, созданные во время предыдущего вызова.


# 1. Граничный случай, при котором функция завершает работу и возращает данные в основную программу
# 2. Рекурсивный случай, при котором функция продолжает вызывать себя

def greetings(st):
    print(st)
    if len(st) == 0: # Граничный случай
        return
    else:
        greetings(st[:-1]) # Рекурсивный случай

# greetings('Hello world!')


# def fact_iter(n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial *= i
#     return factorial

# print(fact_iter(int(input())))

# def fact_iter(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact_iter(n-1)

# print(fact_iter(4))

# a = int(input())
# b = int(input())
# c = int(input())
# multi = lambda x, y, z: f'Обьем коробки: {x*y*z}'
# print(multi(a,b,c))

# cubes = lambda x,y: x**3 +y**3
# print(f'Cумма кубок {cubes(3,2)}')



# def odd_numbers(n):
#     if n <=0:
#         return
#     if n % 2 != 0:
#         print(n)
#     odd_numbers(n-1)


# odd_numbers(10)


# day_new_year = lambda days_pass: 365-days_pass
# print(day_new_year(80))


# day_year = lambda year: year * 365
# print(day_year(5))

# def remove_one(lst):
#     if not lst:
#         return []
#     lst.pop()
#     print(lst)
#     remove_one(lst)

# list_ = [1,2,3,4,5]
# remove_one(list_)

list_ = [12,33,24,2,55,100,9,27]
# squared = list(map(lambda x: x**2, list_))
# print(squared)

# module_3 = list(filter(lambda x: x%3==0, list_))
# print(module_3)

# def sum_numbers(n):
#     if n == 0:
#         return 0
#     else:
#         return n%10 + sum_numbers(n//10)

# print(sum_numbers(256))
