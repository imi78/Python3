M = int(input())
N = int(input())

K = int(input())
L = int(input())

for first in range(M, 10):
  for second in range(9, N -1, -1):
      if first % 2 == 0 and second % 2 == 1:
          first_number = int(str(first) + str(second))
          for first in range(K, 10):
              for second in range(9, L -1, -1):
                  if first % 2 == 0 and second % 2 == 1:
                      second_number = int(str(first) + str(second))
                      if first_number == second_number:
                          print('Cannot change')
                      else:
                          print (f'{first_number} --> {second_number}')