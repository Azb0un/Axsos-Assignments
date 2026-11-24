

def rec_sigma(n):
    if n == 0:
        return 0;
    else:
        if n > 0:
            return n + rec_sigma(n-1)
        else:
            return n + rec_sigma(n + 1)

print(rec_sigma(-5))

def factorial(n):
    if n == 0:
        return 1
    else:
        if n > 0:
            return n * factorial(n-1)
        else:
            return n * factorial(n+1)

print(factorial(-4))

