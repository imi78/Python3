
def Factorial(n):
    if n <= 1:
        return 1
    else:
        sum = n * Factorial(n-1)
        return sum




print(Factorial(4))
