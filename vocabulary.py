food = ['meat', 'salt', 'vegetebles', 'olive oil', 'onion']
count = [1, 2, 3, 4, 5]
for sub_list in food:
    for item in sub_list:
        print(item, end=' ')
    print()
for sub_list1 in count:
    for item in str(sub_list1):
        print(item, end=' ')
    print()

f_c = str(food + count)
print(f_c)

for b in food:
    for st in count:
        print(b + str(st))
    print()