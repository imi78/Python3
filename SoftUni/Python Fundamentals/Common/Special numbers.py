n = int(input())
sum = 0

for i in range(1, n+1):
  first_digit = i % 10
  second_digit = i // 10
  sum  = first_digit + second_digit
  
  if sum == 5 or sum == 7 or sum == 11:
    print (f'{i} -> True')
  else:
    print (f'{i} -> False')