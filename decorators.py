'=================================Декоратор================================'
# Функция высшего порядка - эта та функция которя принимает в аргументы другую функцию, создает внутри себя функцию, вызывает функцию и возращает функцию
from datetime import datetime
import time
def decorator(func):
    def wrapper():
        print('start: ', datetime.now())
        func()
        print('finish: ', datetime.now())
    return wrapper

def hello():
    print('hello_world')

def range_10():
    for i in range(10):
        print(i)
        time.sleep(1)

# hello = decorator(hello) # первый способ вызовва декоратора
# hello()

# decorator(hello)() # второй способ вызова декоратора


# decorator(range_10)()


# Декоратор - это функция высшего порядка, которая нужна чтобы расширять функционал другой функции не изменяя ее (функция обвертка)


def decorator(func):
    def wrapper():
        print("Я - код, до вызова функции")
        func()
        print("Я - код, после вызова функции")
    return wrapper

@decorator # третий способ вызова декоратора
def hello():
    print('hello_world')

# hello()

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Я - код, до вызова функции")
#         print(func(*args, **kwargs))
#         print("Я - код, после вызова функции")
#     return wrapper


# @decorator
# def hello(a,b):
#     return a + b

# @decorator
# def substract(a,b,c):
#     return a - b

# hello(5,5)
# substract(10,5,2)

'''
Напишите декоратор text_decor, который оборачивает вызов декорированной функции фразами «Hello» и «Goodbye!»: фраза «Hello» печатается до вызова, фраза «Goodbye!» - после
'''

'Напишите декоратор repeater, который дважды вызывает декорированную функцию'

# def repeater(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper


# @repeater
# def multiply(num1,num2):
#     print(num1*num2)

# @repeater
# def one(num1):
#     print(num1)
# multiply(2,6)
# one(1)

'Напишите декоратор double_it, который возвращает удвоенный результат вызова декорированной функции'

# def double_it(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) * 2
#     return wrapper


# @double_it
# def multiply(num1,num2):
#     return num1*num2


# print(multiply(2,6)) #24

from functools import wraps

def decorator(num):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(func(*args, **kwargs))
        return wrapper
    return inner_decorator


# @decorator(5)
# def multiply(num1,num2):
#     return num1*num2

# # multiply(2,6)
# print(multiply.__name__)


"""
4)Создайте 3 декоратора, каждый из которых применяет к тексту определённый стиль:
выделение жирным <b>...</b> (декоратор make_bold)
курсив <i>...</i> (декоратор make_italic)
подчеркивание <u>...</u> (декоратор make_underline)
Далее создайте функцию hello которая будет возвращать текст
Hello world
примените к этой функции цепочку декораторов.
@make_bold
@make_italic
@make_underline
def hello():
    return 'Hello world'

print(hello())
Вывод должен быть:
<b><i><u>Hello world</u></i></b>
"""

# def make_bold(func):
#     def wrapper():
#         return f'<b>{func()}</b>'
#     return wrapper

# def make_underline(func):
#     def wrapper():
#         return f'<u>{func()}</u>'
#     return wrapper

# def make_italic(func):
#     def wrapper():
#         return f'<i>{func()}</i>'
#     return wrapper

# @make_underline
# @make_italic
# @make_bold
# def hello():
#     return 'Hello world'

# print(hello())


# def upper_case(func):
#     def wrapper():
#         a = func()
#         return a.upper()
#     return wrapper

# @upper_case
# def list1():
#     import random
#     word = input().split()
#     return random.choice(word)

# print(list1())

# def decorator(func):
#     def wrapper():
#         res = func()
#         return list(set(res))
#     return wrapper


# @decorator
# def numbers():
#     import random
#     return [ random.randint(10,50) for _ in range(10)]

#     # for i in range(100):
#     #     l.append(random.randint(10, 50))

# print(numbers())


# def decorator(func):
#     def wrapper():
#         login, password = func()
#         encrypted_login = ''.join((chr(ord(char)+1) for char in login))
#         encrypted_password = ''.join((chr(ord(char)+1) for char in password))
#         return encrypted_login, encrypted_password
#     return wrapper

# @decorator
# def log_pass():
#     login = input()
#     password = input()
#     return login, password

# print(log_pass())

# def decorator(func):
#     def wrapper():
#         with open('text.txt', 'w') as file:
#             file.write(func())
#         return func()
#     return wrapper

# @decorator
# def hello():
#     return "hello world"

# print(hello())


'''
Декоратор rotate_right, сдвигает все позиционные параметры функции по кругу вправо. Пример:

@rotate_right
def f(a, b, c):
    return a**b + c

print(f(1, 2, 3))   # получится 3**1 + 2 = 5'''

# def rotate_right(func):
#     def wrapper(*args):
#         new_args = (args[-1],) + args[:-1]
#         return func(*new_args)
#     return wrapper


# @rotate_right
# def f(a, b, c):
#     return a**b + c

# print(f(1,2,3))


'''
Декоратор log, перед вызовом функции выводит имя функции и её аргументы (известно, что аргументы только позиционные), потом вызывается функция, потом в той же строчке дописывает результат. '''

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         print(*args)
#         return func(*args, **kwargs)
#     return wrapper


# @log
# def my_func(x):
#     return x+1

# print(my_func(10))
