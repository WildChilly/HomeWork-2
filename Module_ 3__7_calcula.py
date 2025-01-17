import tkinter as tk
from idlelib.debugger_r import wrap_info

def get_values(): # функция принимающая ввод с первого и второго окошка для ввода
    """
    принимающая функция с экранов для ввода и возвращающая значения
    :return:
    """


    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    """
    принимаюая функция
    :param value:
    :return:
    """
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    """
    функция сложения
    :return:
    """
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('450x450')
window.resizable(False,False)
button_add = tk.Button(window, text='+', width=4, height=2, command=add) # создали перееменную и загнали в нее визуализацию кнопки, которая привязана к нашему окну
button_add.place(x=50, y=140) # отсчет начинается с левого верхнего угла x= слева на право, y = сверху вниз
button_sub = tk.Button(window, text='-', width=4, height=2, command=sub)
button_sub.place(x=150, y=140)
button_mul = tk.Button(window, text='*', width=4, height=2, command=mul)
button_mul.place(x=250,y=140)
button_div = tk.Button(window, text='/', width=4, height=2, command=div)
button_div.place(x=350,y=140)
number1_entry = tk.Entry(window, width=50)
number1_entry.place(x=50,y=45)
number2_entry = tk.Entry(window, width=50)
number2_entry.place(x=50,y=90)
answer_entry = tk.Entry(window, width=50)
answer_entry.place(x=50, y=270)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=49,y=22)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=49,y=67)
answer = tk.Label(window, text='Ответ:')
answer.place(x=49,y=247)

window.mainloop()

# import tkinter
# print(tkinter.Tk().tk.eval('info patchlevel'))
