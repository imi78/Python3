def add_and_subtract(a, b, c):
    sum1 = sum_numbers(a, b)
    sub = subtract(sum1, c)
    return sub


def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))