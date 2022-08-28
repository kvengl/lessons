def squirrel(N):
    nuts = getCountNuts(N)
    emeralds = getCountEmeralds(nuts)
    return emeralds

def getCountEmeralds(nuts):
    return getFirstDigit(nuts)

def getCountNuts(N):
    return factorial(N)

def getFirstDigit(number):
    while number > 9:
        number //= 10
    return number

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N - 1)