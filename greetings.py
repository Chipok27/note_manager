# Grade 1. Этап 1: Задание 1
# ЗАМЕТКИ

username = 'Пользователь #1'
title = 'Первая заметка'
content = 'Заметили первую заметку'
# 0 - ожидает, 1 - в работе, 2 - готово
status = 0
created_date = '10-11-2024'
issue_date = '10-12-2024'

print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
if status == 0:
    print('Статус заметки:', 'ожидает')
if status == 1:
    print('Статус заметки:', 'в работе')
if status == 2:
    print('Статус заметки:', 'готово')
print('Дата создания заметки:', created_date)
print('Дата актуальности заметки', issue_date)
