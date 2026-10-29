def larger(a, b):
    if a == b:
        print("They are equal")
        return a
    elif a > b:
        return a
    else:
        return b

print(larger(3, 8))
print(larger(7, 7))