def odd_and_even(number):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return odd_sum, even_sum


num = input()
j = odd_and_even(num)
print(f"Odd sum = {j[0]}, Even sum = {j[1]}")