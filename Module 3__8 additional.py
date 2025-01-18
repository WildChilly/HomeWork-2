def calculate_structure_sum(data):
    '''
    Функция, которая может сложить все что угодно
    '''
    total_sum = 0 # создали счетчик с 0 значением


    if isinstance(data, (list, tuple, set)): # Проверка на список, кортеж или множество
        for item in data:
            total_sum += calculate_structure_sum(item)

    elif isinstance(data, dict): # проверка на словарь
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Считаем ключи словарей рекурсивно добавляем их в счетчик
            total_sum += calculate_structure_sum(value)  # Считаем значения словарей
    elif isinstance(data, str):
        total_sum += len(data) # Считаем длину строки
    elif isinstance(data, (int, float)):
        total_sum += data  # Проверка на число



    return total_sum # возврат полученных значений в переменную total_sum



# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
