import sys
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
    max_odd_index = -1
    max_odd = -sys.maxsize
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            if num_list[i] >= max_odd:
                max_odd = num_list[i]
                max_odd_index = i
    if max_odd_index == -1:
        print('No matches')
    else:
        print(max_odd_index)


def get_max_even(num_list): 
    max_even_index = -1
    max_even = -sys.maxsize
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            if num_list[i] >= max_even:
                max_even = num_list[i]
                max_even_index = i
    if max_even_index == -1:
        print('No matches')
    else:
        print(max_even_index)


def get_min_odd(num_list): 
    min_odd_index = -1
    min_odd = sys.maxsize
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            if num_list[i] <= min_odd:
                min_odd = num_list[i]
                min_odd_index = i
    if min_odd_index == -1:
        print('No matches')
    else:
        print(min_odd_index)


def get_min_even(num_list):
    min_even_index = -1
    min_even = sys.maxsize
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            if num_list[i] <= min_even:
                min_even = num_list[i]
                min_even_index = i
    if min_even_index == -1:
        print('No matches')
    else:
        print(min_even_index)


def first_even_count(num_list):
    first_even = []
    count = 0
    if int(command[1]) == count:
        print(first_even)
        return
    if int(command[1]) > len(num_list):
        print('Invalid count')
        return
    else:
        first_even = [i for i in num_list if i % 2 == 0]
        print(first_even[:int(command[1])])
        return


def first_odd_count(num_list):
    first_odd = []
    count = 0
    if int(command[1]) == count:
        print(first_odd)
        return
    if int(command[1]) > len(num_list):
        print('Invalid count')
        return
    else:
        first_odd = [i for i in num_list if i % 2 == 1]
        print(first_odd[:int(command[1])])
        return


def last_even_count(num_list):
    last_even = []
    count = 0
    if int(command[1]) == count:
        print(last_even)
        return
    if int(command[1]) > len(num_list):
        print('Invalid count')
        return
    else:
        last_even = [i for i in num_list if i % 2 == 0]
        print(last_even[-int(command[1]):])
        return


def last_odd_count(num_list):
    last_odd = []
    count = 0
    if int(command[1]) == count:
        print(last_odd)
        return
    if int(command[1]) > len(num_list):
        print('Invalid count')
        return
    else:
        last_odd = [i for i in num_list if i % 2 == 1]
        print(last_odd[-int(command[1]):])
        return


while command[0] != 'end':
    if command[0] == "exchange":
        index = int(command[1])
        array = exchange(array, index)

    elif command[0] == 'max':
        if command[1] == 'odd':
            get_max_odd(array)
        elif command[1] == 'even':
            get_max_even(array)

    elif command[0] == 'min':
        if command[1] == 'odd':
            get_min_odd(array)
        elif command[1] == 'even':
            get_min_even(array)

    elif command[0] == 'first':
        if command[2] == 'even':
            first_even_count(array)
        elif command[2] == 'odd':
            first_odd_count(array)

    elif command[0] == 'last':
        if command[2] == 'even':
            last_even_count(array)
        elif command[2] == 'odd':
            last_odd_count(array)

    command = input().split(' ')

print(array)
