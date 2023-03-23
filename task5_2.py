"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def count_info():
    try:
        with open('task5_1_file.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Нет такого файла.'


count_info()
