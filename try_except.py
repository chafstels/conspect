'===================================Try Except================================='
# Исключения - это обьекты которые прерывают работу кода, если не были обработаны(связаны с логикой самой программы)
# print(10+'str') # TypeError
# Ошибки - обьекты, которые прерывают работу и их нужно обработать(связаны по большей части с разработчиком)
# print( # SyntaxError

SyntaxError
# исключение, которое выходит, когда в коде допущена синтаксическая ошибка
# '''
'SyntaxError: unterminated triple-quoted string literal (detected at line 9)'
# когда мы не закрыли скобку либо кавычки

# a =
'SyntaxError: invalid syntax'

NameError
# исключение, которые выходит когда мы обращаемся к несущестующей переменной
name = 'Anton'
# print(name1)
'''NameError: name 'name1' is not defined. Did you mean: 'name'?'''

IndexError
# исключение, которые выходит когда мы обращаемся по несуществующему индексу
list_=[1,2,3]
# print(list_[6])
'IndexError: list index out of range'
# list_.pop(5)

KeyError
# исключение, которое выходит когда мы обращаемся по несуществующему ключу
dict_ = {'a':1}
# print(dict_['b'])
"KeyError: 'b'"
# dict_.pop('b')
dict_.get('b')

ValueError
# исключение, когда мы передаем в функцию не коректный для нее тип данных
# когда мы распаковываем итерируемый обьект на несколько переменных и количество переменных не  совпадает с кол-вом элементов внутри итерируемого обьекта

# int('12d')
"ValueError: invalid literal for int() with base 10: '12d'"
# a,b,c=[1,2]
'ValueError: not enough values to unpack (expected 3, got 2)'

TypeError
# когда мы пытаемся использовать методы не свойственные какому-то типу данных
# или когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функции

# for i in 123456:
#     ...
"TypeError: 'int' object is not iterable"

# 5 + '5'
"TypeError: unsupported operand type(s) for +: 'int' and 'str'"

# {[1,2,3]: 'gel'}
"TypeError: unhashable type: 'list'"

# input('hello !', 'world')
'TypeError: input expected at most 1 argument, got 2'

ZeroDivisionError
#выходит при деление на ноль
# 5/0
'ZeroDivisionError: division by zero'

AttributeError
# выходит, когда мы обращаемся к несуществующему методу или атрибуту обьекта(типа данных)

# [].replace()
"AttributeError: 'list' object has no attribute 'replace'"

IndentationError
# выходит, когда мы не правильно используем отступы

    # a=5
'IndentationError: unexpected indent'

# for i in 'asd':
# print(i)
"IndentationError: expected an indented block after 'for' statement on line 79"


Exception
# исключение, которое мы сами создали, чтобы его вызвать
'Вызов исключений raise'
# raise Exception('ошибки')

'===============================Обработка исключений============================'
# Чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except и обрабатывать вызванное исключение

# try:
#     #код, который возможно вызовет ошибку
#     num = int(input("Введите число: "))
# except ValueError: #исключение, которое может возникнуть
#     print("Вы ввели не число!") # код который отработает только если ошибка вызвалась
# else: # код который отработает только елси никакая ошибка не вышла
#     print("Вы ввели число", num)
# finally: # код который отработает в любом случае
#     print('До свидание!')

# try:
#     while True:
#         num=int(input())
#         num2 = int(input())
#         print(num/num2)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя!")
# except ValueError:
#     print('Введите число')


# try:
#     num = int(input('Vvedite num'))
#     if num == 0:
#         raise ValueError
# except (SyntaxError, NameError, ValueError):
#     print('Вышла одна из ошибок')

# try:
#     raise Exception
# except:
#     print('Любая ошибка')

# try:
#     raise TypeError('type error')
# except Exception as error:
#     print(error)


"""
1) Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е. соединение, строк. В остальных случаях введенные числа суммируются.
"""
# try:
#     a = input()
#     b = input()
#     print(int(a)+int(b))
# except:
#     print(a+b)


"""
2) Создайте словарь, в котором ключами будут ID, а значениями - пользовательские имена (username). Напишите программу, которая запрашивает у вас юзернейм и выдает ID этого юзера. Если же данного юзернейма нет, то программа выдает вам исключение, которое содержит следующее сообщение:”Введенного юзера нет в базе данных”. Если исключение не выявилось (т.е. Данный юзернейм существует) программа должна приветствовать юзера по юзернейму. Также в любом случае программа должна в конце выдавать сообщение: “Спасибо!”
"""
# users = ['anton', 'dastan', 'jasmina']
# dict_ = {'ID_'+str(k+1): users[k] for k in range(len(users))}
# print(dict_)
# try:
#     user_name = input("Press username: ").lower()
#     for key, values in dict_.items():
#         if values == user_name:
#             id_user=key
#             print(key)
#     if not (user_name in users):
#         raise NameError
# except:
#     print('Введеного юзера нет в базе данных')
# else:
#     print(f'Приветствую, {dict_[id_user].title()}')
# finally:
#     print('Cпасибо!')
"""
3) Напишите программу, которая будет запрашивать ваш возраст. Если пользователь вводит отрицательное число либо 0, программа должна выдать исключение: “Ваш возраст должен быть больше 0 ”.
"""
# try:
#     age = int(input('Vvedite your age '))
#     if age> 0:
#         print(age)
#     else:
#         raise Exception
# except:
#     print('Ваш возраст должен быть больше нуля')

"""
5) Создайте функцию divide() которая должна принимать 2 числа и возвращать результат их деления.
"""
# def divide():
#     try:
#         num1 = int(input())
#         num2 = int(input())
#         print(f'{num1} / {num2} = {num1/num2}')
#     except ValueError:
#         print('Введите число!')
#         divide
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#         divide()

# divide()

# """
# 1) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
# """
# users = ['anton', 'user1', 'user2', 'IvanovIvan']

# from functools import reduce

# len_name = reduce(lambda x,y: x if len(x)>len(y) else y, users)
# print(len_name)

# try:
#     raise TypeError
# except TypeError:
#     print('Вышла ошибка типов')

# with open('text.txt', 'r') as file:
#     content = file.read().strip()
#     numbers = []
#     for i in content:
#         try:
#             file = int(i)
#             numbers.append(file)
#         except:
#             print('Невозможно преобразовать в целочисленное')
# print(numbers)
# try:
#     with open('text.txt', 'r') as file:
#         content = file.read()
#         numbers = [int(char) for char in content if char.isdigit()]
# except FileNotFoundError:
#     print('File not found')
# except ValueError as e:
#     print('Error converting to integer', e)

# try:
#     with open('text.txt', 'r') as file:
#         f = file.read()
#         if 'w' in f:
#             print('В тексте есть буква w')
#         else:
#             print("В тексте нет буквы")
# except FileNotFoundError:
#     print('Введите существующий файл')
# try:
#     name = input()
#     country = input()
#     birth_day = int(input())

#     with open('text.txt', 'w') as file:
#         file.write(f'Name: {name}\nCountry: {country}\nBirtth day: {birth_day}')
#     print('OK')
# except ValueError as e:
#     print('Error: ', e )

# def name_age(*args, **kwargs):
#     name = kwargs['name']
#     age = kwargs['age']
#     print(f'Name: {name}, Age: {age}')

# try:
#     name_age(name='asd', age='12')
#     name_age(name='asd')
# except KeyError:
#         print(f'Keyerror: такого ключа нету')

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multi(a,b):
    return a * b
def divide(a,b):
    return a / b

# try:
#     add(1,2)
#     subtract(1,2)
#     multi(1,2)
#     divide(1,2)
# except ValueError:
#     print('Введите число')
# except ZeroDivisionError:
#     print('деление на ноль нельзя')

# l1 = [2,3,0,4,1]
# l2 = [10,20,30,40,50]
# result = []
# try:
#     for index in l1:
#         elem = l2[index]
#         result.append(elem)
# except:
#     print('Ошибка индексов')
# print(result)
