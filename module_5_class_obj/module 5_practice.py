class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        if self._is_valid_password(password):
            self.data[username] = password
            print(f'Пользователь успешно зарегистрирован {username}')
        else:
            print('Не верный ввод, повторите попытку')
    def _is_valid_password(self, password):
        if len(password) < 6:
            print('Пароль должен содержать не меньше 6 символов')
            return False
        if (not any(char.isupper() for char in password) or
                not any(char.islower() for char in password) or
                not any(char.isdigit() for char in password) or
                not any(char in "!@#$%^&*{}[]/()\\\"'" for char in password)):
            print('Пароль должен содержать хотя бы одну букву верхнего или нижнего регистра, '
                  'цифру и уникальные символы - "!@#$%^&*{}[]/()\\\"\'"')
            return False

        # if (not any(char.isupper()) for char in password) or \
        #     (not any(char.islower()) for char in password) or \
        #     (not any(char.isdigit()) for char in password) or \
        #     (not any(char.isalnum()) for char in password):# нашел самое оптимальное и лаконичное решение.
        #                                                     # Мне лично всегда сложно начать с логики отрицания,
        #                                                     # в голове всегда присутствует то что должно быть, но на
        #                                                     # самом деле легче пойт от того чего быть не должно.
        #                                                     # есть ли методики для развития мышления и понимания написания кода?
        #     print('Пароль должен содержать хотя бы одну букву верхнего или нижнего регистра, '
        #           'цифру, уникальные символы - "!@#$%^&*{}[]/(\)[\]"') # как убрать синтаксическую ошибку, поможет ли метод raise и обозначение ошибки?
        #     return False
        return True
class User:
    """
    Класс пользователя содержащий атрибутыЖ логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Приветсвую! Выберите действие: \n1 - Вход \n2 - Регистрация \n')
        if choice == '1':
            login = input('Enter login: ')
            password = input('Enter password: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Welcome, {login}')
                    break
            else:
                print('Unknown user')
        if choice == '2':
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                       password2 := input('Подтвердите пароль: '))
            if password != password2:
                continue
            database.add_user(user.username, user.password)
        print(database.data)