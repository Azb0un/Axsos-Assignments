import random

def randInt(min=0, max=100):
    num = random.random() * (max - min) + min
    if min > max:
        min, max = max, min
    return round(num)


print(randInt())

print(randInt(max=50))

print(randInt(min=50))

print(randInt(min=50, max=500))

print(randInt(min=50, max=25))