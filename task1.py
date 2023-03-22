"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('task1_file.txt', 'a', encoding="utf-8") as file:
    while True:
        user_an = input('Введите текст: ')
        file.write(user_an + '\n')
        if not user_an:
            break
