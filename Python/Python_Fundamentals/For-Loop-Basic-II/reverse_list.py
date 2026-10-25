def reverse_list(myList):
    for i in range(len(myList) // 2):
        temp = myList[i]
        myList[i] = myList[len(myList) - 1 - i]
        myList[len(myList) - 1 - i] = temp
    return myList

print(reverse_list([37, 2, 1, -9]))