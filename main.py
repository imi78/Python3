num_list = [1, 3, 5, 7, 9]

command = 'last 5 odd'.split(' ')
last_even = []
num_list = num_list[:: -1]
count = 0

if int(command[1]) > len(num_list):
    print('Invalid count')

else:
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            last_even.append(num_list[i])
            count += 1
            if count == int(command[1]):
                break
    if len(last_even) >= int(command[1]):
        print(last_even[:: -1])
    else:
        print(last_even)