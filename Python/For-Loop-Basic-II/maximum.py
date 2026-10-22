def maximum(myList):
    if len(myList) == 0:
        return False
    highest = myList[0]
    for value in myList:
        if value > highest:
            highest = value
    return highest

print(maximum([37,2,1,-9]))
print(maximum([]))