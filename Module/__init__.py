print('Я в ините в пакете модуле')
#This is package
def print_person_info(name, age): # распаковка функцийБ повторение
    print("Имя:", name)
    print("Возраст:", age)

# Создаем список кортежей
persons = [("Иван", 25), ("Мария", 30)]

# Распаковываем список в аргументы функции
for person in persons:
    print_person_info(*person)


class House:
    def __new__(cls, *args, **kwargs):
        print("Вызван метод __new__ класса", cls)
        return super().__new__(cls)

    # Другие методы...

class Villa(House):
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        self.say_info()
    def say_info(self):
        print(f'{self.name}, {self.floors}')

    def __del__(self):
        print(f'{self.name} удалились')
        return

# Создание экземпляра класса Villa
villa = Villa("Вилла Мечта", 3)
villa2 = Villa("Нет мечты", 4)

del villa  # Удаляем только villa

# Проверка состояния объекта villa2
try:
    print(f"Имя второй виллы: {villa2.name}, Этажи: {villa2.floors}")
except NameError:
    print("villa2 больше не доступна.")
