def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)



print(summa(5))

# Стэк вызовов, хранение в памяти информации о вызовах программы
stack = []
stack.append(1) # Добавляем элементы с начала двигаясь к концу
print('Добавили элемент', stack)
stack.append(2)
print('Добавили элемент', stack)
stack.append(3)
print('Добавили элемент', stack)
print(stack)  # Убираем элементы с конца - двигаюсь к началу
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
print(stack) # тут увидим пустой список


# ошибка рекурсии
# def recursion():
#     recursion()
# recursion()

# Самостоятельная работа

def get_multiplied_digits(number):
    str_number = str(number) # перевели прием функции в строку
    first = int(str_number[0]) # создали переменную
    if len(str_number) > 1:
        if first != 0:

            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402033030)
print(result)
print(result2)




# к сожалению опять ни к чему не приуроченный пример
# не удалось добиться вывода результата 2 до 24 по примеру. в конце получается 0
