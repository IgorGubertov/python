"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_filename = "task5_file.txt"

DIGITS_STR = "16 9.2 122 32.7 0 40 12.1"

if __name__ == "__main__":
    summ = 0

    try:
        with open(my_filename, 'w', encoding='utf-8') as fhs:
            fhs.write(DIGITS_STR)

        with open(my_filename, encoding='utf-8') as fhd:
            data = fhd.read()

        for item in data.split():
            summ += float(item)
    except IOError as e:
        print(e)
    except ValueError:
        print("Неконсистентные данные")

    print(summ)
