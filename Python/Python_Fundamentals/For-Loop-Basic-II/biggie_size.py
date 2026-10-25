def biggieSize (myList):
    for i in range(len(myList)):
        if myList[i] > 0:
            myList[i] = "big"
    print(myList)

biggieSize([1,-5,-6,5,8])