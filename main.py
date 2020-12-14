num_list = [1, 3, 5, 7, 9]
command = 'first 1'.split(' ')
first_odd = []
count = 0
if int(command[1]) == count:
  print(first_odd)
if int(command[1]) > len(num_list):
    print('Invalid count')
    
    
else:
    for i in range(len(num_list)):
      if num_list[i] % 2 == 1:
          first_odd.append(num_list[i])
          count += 1
          if count == int(command[1]):
              print(first_odd)
              break




    # if len(first_odd) >= int(command[1]):
    #     print(first_odd)
    # else:
    #   print(first_odd)