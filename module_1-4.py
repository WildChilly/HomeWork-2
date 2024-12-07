from itertools import count

my_string = input('Моя строка: ')

# колличество символов в строке
print(len(my_string))


# Строка в вверхнем регистре
print(my_string.upper() )

# Строка в нижнем регистре

print(my_string.lower())

# Без пробелов
print(my_string.replace(' ',  ''))
# в этом упражнении остановило то, что параметры old и new оказывается не нужно прописывать, ведь они сами появляются как коментарий
# при вводе нобходимы значений

# Первый символ
print(my_string[0])

# Последний символ
print(my_string[-1])
