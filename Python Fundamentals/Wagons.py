wagons = int(input())

train = [0 for _ in range(wagons)]  # брой на вагоните
command = input()
while command != 'End':

    data = command.split()  # дели командата за да провери какво се дава
    if data[0] == 'add':
        people = int(data[1])
        train[-1] += people # индекса -1 означава последния елемент от списъка с вагоните

    elif data[0] == 'insert':
        index = int(data[1])
        people = int(data[2])
        train[index] += people
    elif data[0] == 'leave':
        index = int(data[1])
        people = int(data[2])
        train[index] -= people
    command = input()
print(train)
