import math

gender = input()
weight = float(input())
height = float(input())*100
age = int(input())
physical_activity = input()

BNM_male = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
BNM_female = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

if physical_activity == 'sedentary':
    BNM_male *= 1.2
    BNM_female *= 1.2
elif physical_activity == 'lightly active':
    BNM_male *= 1.375
    BNM_female *= 1.375
elif physical_activity == 'moderately active':
    BNM_male *= 1.55
    BNM_female *= 1.55
elif physical_activity == 'very active':
    BNM_male *= 1.725
    BNM_female *= 1.725
if gender == 'm':
    print(f'To maintain your current weight you will need {math.ceil(BNM_male)} calories per day.')
else:
    print(f'To maintain your current weight you will need {math.ceil(BNM_female)} calories per day.')