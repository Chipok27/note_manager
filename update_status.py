# Grade 1. Этап 2: Задание 1
# ЗАМЕТКИ

import random, datetime

note_list = []

while True:
    print('===========Ввод данных новой заметки===========\n')
    note = []
    username = input('Введите имя пользователя (нажмите ENTER для случайной генерации): ') or 'Name № ' + str(
        random.randint(1, 100))
    note.append(username)

    title_list = []
    while True:  # бесконечный цикл - ввод значений до прерывания цикла
        title = input('Введите заголовок (или оставьте пустым для завершения ввода)')
        if title == '':  # условие прерывания ввода Заголовков
            break
        elif title not in title_list:  # проверка отсутствия введённого Заголовка в списке Заголовков
            title_list.append(title)  # и добавление Заголовка в список
        else:  # когда не прошли проверку на задублированность Заголовка в списке
            print('Такой заголовок уже существует, попробуйте ввести другой!')

    note.append(title_list)
    content = input('Введите описание заметки (нажмите ENTER для случайной генерации): ') or 'Текст заметки №' + str(
        random.randint(1, 100))
    note.append(content)
    # 0 - ожидает, 1 - в работе, 2 - готово
    while True:
        status = input(
            'Введите статус заметки (0 - ожидает, 1 - в работе, 2 - готово, нажмите ENTER для статуса 0): ') or '0'
        if status not in ('0', '1', '2'):
            print('Пожалуйста, выберите статус из предложенных вариантов!')
        else:
            break
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
    print('Заголовки Заметки :')
    for title in note[1] :
        print('- ', title)
    content = note[2]
    print('Описание заметки:', content)
    status = note[3]
    if status == '0':
        print('Текущий статус заметки:', 'ожидает')
    if status == '1':
        print('Текущий статус заметки:', 'в работе')
    if status == '2':
        print('Текущий статус заметки:', 'готово')
    created_date = note[4]
    print('Дата создания заметки:', created_date[:-5])
    issue_date = note[5]
    print('Дата актуальности заметки', issue_date[:-5])
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
        note[3] = status