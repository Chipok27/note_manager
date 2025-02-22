# Grade 1. Этап 2: Задание 2 (check_dealine)
# ЗАМЕТКИ

import random, datetime


def input_date():  # Функция ввода даты с проверкой
    date_valid = False
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


note_list = []

while True:
    print('===========Ввод данных новой заметки===========\n')
    note = {'username': 'Name',
            'title': ['Tit1', 'Tit2'],
            'content': 'Content',
            'status': '0',  # 0 - ожидает, 1 - в работе, 2 - готово
            'created_date': '01-01-1999',
            'issue_date': '31-12-2024'}
    note['username'] = input('Введите имя пользователя (нажмите ENTER для случайной генерации): ') or 'Name № ' + str(
        random.randint(1, 100))
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
            'Введите статус заметки (0 - ожидает, 1 - в работе, 2 - готово, нажмите ENTER для статуса 0): ') or '0'
        if status not in ('0', '1', '2'):
            print('Пожалуйста, выберите статус из предложенных вариантов!')
        else:
            break
    note['status'] = status

    print('Введите дату создания заметки.')
    note['created_date'] = input_date()

    print('Введите дату актуальности заметки.')
    note['issue_date'] = input_date()

    note_list.append(note)

    continue_input = input('Вводим новую заметку (0 - Нет, 1 - Да (при нажатии ENTER) :') or '1'
    if continue_input == '0':
        break

for note in note_list:
    print('===========Начало заметки===========')
    print('Имя пользователя:', note['username'])
    print('Заголовки Заметки :')
    for title in note['title']:
        print('- ', title)
    print('Описание заметки:', note['content'])
    status = note['status']
    if status == '0':
        print('Текущий статус заметки:', 'ожидает')
    if status == '1':
        print('Текущий статус заметки:', 'в работе')
    if status == '2':
        print('Текущий статус заметки:', 'готово')
    print('Дата создания заметки:', note['created_date'][:-5])
    print('Дата актуальности заметки', note['issue_date'][:-5])

    # Проверка просроченности заметки
    if datetime.datetime.now().strptime(note['issue_date'], '%d-%m-%Y') < datetime.datetime.now():
        print('Данная заметка просрочена!')

    print('============Конец заметки===========')
    status_change = input('Требуется изменение статуса Заметки? (Д|Н) :')
    if status_change in ['д', 'Д']:
        while True:
            status = input(
                'Введите новый статус заметки (0 - ожидает, 1 - в работе, 2 - готово, нажмите ENTER для статуса 0): ') or '0'
            if status not in ('0', '1', '2'):
                print('Пожалуйста, выберите статус из предложенных вариантов!')
            else:
                break
        note['status'] = status
