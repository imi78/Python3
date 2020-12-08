def factorial(n1, n2):
    factorial1 = 1
    factorial2 = 1
    for num1 in range(1, n1 + 1):
        factorial1 *= num1
    for num2 in range(1, n2 + 1):
        factorial2 *= num2
    total = f"{factorial1 / factorial2:.2f}"
    return total


print(factorial(int(input()), int(input())))
