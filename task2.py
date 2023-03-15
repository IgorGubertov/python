"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_user_data(**user_data) -> None:
    """ Распечатывает в одну строку данные пользователя
    :param user_data: данные пользователя
    """
    print(f'{user_data.get("name")} {user_data.get("surname")}'
          f' {user_data.get("birth_year")} года рождения, проживает в городе {user_data.get("city")},'
          f' email: {user_data.get("email")}, телефон: {user_data.get("phone")}')


if __name__ == '__main__':
    user = {
        'name': 'Иван',
        'surname': 'Иванов',
        'birth_year': '1900',
        'city': 'Москва',
        'email': 'iivanov@gmail.com',
        'phone': '8-901-250-33-00',
    }

    print_user_data(**user)
