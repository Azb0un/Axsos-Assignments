import random

def randInt(min=0, max=100):
    num = random.random() * (max - min) + min
    if min > max:
        min, max = max, min
    if max < 0:
        max = 0
    if min < 0:
        min = 0
    return round(num)


print(randInt())

print(randInt(max=50))

print(randInt(min=50))

print(randInt(min=50, max=500))

print(randInt(min=50, max=25))

print(randInt(min=0, max=-10))