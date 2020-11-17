n = int(input())
even_sum = 0
odd_sum = 0
# lst = []

for i in range(n):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number