def average(myList):
    total = 0
    for i in range(len(myList)):
        total += myList[i]
    average = total / len(myList)
    return average

print(average([1,2,3,5,9]))