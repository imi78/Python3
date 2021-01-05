data = input()

to_do_list = {}

while data != 'End':
    data = data.split('-')
    priority = int(data[0])
    action = data[1]
    to_do_list.update({priority: action})
    data = input()

# to_do_list.sorted()
for key in sorted(to_do_list.keys()):

    print(key, to_do_list[key])

###################################################
# The program reads user input, split it and takes the
# digit as a priority and the rest as action
# then adds it to dictionary and prints it prioritized
#######################################################