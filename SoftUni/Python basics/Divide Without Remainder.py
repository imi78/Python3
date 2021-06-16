n = int(input())

p2 = 0
p3 = 0
p4 = 0

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        p2 += 1
    if number % 3 == 0:
        p3 += 1
    if number % 4 == 0:
        p4 += 1


print (f'{p2 / n * 100:.2f}%')
print (f'{p3 / n * 100:.2f}%')
print (f'{p4 / n * 100:.2f}%')
