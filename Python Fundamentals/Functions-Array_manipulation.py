array = input().split(" ")
array = list(map(int, array))
command = input().split(' ')


def exchange(num_list, index):
    if 0 <= index < len(num_list):
        start = num_list[0:index + 1]
        end = num_list[index + 1:]
        exchanged_array = end + start
        return exchanged_array
    else:
        print("Invalid index")
        return num_list


def get_max_odd(num_list):
    odd_list = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            odd_list.append(num_list[i])
    max_odd = max(odd_list)
    return max_odd


def get_max_even(num_list):
    even_list = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even_list.append(num_list[i])
    max_even = max(even_list)
    return max_even


def get_min_odd(num_list):
    odd_list = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            odd_list.append(num_list[i])
    min_odd = min(odd_list)
    return min_odd


def get_min_even(num_list):
    even_list = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even_list.append(num_list[i])
    min_even = min(even_list)
    return min_even


def first_even_count(num_list):  # if statements has to be introduced
    first_even = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            first_even.append(num_list[i])
    return first_even


def first_odd_count(num_list):  # if statements has to be introduced
    first_odd = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            first_odd.append(num_list[i])
    return first_odd


def last_even_count(num_list):   # if statements has to be introduced
    last_even = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            last_even.append(num_list[i])
    return last_even


def last_odd_count(num_list):   # if statements has to be introduced
    last_odd = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            first_odd.append(num_list[i])
    return first_odd


while command[0] != 'end':
    if command[0] == "exchange":
        index = int(command[1])
        new_array = exchange(array, index)

    elif command[0] == 'max':
        if command[1] == 'odd':
            odd_max = get_max_odd(array)
        elif command[1] == 'even':
            even_max = get_max_even(array)

    elif command[0] == 'min':
        if command[1] == 'odd':
            odd_min = get_min_odd(array)
        elif command[1] == 'even':
            even_min = get_min_even(array)

    elif command[0] == 'first':
        if command[2] == 'even':
            count_even = first_even_count(array)
        elif command[2] == 'odd':
            count_odd = first_odd_count(array)

    elif command[0] == 'last':
        if command[2] == 'even':
            count_even = last_even_count(array)
        elif command[2] == 'odd':
            count_odd = last_odd_count(array)

    command = input().split(' ')

print(new_array)
print(odd_max)
print(odd_min)
print(even_max)
print(even_min)
print(count_even)
print(count_odd)
