def perfect_number(number):
    sum = 0
    for num in range(1, number):
        if number % num == 0:
            sum += num
    if number == sum:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


number = int(input())
perfect_number(number)