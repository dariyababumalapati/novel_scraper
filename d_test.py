matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

elements = [e for element in matrix for e in element[2:]]

print(elements)

print("ok")
