lista = [1, 1, 2, 3, 4, 4, 5, 1]

array = []
for item in lista:
    if item not in array:
        array.append(item)

print(array)