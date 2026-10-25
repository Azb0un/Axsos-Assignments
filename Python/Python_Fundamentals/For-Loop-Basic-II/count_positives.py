def count_positivies(myList):
    count = 0
    for i in range(len(myList)):
        if myList[i] > 0:
            count += 1
    myList[len(myList)-1] = count
    return myList
print(count_positivies([-1,1,1,1]))