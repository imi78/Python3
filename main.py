command = input().split()
array = [1, 3, 5, 8, 9, 7, 6]
last_even = []
if command[0] == 'last':
    array = array[:: -1]
    count = int(command[1])
    el = 1
    if command[2] == 'even':
        for i in range(len(array)):
            if array[i] % 2 == 1:
                last_even.append(array[i])
                if el == count:
                    print(last_even[:: -1])
                    break
                else:
                    el += 1

# print(last_even)

