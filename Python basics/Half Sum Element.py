import sys
n = int(input())
max_num = -sys.maxsize
total_sum = 0

for i in range(n):
    number = int(input())
    if number > max_num:
        max_num = number
    total_sum += number

other = total_sum - max_num
f = max_num - other

if other == max_num:
    print (f'Yes\nSum = {max_num}')
else:
    print (f'No\nDiff = {abs(f)}')