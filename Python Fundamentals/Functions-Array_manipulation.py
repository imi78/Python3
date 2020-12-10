import sys
array = input().split(" ")
array = list(map(int, array))
command = input().split(' ')


def exchange(num_list, index):  # Done! Tested!
    if 0 <= index < len(num_list):
        start = num_list[0:index + 1]
        end = num_list[index + 1:]
        exchanged_array = end + start
        return exchanged_array
    else:
        print("Invalid index")
        return num_list


def get_max_odd(num_list):  # Done! Tested!
    max_odd = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            if num_list[i] > max_odd:
                max_odd = i
        else:
            return 'No matches'
    return max_odd


def get_max_even(num_list):  # Done! Tested!
    max_even = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            if num_list[i] > max_even:
                max_even = i
        else:
            return 'No matches'
    return max_even


def get_min_odd(num_list):  # Done! Tested!
    min_odd = sys.maxsize
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            if num_list[i] < min_odd:
                min_odd = i
        else:
            return 'No matches'
    return min_odd


def get_min_even(num_list):  # Done! Tested!
    min_even = sys.maxsize
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            if num_list[i] < min_even:
                min_odd = i
        else:
            return 'No matches'
    return min_even


def first_even_count(num_list):  # Done! Tested!
    first_even = []
    count = 0
    if int(command[1]) > len(num_list):
        return 'Invalid count'
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            first_even.append(num_list[i])
            count += 1
            if count == int(command[1]):
                return first_even
    return first_even


def first_odd_count(num_list):  # Done! Tested!
    first_odd = []
    count = 0
    if int(command[1]) > len(num_list):
        return 'Invalid count'
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            first_odd.append(num_list[i])
            count += 1
            if count == int(command[1]):
                return first_odd

    return first_odd


def last_even_count(num_list):
    last_even = []
    num_list = num_list[:: -1]
    count = 0
    if int(command[1]) > len(num_list):
        return 'Invalid count'
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            last_even.append(num_list[i])
            count += 1
            if count == int(command[1]):
                return last_even[:: -1]
    return last_even[:: -1]


def last_odd_count(num_list):
    last_odd = []
    num_list = num_list[:: -1]
    count = 0
    if int(command[1]) > len(num_list):
        return 'Invalid count'
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            last_odd.append(num_list[i])
            count += 1
            if count == int(command[1]):
                return last_odd[:: -1]

    return last_odd[:: -1]


while command[0] != 'end':
    if command[0] == "exchange":  # Done!
        index = int(command[1])
        new_array = exchange(array, index)

    elif command[0] == 'max':  # Done!
        if command[1] == 'odd':
            odd_max = get_max_odd(array)
        elif command[1] == 'even':
            even_max = get_max_even(array)

    elif command[0] == 'min':  # Done!
        if command[1] == 'odd':
            odd_min = get_min_odd(array)
        elif command[1] == 'even':
            even_min = get_min_even(array)

    elif command[0] == 'first':  # Done!
        if command[2] == 'even':
            count_even = first_even_count(array)
        elif command[2] == 'odd':
            count_odd = first_odd_count(array)

    elif command[0] == 'last':
        if command[2] == 'even':
            last_count_even = last_even_count(array)
        elif command[2] == 'odd':
            last_count_odd = last_odd_count(array)

    command = input().split(' ')

print(new_array)
print(odd_max)
print(odd_min)
print(even_max)
print(even_min)
print(count_even)
print(count_odd)
print(last_count_even)
print(last_count_odd)
