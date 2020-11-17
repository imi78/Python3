bad_grades_count = int(input())

counter = 0
total_grades = 0
grades_count = 0
last_task_name = ''

name = input()
while name != 'Enough':
    grade = int(input())
    total_grades += grade
    grades_count += 1
    if grade <= 4:
        counter += 1

    if counter == bad_grades_count:
        break

    last_task_name = name
    name = input()

if name == 'Enough':
    print(f'Average score: {total_grades / grades_count:.2f}')
    print(f'Number of problems: {grades_count}')
    print(f'Last problem: {last_task_name}')
else:
    print(f'You need a break, {bad_grades_count} poor grades.')