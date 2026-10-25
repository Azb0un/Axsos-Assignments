#1 we build functions to get a return, so i guess the output is 5
def a():
    return 5
print(a())

#2 i guess it will be 10 
def a():
    return 5
print(a()+a())

#3 return work as a door in function so everything after it will not be reached so the answer is 5 i guess
def a():
    return 5
    return 10
print(a())

#4 its the same as 3. any thing after return will not be reached 
def a():
    return 5
    print(10)
print(a())
#5 i think its error since function has no value to return
def a():
    print(5)
x = a()
print(x)

#6 none plus none is error
def a(b,c):
    print(b+c)
#print(a(1,2) + a(2,3))

#7 the answer is 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8 our if statement has return so 7 will not be reached, and since b is not <10 the answer will be 100, 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9 the 3 will not be reached so the answers will be 7,14,21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10 the answer is 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11 the answer is 500, 500, 300, 500 because the function will run only if we call it
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12 the answer is 500 500 300 500 , the return will not print anything, it will save a value only
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13 the answer is 500 500 300 300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14 the only function that was called is a so it will be 1 3 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15 the only function that was called is a again , so it will be 1,3,5,10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)