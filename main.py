def min_even_index(numbers, even):
    for i in range(len(numbers)):
        if numbers[i] % 2 == even:
            print(numbers[i])


num = [2, 4, 6, 1, 4]
command = 'odd'
min_even_index(num, 0 if command == "even" else 1)
