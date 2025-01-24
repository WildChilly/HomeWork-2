from setuptools.package_index import user_agent

print(int.__mro__)  # __mro__ устанавливает цепочку наследования
print(object)

class User:
    __instance = None   #  instance (экземпляр) — это конкретный объект, созданный на основе определённого класса.
                        #  instance в Python — это не просто копия класса, а полноценный объект со своими свойствами и поведением.
                        # Или же это оператор isinstance() для проверки, является ли объект экземпляром определённого класса.

    def __new__(cls, *args, **kwargs):  # пример сингл тона
        print('Я в нью, почти йорке')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance # возвращаем ссылку на класс, а не на условие!!! Соблюдай пробелы и синтаксис

    def __init__(self, *args, **kwargs):
        print('Я в ините, жи есть')
        self.args = args
        #self.name = kwargs.get('name') # Первый способ распаковки
       # self.age = kwargs.get('age')
        for key, values in kwargs.items(): # Лучший способ распаковки кваргс
            setattr(self, key, values)


# переменное количество параметров, когда не знаем сколько параметров будет принимать объект этого класса

other = [1,2,3 ]
user = {'name':'Alex', 'age': 29, 'gender': 'male'}


user1 = User(other, **user)  # Без сингл тона ссылки на объект будут вести в разные места памяти
#user2 = User()  # С использованием сингл тона ссылки на объект будут вести в одну и туже ячейку памяти

print(User.__mro__)
print(user1)
#print(id(user1), id(user2))
print(user1.args)

print(user1.name)
print(user1.age)
print(user1.gender)
