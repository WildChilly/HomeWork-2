immutable_var = (12, 24, 48.3, True, 'Head', 'Hand')
immutable_var_1 = ([96, 1, 99.3], 0)
i_v_3 = immutable_var + tuple(immutable_var_1)
print(i_v_3)

print(i_v_3[1:7:2])
print(i_v_3[0 : 3:])

immutable_var_1[0][2] = 33.3

print(immutable_var_1)

# Невозможно заменить значения float если они указаны как кортеж, если же добавить в кортеж список list, то станоятся
# доступны функции замены из списка внутри кортежа. То есть список находящийся в кортеже можно изменять в пределах списка
# как, кстати, можно заменить список дргугим списком в пределах кортежа?
# А в общем - изменять значения в кортеже нельзя тк это неизменяемый список

mutable_list = ['a', 'hello', 1, 2, 3, 4, 33.4, 54.3, False]

print(mutable_list)
print(mutable_list[0])
print(mutable_list[2:7]*2)
print(mutable_list[0::])
total = sum(mutable_list[3:7])

print(total)
mutable_list.append('Oil')
mutable_list.extend('False')
mutable_list.append('False')
mutable_list.insert(3, False)
print(mutable_list)