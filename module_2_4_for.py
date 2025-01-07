# list_ = ['one', 'two','four']
# list_2 = [2, 4, 3, 2, 1]
# sum1 = 0
#
# for i in range(len(list_2)):
#     sum1 += list_2[i]
#
# print(sum1)
from itertools import count

# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i * j}')
#
# dict_ = {'a':1, 'b':2, 'c':3}
# for i in dict_:
#     print(i, dict_[i])
# dict_ = {'a':1, 'b':2, 'c':3}
# for i, k in dict_.items():
#     print(i, k)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 139]
primes = []
not_primes = []

for i in range(len(numbers)):
    if i < 1:
        continue
    is_prime = True   # Здесь получается мы обозначили степень равенства, и сообщили начальное условие, что если i
                      # меньше двух, то мы продолжаем
    for k in range(2, numbers[i]):  # Вложенным циклом начинаем перебирать числа друг с другом, используя один словарь
                                    # Если число делиться на число из списка i для k  без остатка (остаток после деления
                                    # равен 0), то
        if numbers[i] % k == 0:
            not_primes.append(numbers[i]) #Мы обновляем список не простых чисел, пока не встреимся с простым числом

            is_prime = False         #Если из прайм фолс, то вложенный цикл после перебора остановится и начнет
                                    # выполняться

            break

    if is_prime == True:           #список который соответсвует условию (Обясните почему здесь пришлось использовать знак сравнения )
        primes.append(numbers[i])

print('Primes: ' + str(primes))
print('Not_primes: ' + str(not_primes))