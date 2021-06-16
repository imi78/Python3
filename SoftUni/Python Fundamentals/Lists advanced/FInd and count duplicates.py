lst = [1, 3, 5, 7, 9, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9]

# d = {}
# count = 0
# for number in lst:
#     if number not in d:
#         d[number] = count
#     elif number in d:
#         # x = d.get(number) # get method returns the value of a given key
#         d[number] = (d.get(number) + 1)  # increase the value of dict value with one
# print(d)

#  Same thing with nested loops


def duplicates(numbers):
    for i in lst:
        for j in lst:
            if lst[i] == lst[j]:
                return True


print(duplicates(lst))
