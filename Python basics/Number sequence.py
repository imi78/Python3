n = int(input())
lst = []
for i in range(n):
    number = int(input())
    lst.append(number)

print(f'Max number: {max(lst)}')
print(f'Min number: {min(lst)}')
