# Grade 1. Этап 1: Задание 3
# ЗАМЕТКИ

username = input('Введите имя пользователя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
# 0 - ожидает, 1 - в работе, 2 - готово
status = input('Введите статус заметки (0 - ожидает, 1 - в работе, 2 - готово): ')
created_date = input('Введите дату создания заметки в формате ДД-ММ-ГГГГ: ')
issue_date = input('Введите дату актуальности заметки в формате ДД-ММ-ГГГГ: ')

print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
if int(status) == 0:
    print('Статус заметки:', 'ожидает')
if int(status) == 1:
    print('Статус заметки:', 'в работе')
if int(status) == 2:
    print('Статус заметки:', 'готово')
print('Дата создания заметки:', created_date[:-5])
print('Дата актуальности заметки', issue_date[:-5])