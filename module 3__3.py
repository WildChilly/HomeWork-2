def print_parames(*parames): # *args, **kwargs
    print(a, b , c)

def params(a, b, c):
    print(a, b, c)
    c = 4
    print(c)
list_ = [1, 4, 3]

params(*list_)


def dicter(a, b, c):
    print(a, b ,c)

def dicter_cykle(**kwargs): #распаковка без конкретики
    for key, value in kwargs.items():
        print(key, value)

dict_ = {'a':1, 'b': 2, 'c': 3}
dicter(**dict_)

dicter_cykle(**dict_)

def summ_of_dicter(a, b, c):
    print(a, b, c)

list1_ =[5, 2]
dict2_ = {'c': 77}

summ_of_dicter(*list1_,*dict2_) # в СЛОВАРЯХ ОДНА звездочка распаковывает ключ

summ_of_dicter(*list1_,**dict2_) # в СЛОВАРЯХ ДВЕ звездочки распаковывают значение
summ_of_dicter(list1_,**dict2_, b=23)

# Самостоятельная работа

def print_params(a=1, b='Строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = (1, True, 'fackTheHack')
values_dict = {'a': 22, 'b': False, 'c':'Erevan'}
print_params(**values_dict)
print_params(*values_list)
values_list2 = [44.44, 'Жмых']
print_params(*values_list2, 22)

def a(item, my_list=None):   # как это можно применять на практике?
    if my_list is None:
        my_list=[]
    my_list.append(item)
    print(my_list)

a('ss')
a('erere')
a('ddffeeeeff fefe')

a('Task', my_list=[422442,333,333,44])
task = []
a(3444,task)
a()



