movie = input()

student = 0
standard = 0
kid = 0
total = 0
while movie != 'Finish':
    seats_available = int(input())
    type_of_ticket = input()

    while type_of_ticket != 'End':
        if type_of_ticket == 'student':
            student += 1
        elif type_of_ticket == 'standard':
            standard += 1
        elif type_of_ticket == 'kid':
            kid += 1
        elif type_of_ticket == 'Finish':
            print(f'{movie} - {total / seats_available * 100:.2f}% full.')
            movie = 'Finish'
            break
        total = student + standard + kid
        type_of_ticket = input()
    else:
        print(f'{movie} - {total / seats_available * 100:.2f}% full.')
        movie = input()
        continue
    # movie = input()
else:
    print(f'Total tickets: {total}')
    print(f'{student/total*100:.2f}% student tickets.')
    print(f'{standard/total*100:.2f}% standard tickets.')
    print(f'{kid/total*100:.2f}% kids tickets.')
