# Grade 1. Этап 1: Задание 5
# ЗАМЕТКИ

import random, datetime

note_list = []

while True:
    print('===========Ввод данных новой заметки===========\n')
    note = []
    username = input('Введите имя пользователя (нажмите ENTER для случайной генерации): ') or 'Name № ' + str(
        random.randint(1, 100))
    note.append(username)
    title_count = int(input('Сколько заголовков у заметки (нажмите ENTER, если один) :') or '1')
    note.append(title_count)
    title_list = []
    for i in range(title_count):
        title = input('Введите заголовок заметки №' + str(i + 1) + ' : ') or 'Заголовок' + str(random.randint(1, 100))
        title_list.append(title)
    note.append(title_list)
    content = input('Введите описание заметки (нажмите ENTER для случайной генерации): ') or 'Текст заметки №' + str(
        random.randint(1, 100))
    note.append(content)
    # 0 - ожидает, 1 - в работе, 2 - готово
    status = input(
        'Введите статус заметки (0 - ожидает, 1 - в работе, 2 - готово, нажмите ENTER для статуса 0): ') or '0'
    note.append(status)
    created_date = input(
        'Введите дату создания заметки в формате ДД-ММ-ГГГГ (или нажми ENTER для ввода текущей даты) : ') or datetime.datetime.now().strftime(
        '%d-%m-%Y')
    note.append(created_date)
    issue_date = input('Введите дату актуальности заметки в формате ДД-ММ-ГГГГ: ') or '31-12-2024'
    note.append(issue_date)
    note_list.append(note)

    continue_input = input('Вводим новую заметку (0 - Нет, 1 - Да (при нажатии ENTER) :') or '1'
    if continue_input == '0':
        break

for note in note_list:
    print('===========Начало заметки===========')
    username = note[0]
    print('Имя пользователя:', username)
    title_count = note[1]
    for i in range(title_count):
        title = note[2][i]
        print('Заголовок №' + str(i + 1) + ' заметки:', title)
    content = note[3]
    print('Описание заметки:', content)
    status = note[4]
    if int(status) == 0:
        print('Статус заметки:', 'ожидает')
    if int(status) == 1:
        print('Статус заметки:', 'в работе')
    if int(status) == 2:
        print('Статус заметки:', 'готово')
    created_date = note[5]
    print('Дата создания заметки:', created_date[:-5])
    issue_date = note[6]
    print('Дата актуальности заметки', issue_date[:-5])
    print('============Конец заметки===========')
