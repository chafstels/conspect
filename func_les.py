'======================================Функция================================'
# Функция - это именнованный блок кода, которая вызывается множество раз в других частях программы
# Они создаются благодаря ключевому слову def
# При наименовании функции нужно придерживаться стилю Snake_case

# def name_of_functions(a, b параметры сколько угодно):
#     <body> код, который имеет некую логику
#     return оператор, который возращает результат выполнения функции




# def sum_our():
#     number_1 = int(input("Введите первое число: "))
#     number_2 = int(input("Введите второе число: "))
#     return f'{number_1} + {number_2} = {number_1 + number_2}'

# print(sum_our())

'''Всеми любимая программа «hello world». Создайте функцию с именем say_hello_world , которая принимает на вход имя человека в виде строки и печатает фразу «{name} говорит hello world!»
'''
# def say_hello_world():
#     name = input('Vvedite svoe name')
#     return f'{name} говорит hello world!'
# print(say_hello_world())

'''
Напишите функцию summa_n, которая принимает одно целое положительное t число и находит сумму всех чисел от 1 до t включительно. Программа должна распечатать сообщение

"Я знаю, что сумма чисел от 1 до {t} равна {S}", где в качестве t и S вам необходимо подставить значения '''
# def summa_n():
#     t = int(input())
#     S = sum([i for i in range(1, t+1)])
#     return f'Я знаю, что сумма чисел от 1 до {t} равна {S}'
# print(summa_n())


'''
Напишите функцию exponentiation, которая принимает на вход целое число и выводит на экран через пробел квадрат и куб этого числа. '''
# def exponentiation():
#     number = int(input())
#     return (number ** 2, number **3)
# print(*exponentiation())

'''
Напишите функцию sum_num для суммирования всех цифр строки.
Функция должна принимать строку, суммировать все ее символы, которые являются цифрами,
и в качестве ответа выводить найденную сумму.'''

# def sum_num():
#     stroka = input()
#     result = sum([int(num) for num in stroka if num.isdigit()])
#     return result
# print(sum_num())


'''
Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

Сложным паролем будет считаться комбинация символов, в которой :

Есть хотя бы 3 цифры
Есть хотя бы одна заглавная буква
Есть хотя бы один символ из следующего набора "!@#$%*"
Общая длина не менее 10 символов
Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"'''

def check_password(password):
    a = sum([1 for num in password if num.isdigit()])
    b = sum([1 for upper in password if upper.isupper()]) #sum[1,1,1] # 3
    c = sum([1 for symvol in password if symvol in '!@#$%*'])
    len_our = len(password) >= 10
    if a >=3 and b>=1 and c>=1 and len_our:
        return 'Perfect password'
    else:
        return 'Easy peasy'

print(check_password('qwerty1234A!'))


# def say():
#     a = 3
#     b = 2
#     c = a+ b
#     print('hello', c)
#     return None
# print(say())

# def numbers():
#     set1 = min({int(value) for value in input().split()})
#     return set1

# print(numbers())

# def credit_cost():
#     credit = int(input())
#     if credit < 100_000:
#         print('Сумма займа должна быть не менее 100000')
#     else:
#         procent = 7.89
#         pereplata = round(credit * (procent/100),2)
#         print(pereplata)
# credit_cost()

# def num_split():
#     stroka = input()
#     numbers =''.join([i for i in stroka if i.isdigit()])
#     if numbers:
#         integer = int(numbers)
#         print(integer)
#     else:
#         print("Цифр в строке не было")
# num_split()

# def calculate_days(user_months, user_years):
#     total_days = user_months * 30 + user_years * 365
#     return total_days

# user_months = int(input())
# user_years = int(input())

# print(calculate_days(user_months, user_years))

def dict_num():
    numbers = {i:i**3 for i in range(1,11)}
    return numbers
# print(dict_num())
# print(dir(dict))

# def calculate_sum():
#     total_sum = sum(range(1,51))
#     return total_sum

# print(calculate_sum())
