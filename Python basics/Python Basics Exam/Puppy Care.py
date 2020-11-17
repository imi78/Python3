food = int(input()) * 1000
counter = 0
while True:
    command = input()
    if command != 'Adopted':
        command = int(command)
        counter += command
    else:
        if counter > food:
            print(f'Food is not enough. You need {abs(food - counter)} grams more.')
            break
        else:
            print(f'Food is enough! Leftovers: {abs(food - counter)} grams.')
            break
