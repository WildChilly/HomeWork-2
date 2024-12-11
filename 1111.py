numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        index += 1
        continue
    print(numbers[index])
    index += 1