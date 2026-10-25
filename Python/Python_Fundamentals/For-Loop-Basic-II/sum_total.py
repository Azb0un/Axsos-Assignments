def sum_total(myList):
    total = 0
    for i in range(len(myList)):
        total += myList[i]
    return total

print(sum_total([1,2,5,9,3]))