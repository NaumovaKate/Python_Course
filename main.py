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

