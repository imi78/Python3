def last_even_count(num_list):
    last_even = []
    num_list = num_list[:: -1]
    count = 0
    if int(command[1]) == count:
      print(last_even)
      return
    if int(command[1]) > len(num_list):
        print('Invalid count')
        return
    else:
        last_even = [i for i in num_list if i % 2 == 0]
        print(last_even[:int(command[1])])
        return

num_list = [2, 4, 6, 1, 4]
command = 'first 2'.split(' ')
last_even_count(num_list)