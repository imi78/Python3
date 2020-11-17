locations = int(input())

for i in range(locations):
    average = float(input())
    days = int(input())
    average_gold_per_day = 0
    for day in range(days):
        gold = int(input())
        average_gold_per_day += gold
    total_gold = (average_gold_per_day / days)
    if total_gold >= average:
        print(f'Good job! Average gold per day: {total_gold:.2f}.')
    else:
        print(f'You need {abs(total_gold-average):.2f} gold.')