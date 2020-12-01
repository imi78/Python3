nums = list(map(int, input().split(', '))) # преобразува user input-a в int.
 # и го слага в сисък

evens = [num for num in nums if num % 2 == 0] # намира четните числа
odds = [num for num in nums if not num % 2 == 0] # намира нечетните числа
print(evens)
print(odds)
