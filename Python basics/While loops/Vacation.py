money_needed = float(input())
money_owned = float(input())

days_spent = 0
days_count = 0

while money_owned < money_needed:
    action = input()
    amount = float(input())
    days_count += 1

    if action == 'save':
        money_owned += amount
        days_spent = 0

    elif action == 'spend':
        days_spent += 1
        if (money_owned - amount) > 0:
            money_owned -= amount
        else:
            money_owned = 0
        if days_spent == 5:
            print(f'You can\'t save the money.')
            print(days_count)
            break
if money_owned >= money_needed:
    print (f'You saved the money for {days_count} days.')