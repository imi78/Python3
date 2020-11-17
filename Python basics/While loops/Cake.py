width = int(input())
length = int(input())
total = width * length
pieces = 0
while True:
    command = input()
    if command == 'STOP':
        print(f'{total} pieces are left.')
        break
    else:
        command = int(command)
        total -= command
        pieces += command
        if total < 0:
            print(f'No more cake left! You need {pieces-width * length} pieces more.')
            break
