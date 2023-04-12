def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding = 'utf-8') as f: #для вывода русского языка encoding = 'utf-8'
        print(f.read())

def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f: #для вывода русского языка encoding = 'utf-8'
        f.write(f'\n{fio} | {tel_number}') #\n для переноса на новую строку
    print('Успешно!')

def find_data() -> None:
     '''Осуществляет поиск по справочнику'''
     data = input('Введите данные для поиска: ')
     with open('book.txt', 'r', encoding = 'utf-8') as f: #для вывода русского языка encoding = 'utf-8'
        tel_book = f.read()
        print('Результаты поиска: ')
        print(search(tel_book, data))


def search(book: str, info: str) -> str:
    '''Находит в строке запись по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


def delete_data() -> None:
    '''Удаляет данные в строке записи по поиску'''
    with open('book.txt', 'r', encoding = 'utf-8') as f: #для вывода русского языка encoding = 'utf-8'
        tel_book = f.read()
    a = tel_book.split('\n')
    print(a)
    text = input('Кого удаляем: ')
    b = (search(tel_book, text))
    print('Удалено!')
    