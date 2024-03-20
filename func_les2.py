# '================================Функции====================='
# # Функции - именованный блок кода, который может принимать аргументы и возращать результат

# # Параметры функции - это переменные, которые будет принимать ваша функция, для того чтобы вы смогли работать с данными, которые попадают в вашу функцию
# # Аргументы - данные, которые мы передаем для параметров при вызове функции.
# # return(по умолчанию возращает None) - оператор, который нужен, чтобы функция возращала результат
# # string_ = '1234abs'
# # def our_len(str1):
# #     count = 0
# #     for _ in str1:
# #         count += 1
# #     return count

# # print(our_len(string_))

# '================================Виды параметров=========================='
# # Обязательные
# # Необязательные:
#     # с дефолтом (со значением по умолчанию)
#     # args (все позиционные аргументы, которые не попали в обязательные и с дефолтом)
#     # kwargs (все лишние именованные параметры)
# def greet(*args):
#     for name in args:
#         print(f'Привет {name}')
# def my_greet(**kwargs):
#     name = kwargs.get('name')
#     age = kwargs.get('age')
#     print(f'Privet {name}, your age == {age}')
# my_greet(age=12, name='ada')
# '==============================Виды аргументов============================'
# # 1. Позиционные (по позиции)
# # 2. Именованные (по названию (параметр=значение))

# def add_10(num1, num2=10):
#     """Складывает два числа"""
#     return num1 + num2
# print(add_10(5))
# print(add_10(1, 2))
# print(add_10(num1=2, num2=2))

# '''
# Чем хороши функции?
# 1. Помогает избегать повторения одинковых фрагментов кода
# Функции соблюдают принцип DRY (don't repeat yourself)
# 2. Упрощают внесение изменений в повторяемых блоках кода
# 3. Позваляет разбить задачу на подзадачи
# '''

# '===================================Lambda============================='
# # lamda - это анонимная функция, которая записавыается в одну строку
# lambda_func = lambda x: x**2
# print(lambda_func(5))
# def func(x):
#     return x**2
# print(func(5))

# calc = {
#     '+': lambda n1, n2: n1+n2,
#     '-': lambda n1, n2: n1-n2,
#     '*': lambda n1, n2: n1*n2,
#     '/': lambda n1, n2: n1/n2,
#     '//': lambda n1, n2: n1//n2,
#     '%': lambda n1, n2: n1%n2,
# }
# def main():
#     num1 = int(input('your number_1'))
#     num2 = int(input('your number_2'))
#     operator = input('your operator')
#     func_ = calc[operator]
#     res = func_(num1,num2)
#     return res
# # print(main())
# '==================================Register, Login==========================='
# database = [
#     {'name': 'user1', 'password':12345},
#     {'name': 'user2', 'password':12345},
#     {'name': 'user3', 'password':12345},
#     {'name': 'user4', 'password':12345},
# ]

# def in_database(name):
#     for user in database:
#         if user['name'] == name:
#             return True
#     return False

# def register_database(name, password1, password2):
#     if in_database(name):
#         return 'Юзер с таким именем уже существует'
#     if password1 != password2:
#         return 'Пароли не совпали'
#     user = {'name': name, 'password': password1}
#     database.append(user)
#     return 'Вы успешно зарегистрировались'

# def login_database(name, password):
#     if not in_database(name):
#         return 'Пользователь не найден'
#     for user in database:
#         if user['name'] == name:
#             if user['password'] != password:
#                 return 'Пароль не верный'
#     return 'Вы успешно вошли'

# def main():
#     print('Добро пожаловать')
#     while True:
#         action = input('Введите что-то из этого --> rеgister:1, login:2, exit:3  ')
#         if action == '3':
#             break
#         elif action== '1':
#             name = input('введите имя пользователя: ')
#             password1 = input('введите пароль: ')
#             password2 = input('введите снова пароль: ')
#             print(register_database(name, password1, password2))
#         elif action == '2':
#             name = input('введите имя пользователя: ')
#             password1 = input('введите пароль: ')
#             print(login_database(name, password1))
#         else:
#             print('Не корректный выбор')
# # main()


# '''
# Напишите функцию count_letter(text, letter), которая принимает два параметра:
# text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
# letter – буква, количество которой мы должны посчитать в text.
# '''
# def count_letter(text,letter):
#     print(text.count(letter))
# text = input()
# letter = input()
# count_letter(text,letter)


# def naob(spisok):
#     half = len(spisok) // 2
#     print('Оригинал: ', spisok)
#     spisok[:half] = reversed(spisok[:half])
#     spisok[half:] = reversed(spisok[half:])
#     print(spisok)

# list1 = ['python', 'Django', '3.11', '4','5']
# naob(list1)

# def gen_number():
#     import random
#     prefix = '0888'
#     number = prefix + ''.join(random.choice('568034') for _ in range(6))
#     return number

# print(gen_number())

# def add(x,y):
#     return x+y
# def substract(x,y):
#     return x-y
# def myltiply(x,y):
#     return x*y
# def divede(x,y):
#     return x/y

# def count_letters(sentence):
#     count = 0
#     letters = sum([1 for i in sentence if i.isalpha()])
#     for _ in sentence:
#         count += 1
#     return count, letters


# print(count_letters(input()))



'''
Напишите функцию print_initials(name, surname, middlename), которая принимает три параметра:

name – имя человека;
surname – фамилия человека;
middlename– отчество человека;
а затем выводит на печать фамилию и инициалы в определенном формате (первая буква фамилии должна стать заглавной, все остальные строчные; в имени и отчестве остаются только по одной букве в верхнем регистре).'''

# Мария Ивановна Филлиповна  Ивановна М.Ф.

# def print_initials(name, surname, middlename):
#     print(f'{surname.title()} {name[0].upper()}. {middlename[0].upper()}.')

# print_initials('мария', "ивановна", "филлиповна")

