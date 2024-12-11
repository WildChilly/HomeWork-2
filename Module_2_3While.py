
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

# redy = list_while + my_list[int]

while i < len(my_list):
    if my_list[i] == 0:
        i += 1   # если отдельно закоментировать этот инструмент, то в консоль мы получим 0 тк i == 0, значит ли
                 # это чт
        print(my_list[i])
        i += 1
    if my_list[i] < 0:

        break
    print(my_list[i])
    i += 1

# в уроках ничего не сказано об инструментах отладки i += 1


