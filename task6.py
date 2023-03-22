"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

my_filename = "task6_file.txt"

if __name__ == "__main__":
    subjects = {}

    try:
        with open(my_filename, encoding='utf-8') as fh:
            lines = fh.readlines()

        for line in lines:
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
    except IOError as e:
        print(e)
    except ValueError:
        print("Неконсистентные данные")

    print(subjects)
