type = input()
row = int(input())
column = int(input())
capacity = row*column

if type == 'Premiere':
    income = capacity*12
elif type == 'Normal':
    income = capacity * 7.50
elif type == 'Discount':
    income = capacity * 5.00
print(f'{income:.2f} leva')
