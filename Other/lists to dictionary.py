from itertools import zip_longest  # combines two lists of different lenght

lst_1 = [1, 2, 3, 4, 5]
lst_2 = [10, 20, 30]
dict = {}

# добавяш листовете в речник

for k, v in zip_longest(lst_1, lst_2):
    dict[k] = v
  
# промяна на keys and values

dict[1] = 300  # тук променяш стойността 
dict['one'] = dict.pop(1)  # тук променяш ключа

# call the keys and values

print(dict['one'])  # с това викаш стойността на ключа 'one'
val = [v for k, v in dict.items() if k == 5] # stores the value of a given key
