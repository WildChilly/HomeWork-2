# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#
#
#     def say_info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age}')
#
#
#     def birthday(self):
#         self.age += 1
#         print(f'У меня день рождения, мне теперь {self.age}')
#
#
# #den = Human('Денис', 33) # определяет срабатывание метода инит,
# # если не прописать то не сработает
# #max_ = Human('Максим', 23)
# # print(den.name, den.age)
# # print(max_.name, max_.age)
# # den.surname = 'Popov'
# # print(den.age, den.surname, den.name)
# # den.say_info()
# # max_.say_info()
# # print(den.age)
# #max_.birthday() # вызов второго атрибута день рожденье
import random
print('\n@@@@@  Домашняя работа @@@@@\n')
class House:

    house_history = []

    head = True # классовый атрибут

    def __new__(cls, *args, **kwargs):


    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        self.say_info()


    def say_info(self):
        print(f'Это дом {self.name}, у него {self.floors} этажей(а)')


    def go_to(self, new_flor): # Метод считающий этажи
        global massage  # добавил саспиенса текстом, не уверен нужна ли переменная глобал????
        random_text = ['визг механизма', '..шорохи..','скрипы..', 'крехтения', 'звук ломающегося подъемника',
                       'звуки ада*уууу*аааа', 'может не доедешь', 'вот-вот рухнет']
        random.shuffle(random_text)
        if new_flor < 1 or new_flor > self.floors: # намного логичнее и удобнее получается,
                                                    # если начинать с логических отрицаний или операторов
            print(f'{new_flor}-й, серьезно? Такого этажа не существует Х_х \n')
        else:
            for flor in range(1, new_flor + 1):

                massage = random.choice(random_text) # заворачиваем в удобную переменную нашу функцию рандомного
                                                                                            # вынимания строк


                print(f'{flor}-й этаж \n....{massage}....') # Перебираем все этажи и добавляем (поса)саспиенса
            print(f'\n //// Поздравляю, ты живой доехал на {new_flor}-й этаж //// \n') # Обозначаем что добрались на нужный этаж
# МАГИЧЕСКИЕ ЗАДАНИЯ или новая версия задания
    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.floors}'

# НУЖНО БОЛЬШЕ ЭТАЖЕЙ следующее ДЗ
    def __add__(self, value): #метод адд
        self.floors += value
        return self

    def __radd__(self, value): # метод используется когда слева обьект не определен
        return self + value

    def __iadd__(self, value): # делает тоже самое что адд и  в чем разница?
        self.floors += value
        return self

    def __eq__(self, other):
        return  self.floors == other.floors
    def __lt__(self, other):
        return  self.floors < other.floors
    def __le__(self, other):
        return  self.floors <= other.floors
    def __gt__(self, other):
        return  self.floors > other.floors
    def __ge__(self, other):
        return  self.floors >= other.floors
    def __ne__(self, other):
        return  self.floors != other.floors



h1 = House('Мега Дом Дон', 40)
h2 = House('Derevnya Дом Дон', 4)
h1.go_to(10)
h2.go_to(45)
h2.go_to(4)

# Вопрос: как для последнего этажа убрать приписку из рандомного списка, чтобы сразу печаталось поздравление о
# достижении нужной высоты?


# Вывод по второй части задания
print(f'\n#### Вывод по второй части задания ####\n')
print(f'\n.... вывод по магии len')
print(len(h1))
print(len(h2))
print(f'\n.... вывод по магии str')
print(str(h1))
print(str(h2))
# Это получается что мы в глобальной видимости имен переписали функцию лен?

print(f'\n#### Вывод по третьей части задания ####\n')
print(f'\n __add__')
h1 += 22
print(len(h1 + 3))
print(len(h2 + 3))
print(f'\n __eq__')
print(h1 == h2)
print(f'\n __')
h1 = h1 + 3
print(h1)
print(f'\n__ Перегруженные операторы сравнений')
print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__