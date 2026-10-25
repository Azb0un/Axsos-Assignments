def ultimate_analysis(myList):
    total = 0
    smallest = myList[0]
    biggest = myList[0]
    count = 0

    for value in myList:
        total += value
        count += 1
        if value < smallest:
            smallest = value
        if value > biggest:
            biggest = value

    return {
        'sumTotal': total,
        'average': total / count,
        'minimum': smallest,
        'maximum': biggest,
        'length': count
    }

print(ultimate_analysis([37, 2, 1, -9]))