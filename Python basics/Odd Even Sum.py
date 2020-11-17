n = int(input())
even_sum = 0
odd_sum = 0
lst = []

for i in range(n):
    number = int(input())
    lst.append(number)

for j in range(n):
    if j % 2 == 0:
        even_sum += lst[j]
    else:
        odd_sum += lst[j]

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(odd_sum - even_sum)}')