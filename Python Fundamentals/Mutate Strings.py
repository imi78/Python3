str_1 = input()
str_2 = input()
str_3 = ''
counter = 1

for i in range(len(str_1)):
    for j in range(len(str_2)):
        str_3 = str_2[i:counter] + str_1[j+1:]
        if counter == len(str_1):
            break
        else:
            counter += 1
            print(str_3)
