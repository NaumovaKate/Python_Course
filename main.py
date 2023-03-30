# Задача 1.
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
# решение:
# n = int(input())
# m = int(input())
# # a= int(m / n)
# # # d= a+ m%n
# # print(a + int(bool(m % n)))
# print(math.ceil(m/n))

# Задача 3
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
# решение:
# k1=25
# k2=28
# k3=22

# part1=k1//2 + k1%2
# part2=k2//2 + k2%2
# part3=k3//2 + k3%2
# pppart=part1+part2+part3
# print(part1, part2, part3)

# Задача 5
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
#  а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
# Он хочет определить, сколько всего вагонов в электричке. 
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

# Input: 3 4(ввод на разных строках)
# Output: 6
# Решение:
# i = int(input())
# j = int(input())
# if i == j:
#     print ("нужна доп.инфа")
# else:
#     print (i+j-1)


# Задача 7
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, 
# но не кратен 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# n = int(input())
# if n%4==0 and n%100!=0 or n%400==0:
#     print("yes")
# else:
#     print("no")

# Шахматный конь ходит буквой "Г" - на две клетки по вертикали в любом направлении 
# и на одну клетку по горизонтали, или наоборот. 
# Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки
# на вторую одним ходом. В случае, если хотя бы одно из введенных 
# не лежит в диапазоне от 1 до 8, выведите строку "Ошибка!".

# x1=int(input())
# x2=int(input())
# y1=int(input())
# y2=int(input())
# # # diagonal_x = abs(x1 - x2)
# # diagonal_y = abs(y1 - y2)
# # if diagonal_x == 1 and diagonal_y == 2 or diagonal_x == 2 and diagonal_y == 1:
# #     print('YES')
# # else:
# #     print('NO')
# решение2
# if not 0<(x1)<9 and not 0<(x2)<9 and not 0<(y1)<9 and not 0<(y2)<9 :
#   print("ошибка")
# elif (abs(x2 - x1) == 1 or abs(x2 - x1) == 2) and (abs(y2 - y1) == 1 or abs(y2 - y1) == 2):
#   print("YES")
# else:
#   print("NO")
# решение3:
# if not(1 <= x1 <= 8) or not (1 <= y1 <= 8) or not (1 <= x2 <= 8) or not (1 <= y2 <= 8):
#     print("ошибка")
# elif abs(x2-x1)==2 and abs(y2-y1)==1 and abs(x2-x1)==1 and abs(y2-y1)==2:
#     print("такой ход возможен")
# else:
#     print("такой ход невозможен")

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует.
# решение1:
# a, b, c = int(input()), int(input()), int(input())
# if a>=c+b or c>=a+b or b>=c+a:
#    print("треугольник существует")
# else:
#    print("такой треугольник не существует")

# a = 1
# while a < 5:
#     a += 1
#     if a == 3:
#         break
# print(a) # 2

# a = 1
# while a < 5:
#     a += 1
#     if a == 3:
#         continue
# print(a)  # 2, 4, 5


# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1

# n = int(input())
# print('Длина числа равна', len(str(n)))


# for i in range(14):  # равносильно инструкции for i in 0, 1, 2, 3:
#     # здесь можно выполнять циклические действия
#     print(i)
#     print(i ** 2)
#     print(" ")
# # цикл закончился, поскольку закончился блок с отступом
# print('Конец цикла')


# СЕМИНАР 2 от 13.03.23
# Задача 9
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input:       5
# Output:    120

# Решение:
# n = int(input('введите число: '))
# result = 1
# count = 1
# while count <= n:
#     result *= count
#     count += 1
# print(result)

# Задача 11
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A.Если А не является числом Фибоначчи, выведите число -1.
# Input:     5
# Output:  6
# Последовательность Фибоначчи определяется так:
# F(0)=0, F(1)=1, F(n)=F(n-1) + F(n-2)

# Решение:
# a = int(input("Номер элемента ряда Фибоначчи: "))
# if a == 0:
#     print(0)
# else:
#     fib_prev, fib_next = 0, 1
#     n = 1
#     while fib_next <= a:
#         if fib_next == a:
#             print(n)
#             break
#         fib_prev, fib_next = fib_next, fib_prev + fib_next
#         n += 1
#     else:
#         print(-1)

# n = int(input("Номер элемента ряда Фибоначчи: "))
# F1 = 1
# F2 = 1
# i = 0
# while i < n - 2:
#     F_sum = F1 + F2
#     F1 = F2
#     F2 = F_sum
#     i = i + 1
# print ("Значение этого элемента: ", F2)

# Задача 13
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это 
# самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

# SEMINAR 3
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list_11 = set(list_1)
# print(len(list_11))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# list_2 = [1, 2, 3, 4, 5]
# k = 2
# list_3 = [0]*len(list_2)
# for i in range(len(list_2)):
#     list_3[i] = list_2[(i-k)]
# print(list_3)

# №21. Напишите программу для печати всех уникальных  значений в словаре.  
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. 
# Пользователь его не вводит

# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# list_4 = []

# for v in dictionary:
#     for value in v.values():
#         list_4.append(value.strip()) 

# print(*set(list_4))

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 

# count = 0
# list_5 = [0, -1, 5, 2, 3, 5, 6, 2]
# for i in range(len(list_5)-1):
#     if list_5[i] < list_5[i+1]:
#         count += 1
# print(count)




# SEMINAR 4

# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# my_str = my_str = 'a a a b c a a d c d d'

# Этот вариант, если нужно split применить обязательно

# print('Этот вариант, если нужно split применить обязательно')

# my_list = my_str.split()
# print(my_list)
# for i in range(len(my_list)):
# if my_list.count(my_list[(i + 1) * -1]) > 1:
# my_list[(i + 1) * -1] += f'_{str(my_list.count(my_list[(i + 1) * -1]) - 1)}'

# print(my_list)


# # Этот вариант больше похож на пример в задании

# print('Этот вариант больше похож на пример в задании')

# print(my_str)
# new_str = ''

# for i in range(len(my_str)):
# if my_str[i] != ' ' and my_str.count(my_str[i], 0, i) > 0:
# new_str += f'{my_str[i]}_{my_str.count(my_str[i], 0, i)}'
# else:
# new_str += my_str[i]

# print(new_str)

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# text_ = "She sells sea shells on the sea shore The shells that she sells are \
# sea shells I'm sure.So So if she sells sea shells on the sea shore I'm sure that \
# the shells are sea shore shells"
# print(text_)

# text_ = text_.replace(".", " ").split()
# print(text_)

# text_ = [i.upper() for i in text_]

# set_text = set(text_)

# print(set_text)
# print(f'{len(set_text)}')

# решение 2
# a = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower()
# a = a.replace(".", " ")
# res = len(set(a.split()))
# print(res)



# “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”.

# n = int(input())
# max_ = n
# while n != 0:
#     if n > max_:
#         max_ = n
#     n = int(input())
# print(f'{max_ = }')


# SEMINAR 6

# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# num_1 = int(input('Введите количество элементов в первом массиве: '))
# list_1 = list()

# решение 1:

# for i in range(num_1):
#     x = int(input('введите элемент массива: '))
#     list_1.append(x)
# print(list_1)
# num_2 = int(input('Введите количество элементов во втором массиве: '))
# list_2 = list()

# for i in range(num_2):
#     x = int(input('введите элемент массива: '))
#     list_2.append(x)
# print(list_2)
# list_new = list()

# def result (list_1, list_2, list_new):
#     for i in list_1:
#         if i not in list_2:
#             list_new.append(i)
# # for j in list_2:
# # if i == j:
# # list_new.append(i)

#     return list_new

# print(result(list_1, list_2, list_new))


# решение 2:
# a = [int(input()) for i in range(int(input()))]
# b = [int(input()) for j in range(int(input()))]
# c = [i for i in a if i not in b]
# c_1 = []
# for i in a:
#     if i not in b:
#         c_1.append(i)
# print(c, c_1)


# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# решение 1:

# num_1 = int(input('Введите количество элементов в первом массиве: '))
# list = list()

# for i in range(num_1):
#     x = int(input('введите элемент массива: '))
#     list.append(x)  
# print(list)

# count = 0
# # 0 1 2 3 4
# def summ (list, count): # [ 6 5 1 5 1]
#     for i in range(1, len(list)-1):
#         if list[i-1]<list[i]>list[i+1]:
#             count +=1

#     return count

# print(summ(list, count))


# num_1 = int(input('Введите количество элементов в первом массиве: '))
# list = list()

# for i in range(num_1):
#     x = int(input('введите элемент массива: '))
#     list.append(x)
# print(list)

# count = 0
# # 0 1 2 3 4 5 6
# def para (list, count): # [ 1 2 3 2 3 2 2]
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] == list[j]:
#                 count +=1
#         return count

# print(para(list, count))

#  решение 2:
# a = [int(input()) for i in range (int(input()))]
# count = 0
# for i in range(1, len(a) - 1):
#     if a[i - 1] < a[i] > a[i + 1]:
#         count+=1
# print(count)
