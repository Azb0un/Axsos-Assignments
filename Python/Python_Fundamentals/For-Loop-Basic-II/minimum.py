def minimum(myList):
    if len(myList) == 0:
        return False
    smallest = myList[0]
    for value in myList:
        if value < smallest:
            smallest = value
    return smallest

print(minimum([37, 2, 1, -9]))
print(minimum([]))