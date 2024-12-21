# Grade 1. Этап 1: Задание 4
# ЗАМЕТКИ

title_list = []
username = input('Введите имя пользователя: ')
title_count = int(input('Сколько заголовков у заметки :'))
for i in range(title_count):
    title = input('Введите заголовок заметки №' + str(i + 1) + ' : ')
    title_list.append(title)
content = input('Введите описание заметки: ')
# 0 - ожидает, 1 - в работе, 2 - готово
status = input('Введите статус заметки (0 - ожидает, 1 - в работе, 2 - готово): ')
created_date = input('Введите дату создания заметки в формате ДД-ММ-ГГГГ: ')
issue_date = input('Введите дату актуальности заметки в формате ДД-ММ-ГГГГ: ')

print('Имя пользователя:', username)
for i in range(title_count):
    print('Заголовок №' + str(i + 1) + ' заметки:', title_list[i])
print('Описание заметки:', content)
if int(status) == 0:
    print('Статус заметки:', 'ожидает')
if int(status) == 1:
    print('Статус заметки:', 'в работе')
if int(status) == 2:
    print('Статус заметки:', 'готово')
print('Дата создания заметки:', created_date[:-5])
print('Дата актуальности заметки', issue_date[:-5])
