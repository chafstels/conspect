'=========================Встроенные функции==================='
# map, filter, reduce, zip, enumerate, all, any

# zip - соединяет несколько последовательностей (получаем генератор, в котром элементы - tuple)
list1 = [1,2,3,4,5,6]
list2 = ['a','b','c']
list3 = [1.5]
zipped = zip(list1,list2,list3)
# print(list(zipped))

# for elem in zipped:
#     print(elem)

names = ['Alina', 'Anton', 'Mark']
ages = [14,16,17]
people = dict(zip(names,ages))
# print(people)
# for name, age in zip(names,ages):
#     print(name,age)


# enumerate - нумерует последовательность (по дефолту с 0) (тоже получаем генератор)
enumerated = enumerate('hello') #enumerate object
# print(next(enumerated))
# print(next(enumerated))
# print(next(enumerated))
# print(next(enumerated))
# print(next(enumerated))
names = ['Ada', 'Bob', 'Max']
enum_names = list(enumerate(names, start=1))
# print(enum_names)


# map - функция высшего порядка, принимает другую функцию и итерируемый обьект, выполняет заданную функцию на каждый элемент последовательности

# nums = [1,2,3,4,5]
# n = list(map(lambda x: x*10, nums))
# print(n)

text = list(map(int, input('Введите числа через пробел').split()))
print(sum(text),'сумма чисел')
# num = [1,2,3]
# num2 = [4,5,9]
# num3 = [6,7,8]
# sums = list(map(lambda n1,n2,n3: n1+n2+n3, num, num2,num3))
# print(sums)


# filter - функция высшего порядка, возвращающий генератор, с элементами прошедщими фильтр (какое-то условие), принимает функции и последовательность(func, iterable)

people = [
    ('Jonhy', 22),
    ('Adriana', 14),
    ('Adam', 12),
    ('Mark', 18),
    ('Sam', 11),
]
# def is_adult(person):
#     return person[1] >= 18
# print(list(filter(lambda p: p[1]>=18, people)))

list_ = [3,-5,0,10,-3]
filtered = list(filter(lambda i: i>0, list_))
print(filtered)

# reduce - функция высшего порядка, котроая принимает другую функцию и последовательность, возрашает один элемент
from functools import reduce

list_ = [1,2,3,4,5]
# print(reduce(lambda x,y: x+y, list_))

string = 'hello'
# print(reduce(lambda x,y: x + '|' + y, string))

users = [
    {'name':'kurmajan', 'age': 13},
    {'name': 'Anton', 'age': 20},
    {'name': 'user1', 'age': 33},
    {'name': 'user2', 'age': 21},
]
# print(reduce(lambda x,y: x if x['age']>y['age'] else y,  users)['name'])


# all - функция которая принимает итерабельный обьект, и возращает True иначе False
print(all([True,1, {'name':'users'}]))
print(all(['', True, True]))

# any - функция которая принимает последовательность, и возращает True, если хотя бы один элемент был истинной(True), иначе False
print(any([False,False,False]))
print(any([1,False,False]))
