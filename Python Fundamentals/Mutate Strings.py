str_1 = input()
str_2 = input()
current_string = ''
previous_string = str_1

for i in range(len(str_1)):
    for index_str_2 in range(0, i+1):
        current_string += str_2[index_str_2]
    for index_str_1 in range(i + 1, len(str_1)):
        current_string += str_1[index_str_1]

    if not previous_string == current_string:
        print(current_string)

    previous_string = current_string
    current_string = ''
