# Grade 1. Этап 3: Задание 3
# ЗАМЕТКИ

import random, datetime, time

# Список (словарь) статусов Заметок
status_list = {0: 'новая',
               1: 'в процессе',
               2: 'выполнена'}


def input_date():  # Функция ввода даты с проверкой
    date_valid = False
    date_ = ''
    while not date_valid:
        date_ = input(
            'Введите дату в формате ДД-ММ-ГГГГ (или нажмите ENTER для ввода текущей даты) : ') or datetime.datetime.now().strftime(
            '%d-%m-%Y')
        try:
            year = int(date_[6:10])
            month = int(date_[3:5])
            day = int(date_[0:2])
            if year in range(1, 10000):  # год в пределах от 1 до 9999
                if month in (1, 3, 5, 7, 8, 10, 12):  # месяцы с 31 днём
                    if day in range(1, 32):
                        date_valid = True
                    else:
                        date_valid = False
                elif month in (4, 6, 9, 11):  # месяцы с 30 днями
                    if day in range(1, 31):
                        date_valid = True
                    else:
                        date_valid = False
                elif month == 2:  # февраль
                    if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):  # проверка високосного года
                        if day in range(1, 30):
                            date_valid = True
                        else:
                            date_valid = False
                    else:
                        if day in range(1, 29):
                            date_valid = True
                        else:
                            date_valid = False
                else:
                    print('Не правильно ввели номер месяца за пределами диапазона 01..12:', month)
                    date_valid = False
            else:
                print('Не правильно ввели номер года за пределами диапазона 0001..9999:', year)
                date_valid = False
            if not date_valid:
                print('Ошибка ввода даты!')
        except:
            print('Ошибка преобразования введённой даты. Используйте при вводе предложенный формат.')
    return date_


# Процедура вывода меню на экран с опросом выбора - возвращает номер выбранного пункта меню
def select_menu():
    while True:
        print('\n' * 100)
        print(' ' * 10, 'Меню работы с Заметками :', '\n')
        print('1. Добавить Заметку.')
        print('2. Просмотреть Заметки.')
        print('3. Найти и Удалить Заметки.')
        print('0. Выйти из программы.')
        try:
            selected = int(input('Введите номер меню :') or '0')
        except:
            print('Ошибка ввода числа!')
            time.sleep(3)
            continue
        if selected not in range(0, 4):
            print('Ошибка выбора! Необходимо выбирать из предложенных вариантов!')
            time.sleep(3)
            continue
        else:
            return selected


# Процедура ввода Заметки и добавления её в Список заметок
def create_note():
    print('=' * 10, 'Ввод данных новой заметки', '=' * 10, '\n')

    # Значения Заметки по умолчанию (структура словаря)
    note = {'username': 'Name',
            'title': ['Tit1', 'Tit2'],
            'content': 'Content',
            'status': 0,
            'created_date': '01-01-1999',
            'issue_date': '31-12-2024'}

    note['username'] = input('Введите имя пользователя (нажмите ENTER для случайной генерации): ') or 'Name № ' + str(
        random.randint(1, 100))
    # Пустой список Заголовков
    title_list = []
    while True:  # бесконечный цикл - ввод значений до прерывания цикла
        title = input('Введите заголовок (или оставьте пустым для завершения ввода)')
        if title == '':  # условие прерывания ввода Заголовков
            break
        elif title not in title_list:  # проверка отсутствия введённого Заголовка в списке Заголовков
            title_list.append(title)  # и добавление Заголовка в список
        else:  # когда не прошли проверку на задублированность Заголовка в списке
            print('Такой заголовок уже существует, попробуйте ввести другой!')
    note['title'] = title_list
    note['content'] = input(
        'Введите описание заметки (нажмите ENTER для случайной генерации): ') or 'Текст заметки №' + str(
        random.randint(1, 100))

    # 0 - ожидает, 1 - в работе, 2 - готово
    while True:
        status = input(
            f'Введите статус заметки (0 - {status_list[0]}, 1 - {status_list[1]}, 2 - {status_list[2]}, нажмите ENTER для статуса 0): ') or 0
        if status not in range(3):
            print('Пожалуйста, выберите статус из предложенных вариантов!')
        else:
            break
    note['status'] = status

    print('Введите дату создания заметки.')
    note['created_date'] = input_date()

    print('Введите дату актуальности заметки.')
    note['issue_date'] = input_date()

    return note


# Вывод одной Заметки
def show_one_note(note: dict):
    print('Имя пользователя:', note['username'])
    print('Заголовки Заметки :')
    for title in note['title']:
        print('- ', title)
    print('Описание заметки:', note['content'])
    print('Текущий статус заметки:', status_list[note['status']])
    print('Дата создания заметки:', note['created_date'][:-5])
    print('Дата актуальности заметки', note['issue_date'][:-5])
    input('Нажмите ENTER для продолжения.')


# Процедура вывода Заметок из Списка заметок
def display_notes(note_list: list):
    for note in note_list:
        print('===========Начало заметки===========')
        show_one_note(note)
        choise = input('Введите 0, если необходимо изменить Заметку или ENTER - для продолжения!')
        if choise == '0':
            note = update_note(note)

        # Проверка просроченности заметки
        # status_change = input('Требуется изменение статуса Заметки? (Д|Н) :')
        # if status_change in ['д', 'Д']:
        #     while True:
        #         status = input(
        #             'Введите новый статус заметки (0 - ожидает, 1 - в работе, 2 - готово, нажмите ENTER для статуса 0): ') or '0'
        #         if status not in ('0', '1', '2'):
        #             print('Пожалуйста, выберите статус из предложенных вариантов!')
        #         else:
        #             break
        #     note['status'] = status
    if note_list == []:
        print('Список Заметок пуст!')
        input('Нажмите ENTER для продолжения.')


# Процедура удаления Заметок по результатам поиска
def delete_notes(note_list: list):
    phrase = input(
        'Введите ключевую фразу для поиска (среди Имен и Заголовков) и удаления Заметок или "ENTER" для отмены ввода:')
    count_dn = 0  # Счётчик удалённых Заметок
    count_n = len(note_list)  # Счётчик номера просматриваемой Записи
    if phrase != '':
        for note in reversed(note_list):
            count_n = count_n - 1
            if phrase in note.get('username') or phrase in note.get('title'):
                temp_note = note_list.pop(count_n)
                print('Удалена Заметка :')
                show_one_note(temp_note)
                count_dn = count_dn + 1
                input('Нажмите ENTER для продолжения.')
        if count_dn > 0:
            print('Количество удалённых Заметок :', count_dn)
            input('Нажмите ENTER для продолжения.')
        else:
            print(f'Заметок с ключевой фразой : "{phrase}" не найдено.')
            input('Нажмите ENTER для продолжения.')


# Процедура обновления Заметки
def update_note(note):
    while True:
        while True:
            choise = input(
                'Выберите изменяемые поля Заметки (username, title, content, status, issue_date) или ENTER для продолжения: ')
            if choise in ('username', 'title', 'content', 'status', 'issue_date', ''):
                break
            else:
                print('Ошибка ввода! Вводите текст из предложенных вариантов.')
        if choise == 'username':
            note['username'] = input(
                'Введите НОВОЕ имя пользователя (нажмите ENTER для случайной генерации): ') or 'Name № ' + str(
                random.randint(1, 100))
        if choise == 'title':
            # Пустой список Заголовков
            title_list = []
            while True:  # бесконечный цикл - ввод значений до прерывания цикла
                title = input('Введите НОВЫЙ заголовок (или оставьте пустым для завершения ввода)')
                if title == '':  # условие прерывания ввода Заголовков
                    break
                elif title not in title_list:  # проверка отсутствия введённого Заголовка в списке Заголовков
                    title_list.append(title)  # и добавление Заголовка в список
                else:  # когда не прошли проверку на задублированность Заголовка в списке
                    print('Такой заголовок уже существует, попробуйте ввести другой!')
            note['title'] = title_list
        if choise == 'content':
            note['content'] = input(
                'Введите описание заметки (нажмите ENTER для случайной генерации): ') or 'Текст заметки №' + str(
                random.randint(1, 100))
        if choise == 'issue_date':
            print('Введите дату актуальности заметки.')
            note['issue_date'] = input_date()
        if choise == 'status':
            # 0 - ожидает, 1 - в работе, 2 - готово
            while True:
                status = input(
                    f'Введите статус заметки (0 - {status_list[0]}, 1 - {status_list[1]}, 2 - {status_list[2]}, нажмите ENTER для статуса 0): ') or 0
                if status not in range(3):
                    print('Пожалуйста, выберите статус из предложенных вариантов!')
                else:
                    break
            note['status'] = status
        else:
            break
    return note


# ОСНОВНАЯ ПРОГРАММА

# инициализация нового (пустого) списка Заметок
note_list = []
while True:
    menu = select_menu()
    if menu == 1:  # Добавить Заметку
        note_list.append(create_note())
    elif menu == 2:  # Вывести Заметки и предложить изменение Заметки
        display_notes(note_list)
    elif menu == 3:  # Удалить Заметки
        delete_notes(note_list)
    elif menu == 0:  # Выход из программы
        break
