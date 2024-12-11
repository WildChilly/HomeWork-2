grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}




stud = list(students)
stud.sort(key= None, reverse= False) # Перевел в изменяемый список и сортировал по алфавиту (что в итоге делает маяк Key= не выяснил)

mean_grade = sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4]) # полагаю что в будущем научат более изящным решениям
# mean_grade_1 = int(sum(grades[0:1:4])) / len(grades[0:1:4]) почему нельзя вот так?
mean_grade_of_students = mgos = {} # создал пустой словарь, как еще в него можно добавить и обьеденить два списка, не прибегая к методам которых нет в первом модуле обучения?

mgos = zip(stud,mean_grade) # Упаковал Ключ и полученные значения



print(dict(mgos))

