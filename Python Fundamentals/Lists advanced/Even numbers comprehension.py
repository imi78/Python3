numbers = [int(el) for el in input().split(', ')]
evens = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

print(evens)