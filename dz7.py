# Задача 34: 

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 

# Вывод:
# Парам пам-пам

# решение:

# def song(str):
#     str = str.split()
#     list = []
#     for word in str:
#         result = 0
#         for i in word:
#             if i in "а е ё и о у ы э ю я":
#                 result += 1
#         list.append(result)
#     return len(list) == list.count(list[0])

# print("Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам")

# str = input()
# if song(str):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 

# решение 1:

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1): 
#             if i != 1 and j != 1: 
#                 print(operation(j, i), end="\t") 
#             elif i == 1: 
#                 print(j, end ="\t") 
#             else: 
#                 print(i, end ="\t") 
#         print()

# print_operation_table(lambda x, y: x * y)



# решение преподавателя:

# def show_table(table: list[list[int]]) -> None:
# # '''Просто красиво печает матрицу)'''
#     print('\n'.join('\t'.join(map(str, row)) for row in table))

# def print_operation_table(oper: callable,
#                         num_columns: int = 4,
#                         num_rows: int = 4) -> None:
# # '''Выводит таблицу для чисел с заданной операцией oper,
# # числом столбцов num_columns и строк num_rows'''
#     table = [list(range(i, i+num_columns)) for i in range(1, num_rows+1)]
# # show_table(table)
#     for i in range(1, len(table)):
#         for j in range(1, len(table[i])):
#             table[i][j] = oper(table[i][0], table[0][j])
#     show_table(table)

# oper = lambda x, y: x * y
# n = 4
# m = 5
# print_operation_table(oper, n, m)