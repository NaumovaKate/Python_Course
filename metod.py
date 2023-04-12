Методы и функции по работе со списками
Для управления элементами списки имеют целый ряд методов. Некоторые из них:

append(item):   добавляет элемент item в конец списка

pop([index]):   удаляет и возвращает элемент по индексу index. Если индекс не передан, 
                то просто удаляет последний элемент.

insert(index, item): добавляет элемент item в список по индексу index

extend(items):  добавляет набор элементов items в конец списка

remove(item):   удаляет элемент item. Удаляется только первое вхождение элемента. 
                Если элемент не найден, генерирует исключение ValueError

clear():        удаление всех элементов из списка

index(item):    возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

count(item): возвращает количество вхождений элемента item в список

sort([key]):    сортирует элементы. По умолчанию сортирует по возрастанию. 
                Но с помощью параметра key мы можем передать функцию сортировки.

reverse(): расставляет все элементы в списке в обратном порядке

copy(): копирует список

Кроме того, Python предоставляет ряд встроенных функций для работы со списками:

len(list): возвращает длину списка

sorted(list, [key]): возвращает отсортированный список

min(list): возвращает наименьший элемент списка

max(list): возвращает наибольший элемент списка


# a[a.index(b)] = remove(b, text)
    # with open('book.txt', 'w', encoding = 'utf-8') as f: #для вывода русского языка encoding = 'utf-8'
    # f.write('\n'.join(a))

# def del_memb(data):
#     ''' удаление по имени и фамилии'''
#     member = ' '.join(map(str.lower, [input('имя > '), input('фамилия > ')]))
#     for i,obj in enumerate(data):
#         if obj.identifier() == member:
#             data.pop(i)
#             savedata(data,name) # перезаписываем файл c новыми данными
#             print('удалено')
#             return
    
# def edited(text: str) -> str:
#     fio = input (' Введите новые фио: ')
#     num = input (' Введите новый номер телефона: ')
#     if len(fio) == 0:
#         fio = text.split(' |')[0]
#     if len(num) == 0:
#         fio = text.split(' |')[1]
#     return f'{fio} | {num}'

# def remove(text:str, remove_text: str) -> str:
#     if remove_text.isaipha():
#         num = text.split(' |')[1]
#         return f' | {num}'
#     else:
#         fio = text.split(' |')[0]
#         return f'{fio} | '








