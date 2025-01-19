

def say_hi():
    print('Привет я из функции во втором модуле demo_urban_less2')
    from random import randint
    print(randint(2,34))

def main():
    a = 5
    b = 10
    print('Привет')

def some_func():
    a = 'Привет я из второго модуля'
    print('Привет я из второго модуля')
    return a
some_func()

if __name__ == '__main__':
    main()