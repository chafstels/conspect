'=========================Циклы=========================='
# Циклы - это блок кода, который отрабатывается несколько раз
# 1. For - цикл, который работает до конца итерируемого обьекта
# 2. While - цикл, который работает пока условие истина(True)

'FOR'
# list_  = [1,2,3,4,5,True,False,None, [4,3,2,1]]

# for i in list_:
#     print(i)

# for i in 'Barcelona':
#     print(i)

# for i in range(0, 101, 2):
#     print(i)

# 'WHILE'
# count = 0
# while count < 10:
#     print('Hello world')
#     count += 1
#     print(count)


'==========================break and continue======================='
# break - оператор, который останавливает цикл (выходит из цикла)
# continue - оператор, который переходит к следующей итерации

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

# for i in range(10):
#     print(i)
#     break

# for i in range(10):
#     if i == 3:
#         break
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# for i in range(1,11):
#     print(i)

# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# for i in range(0,21,2):
#     print(i)


# count = 1
# while count <= 100:
#     if count % 3 == 0:
#         print(count, count // 3)
#     count += 1

for i in range(1,101):
    if i % 3 == 0:
        print(i, i // 3)
