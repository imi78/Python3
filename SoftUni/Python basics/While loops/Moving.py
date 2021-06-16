width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
command = input()

while command != 'Done':
    boxes = int(command)
    volume -= boxes
    if volume <= 0:
        print (f'No more free space! You need {abs(volume)} Cubic meters more.')
        break
    command = input()

print (f'{abs(volume)} Cubic meters left.')
