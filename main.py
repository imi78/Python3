def first_odd_count(num_list):
    first_odd = []
    count = 0
    if int(command[1]) == count:
      print(first_odd)
      return
    if int(command[1]) > len(num_list):
        print('Invalid count')
        return
    else:
        first_odd = [i for i in num_list if i % 2 == 1]
        count += 1
        if count == int(command[1]):
          print(first_odd[:int(command[1])])
          return




num_list = [1, 3, 5, 7, 9]
command = 'first 4'.split(' ')

first_odd_count(num_list)

