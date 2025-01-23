# Grade 1. Этап 3: Финальное
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
        print('3. Просмотреть Заметки с возможностью из изменения.')
        print('4. Найти и Удалить Заметки.')
        print('5. Найти и показать Заметки.')
        print('0. Выйти из программы.')
        try:
            selected = int(input('Введите номер меню : ') or 0)
        except:
            print('Ошибка ввода числа!')
            time.sleep(3)
            continue
        if selected not in range(0, 6):
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
        title = input('Введите заголовок (или оставьте пустым для завершения ввода): ')
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
        try:
            status = int(input(
                f'Введите статус заметки (0 - {status_list[0]}, 1 - {status_list[1]}, 2 - {status_list[2]}, нажмите ENTER для статуса 0): ') or 0)
        except:
            print('Пожалуйста, введите статус из предложенных вариантов в виде числа!')
            continue

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
    print('Имя пользователя : ', note['username'])
    print('Заголовки Заметки :')
    for title in note['title']:
        print('- ', title)
    print('Описание заметки : ', note['content'])
    print('Текущий статус заметки : ', status_list[note['status']])
    print('Дата создания заметки : ', note['created_date'][:-5])
    print('Дата актуальности заметки : ', note['issue_date'][:-5])


# Процедура вывода Заметок из Списка заметок
def display_notes(note_list: list, do_pause=False, do_change=False, do_status=False):
    for note in note_list:
        print('===========Начало заметки===========')
        show_one_note(note)

        # Запрос на паузы между Заметками при выводе
        if do_pause:
            input('Нажмите ENTER для продолжения.')

        # Запрос на изменение Заметок
        if do_change:
            choise = input('Введите 0, если необходимо изменить Заметку или ENTER - для продолжения! : ')
            if choise == '0':
                note = update_note(note)

        # Проверка просроченности заметки
        if do_status:
            status_change = input('Требуется изменение статуса Заметки? (Д|Н) :')
            if status_change in ['д', 'Д']:
                while True:
                    try:
                        status = int(input(
                            'Введите новый статус заметки (0 - ожидает, 1 - в работе, 2 - готово, нажмите ENTER для статуса 0): ') or 0)
                        if status not in range(3):
                            print('Пожалуйста, выберите статус из предложенных вариантов!')
                        else:
                            break
                    except:
                        print('Пожалуйста, введите число!')
            note['status'] = status

    if note_list == []:
        print('Список Заметок пуст!')
        input('Нажмите ENTER для продолжения.')


# Процедура удаления Заметок по результатам поиска
def delete_notes(note_list: list):
    phrase = input(
        'Введите ключевую фразу для поиска (среди Имен и Заголовков) и удаления Заметок или "ENTER" для отмены ввода : ')
    count_dn = 0  # Счётчик удалённых Заметок
    count_n = len(note_list)  # Счётчик номера просматриваемой Записи
    if phrase != '':
        for note in reversed(note_list):
            count_n = count_n - 1
            if phrase.lower() in note.get('username').lower():
                temp_note = note_list.pop(count_n)
                print('Удалена Заметка : ')
                show_one_note(temp_note)
                count_dn = count_dn + 1
                input('Нажмите ENTER для продолжения.')
            else:
                for title in note.get('title'):
                    if phrase.lower() in title.lower():
                        temp_note = note_list.pop(count_n)
                        print('Удалена Заметка : ')
                        show_one_note(temp_note)
                        count_dn = count_dn + 1
                        input('Нажмите ENTER для продолжения.')
        if count_dn > 0:
            print('Количество удалённых Заметок : ', count_dn)
            input('Нажмите ENTER для продолжения.')
        else:
            print(f'Заметок с ключевой фразой : "{phrase}" не найдено.')
            input('Нажмите ENTER для продолжения.')


# Процедура обновления Заметки
def update_note(note):
    while True:
        while True:
            choise = input(
                'Выберите изменяемые поля Заметки (username, title, content, status, issue_date) или ENTER для продолжения : ')
            if choise in ('username', 'title', 'content', 'status', 'issue_date', ''):
                break
            else:
                print('Ошибка ввода! Вводите текст из предложенных вариантов.')
        if choise == 'username':
            note['username'] = input(
                'Введите НОВОЕ имя пользователя (нажмите ENTER для случайной генерации) : ') or 'Name № ' + str(
                random.randint(1, 100))
        if choise == 'title':
            # Пустой список Заголовков
            title_list = []
            while True:  # бесконечный цикл - ввод значений до прерывания цикла
                title = input('Введите НОВЫЙ заголовок (или оставьте пустым для завершения ввода) : ')
                if title == '':  # условие прерывания ввода Заголовков
                    break
                elif title not in title_list:  # проверка отсутствия введённого Заголовка в списке Заголовков
                    title_list.append(title)  # и добавление Заголовка в список
                else:  # когда не прошли проверку на задублированность Заголовка в списке
                    print('Такой заголовок уже существует, попробуйте ввести другой!')
            note['title'] = title_list
        if choise == 'content':
            note['content'] = input(
                'Введите описание заметки (нажмите ENTER для случайной генерации) : ') or 'Текст заметки №' + str(
                random.randint(1, 100))
        if choise == 'issue_date':
            print('Введите дату актуальности заметки.')
            note['issue_date'] = input_date()
        if choise == 'status':
            # 0 - ожидает, 1 - в работе, 2 - готово
            while True:
                status = input(
                    f'Введите статус заметки (0 - {status_list[0]}, 1 - {status_list[1]}, 2 - {status_list[2]}, нажмите ENTER для статуса 0) : ') or 0
                if status not in range(3):
                    print('Пожалуйста, выберите статус из предложенных вариантов!')
                else:
                    break
            note['status'] = status
        else:
            break
    return note


# Функция поиска Заметки по критерию
def search_notes(note_list: list, keyword=None, status=None):
    note_list_seach = []
    if keyword != None or status != None:
        get_note_keyword = True
        get_note_status = True
        for note in note_list:
            if keyword != None:
                get_note_keyword = False
                if keyword.lower() in note.get('username').lower() or keyword.lower() in note.get('content').lower():
                    get_note_keyword = True
                else:
                    for title in note.get('title'):
                        if keyword.lower() in title.lower():
                            get_note_keyword = True
            if status != None:
                get_note_status = False
                if status.lower() in status_list[note.get('status')].lower():
                    get_note_status = True
            if get_note_keyword and get_note_status:
                note_list_seach.append(note)
    return note_list_seach


# ОСНОВНАЯ ПРОГРАММА
if __name__ == '__main__':
    # инициализация нового (пустого) списка Заметок
    note_list = []
    # инициализация предзаполненного списка Заметок
    note_list = [{'username': 'Максим',
                  'title': ['Программирование', 'Тестирование'],
                  'content': 'Решить и проверить задачу',
                  'status': 1,
                  'created_date': '22-01-2025',
                  'issue_date': '31-01-2025'},
                 {'username': 'Алекс',
                  'title': ['Тестирование'],
                  'content': 'Проверить задачу Максима',
                  'status': 0,
                  'created_date': '23-01-2025',
                  'issue_date': '01-02-2025'},
                 {'username': 'Ирина',
                  'title': ['Подготовить задание', 'Разработать тесты'],
                  'content': 'Придумать задачу и несколько тестов для проверки её решения',
                  'status': 2,
                  'created_date': '28-12-2024',
                  'issue_date': '20-01-2025'},
                 {'username': 'Игнат',
                  'title': ['Программирование'],
                  'content': 'Написать программу решения задачи',
                  'status': 2,
                  'created_date': '03-01-2025',
                  'issue_date': '31-01-2025'}]
    while True:
        menu = select_menu()
        if menu == 1:  # Добавить Заметку
            note_list.append(create_note())

        elif menu == 2:  # Вывести Заметки
            display_notes(note_list, True)

        elif menu == 3:  # Вывести Заметки и предложить изменение Заметки
            display_notes(note_list, False, True)

        elif menu == 4:  # Удалить Заметки по искомым параметрам
            delete_notes(note_list)

        elif menu == 5:  # Поиск Заметок и вывод на экран
            notes = []
            key_phrase = input('Введите искомую ключевую фразу Заметки или "ENTER" для отмены ввода : ') or None
            key_status = input('Введите искомый Статус Замети или "ENTER" для отмены ввода : ') or None
            notes = search_notes(note_list, key_phrase, key_status)
            if notes != []:
                print('Список найденных заметок :')
            display_notes(notes, True)

        elif menu == 0:  # Выход из программы
            print('Программа завершена. Спасибо за использование!')
            break
