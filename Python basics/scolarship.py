income = float(input())
avg_grade = float(input())
min_salary = float(input())

social_scholarship = min_salary * 35 / 100
grade_scholarship = avg_grade * 25

if income < min_salary and avg_grade >= 4.5:
    print(f'You get a Social scholarship {social_scholarship} BGN')

elif avg_grade >= 5.5:
    print(f'You get a scholarship for excellent results {grade_scholarship} BGN')

else:
    print(f'You cannot get a scholarship!')
