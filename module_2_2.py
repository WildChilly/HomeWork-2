
name = input('Как к вам обращаться? '
             '(введите Ваше имя/никнейм): ')

print('Привет,', name, ', я программа сравнения чисел, давай-ка всё сравним!')
while True:
    print('Введи свои числа ниже в появляющиеся строки, после ввода каждого числа жми "Enter" чтобы пойти дальше')
    first = input('Введи первое число: ')
    second = input('Введи второе число: ')
    third = input('Введи третье число: ')
    while True:
        if len(first) == 1 and first.isalpha() or len(second) == 1 and second.isalpha() or third == 1 and third.isalpha():
                print('Числа это циферки :))) буквы еще не могу')
        break




    if first == second and first == third and second == third:
        print('Все числа похожи, ура :) Индекс: ', 3)
    elif first == second or first == third or second == third:
        print('Есть два похожих числа, неплохо :/ Индекс', 2)
    elif first != second and first != third or second != third:
        print('Похожих совсем нет:( Индекс: ', 0)

    print('Пробуем еще?')



