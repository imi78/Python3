M = int(input())
N = int(input())

K = int(input())
L = int(input())
counter = 0
for first in range(M, 10):
    for second in range(9, N -1, -1):
        if first % 2 == 0 and second % 2 == 1:
            first_number = int(str(first) + str(second))
            for third in range(K, 10):
                for fourth in range(9, L -1, -1):
                    if third % 2 == 0 and fourth % 2 == 1:
                        second_number = int(str(third) + str(fourth))
                        if counter == 6:
                            break
                        else:
                            if first_number == second_number:
                                print('Cannot change the same player.')
                            else:
                                print(f'{first_number} - {second_number}')
                                counter += 1
