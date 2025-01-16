print(1==1) # True
print(2==1) # False

print(2!=1) # True
print(1!=1) # False

print(2>1) # True
print(1>2) # False

print(2>=2) #True
print(1>=2) # False

print(1<2) # True
print(2<1) # False

print(1<=2) # True
print(2<=1) # False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    if numbers[i]<2:
        continue
    is_prime = True
    for k in range(2,numbers[i]):
        if numbers[i] % k == 0:
            not_primes.append(numbers[i])
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])

print(primes)
print(not_primes)

def dict_students(grades,students):
    dic_students = {} #словарь
    students_1 = sorted(students)
    for i in range(len(students_1)):
        grades[i]= sum(grades[i])/len(grades[i])
        dic_students.update({students_1[i]:int(grades[i])})
    return dic_students

a = dict_students(grades=[[5,3,3,5,4],[2,2,2,2,2]], students={'Ivanov', 'Petrov'})


print(a)

b = dict_students(grades=[[5,4,5,6,5,6,9]], students={'Burdakoff'})


print(b)

def add_item_to_shopping_list(item, shopping_list=None):
    if shopping_list is None:
        shopping_list = []
    shopping_list.append(item)
    print(f"Товар добавлен: '{item}', Текущий список покупок: {shopping_list}")

add_item_to_shopping_list("Яблоки")
add_item_to_shopping_list("Хлеб")

def a(item, my_list=None): # система функция собирающая данные
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

def collect_user_inputs():
    user_inputs = []
    while True:
        user_input = input("Введите значение (или 'exit' для выхода): ")
        if user_input.lower() == 'exit':
            break
        user_inputs = a(user_input, user_inputs) # здесь используется предыдущая функция def a(item, my_ list=None) она сохраняет в себя полученные значения из user_input
    print("Собранные данные:", user_inputs)

collect_user_inputs()
