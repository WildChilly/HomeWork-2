


class Human:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health
        self.say_info()


    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age} и у меня еще пока {self.health} здоровья')



    def birthday(self):
        self.age += 1

        print(f'У меня день рождения, мне теперь {self.age} и кстати я {self.name}, {self.health} - осталось здоровья')

    def damage_health(self):
        if self.age + 1:

            self.health -= 1
            print(f'{self.health}')
    def __len__(self):
        return self.age

    def __del__(self):
        print(f'{self.name} ущел жи есть ехать на лифте, дон')

den = Human('Денис', 33, 100) # определяет срабатывание метода инит,
                                    # если не прописать то не сработает
max_ = Human('Максим', 23, 100)

max_.surname = 'RavnovESV'



#den.say_info()
# max_.say_info()
# # удалили Дэна
max_.birthday() # вызов второго атрибута день рожденье
max_.damage_health()
input()
max_.birthday()
max_.damage_health()
revers_surname = max_.surname[::-1]
print(revers_surname)
print(reversed(max_.surname))
max_.damage_health()
print(len(max_))