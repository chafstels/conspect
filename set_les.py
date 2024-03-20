"==========================Множества (set)======================="
# множество - это изменяемый, неупорядочный, итерируемый, неиндексируемый, предназаченный для хранения уникальных значений(нельзя хранить изменияемые типы данных), даже нельзя в tuple([1,2,3])

set1 = {1,2,3,'hello'}
print(set1)
set1 = {1,1,1,1,1,1,1,1}
print(set1)
set1 = {1,True,False,0}
print(set1)

'========================Методы множества======================'
set1 = {'a','b',3,4,5}

# add - добавляет элемент в множество
set1.add(66)
print(set1)

# pop - удаляет случайный элемент из set
popped = set1.pop()
print(popped)
print(set1)

# remove - удаляет элемент из set по значению, если не найдет значение выводит ошибку KeyError
set1.remove(3)
print(set1)

# difference - находит различия между множеством и другой коллекцией
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.difference(set2)) # (1, 2)
print(set2.difference(set1)) # (4, 5)

# symmetric_difference - находит только разные значения в множествах
print(set1.symmetric_difference(set2))

# intersection - выводит одинаковые значения коллекций
print(set1.intersection(set2))



'''
Шифр Цезаря
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут понять, как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.


В первой строке дается число n(1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.
Входные данные:
1
bwfusvfupdbftbs
Вывод:
avetruetocaesar
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
s = input()

for simvol in s:
    ind = alphabet.index(simvol)
    new_simvol = alphabet[ind-n]

    print(new_simvol, end='')


# n = int(input())
# s = input()
# list_ = []
# for i in s:
#     str1 =97 + (ord(i) - 97 + 26 -n) % 26
#     print(str1)
#     list_.append(chr(str1))

# print(list_)


alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=alfavit.lower()
print(a)
s=''
step=int(input('число сдвига'))
stroka=input('вести строку')
for i in stroka:
    index=a.find(i)
s=s+a[index+step]
print(s)
