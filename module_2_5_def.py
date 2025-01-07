from ctypes import HRESULT


def say_hello(name):
    print('Hello ' + name)
say_hello('Gagik')  # Принимающая функция


import random
def lottery():
    tickets = range(1, 101)
    win = random.choice(tickets)
    return  win
win = lottery()

print(win)

def test_gano_lekcia(a= 'Gano', b= 'Sanoek'):
    print(a,b)
test_gano_lekcia()

def malo_inform_sam_naydi(name='Loxnes', ser_name='Pirod'):
    print(name, ser_name)
malo_inform_sam_naydi(name='Losaral', ser_name='Sanayanu')

malo_inform_sam_naydi('YA', 'Jack')

# Домашнее задание
def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
         matrix.append([]) #Очень долгое время ломал голову над тем, что на самом деле необходимо список обновить списком,
        #                   что по русски написано в задании =))

        for k in range (m):
            matrix[i].append(value)
    return matrix
result_1 = get_matrix(2,2,13)
result_2 = get_matrix(3,5,42)
result_3 = get_matrix(4,2,13)
print(result_1)
print(result_2)
print(result_3)

#Единственное что не ясно из уроков и лекции и из самого задания - для чего применяются матрицы? Просто пробуйте говорится в уроке)))))
# Вот для чего конкретно можно было использовать эту матрицу?
