# dict = {'orange': 'портокал', 'car': 'кола'}
# # second = {'cat': 'котка', 'dog': 'куче'}
# for k, v in {'cat': 'котка', 'dog': 'куче'}.items():
#   dict.update({k:v})


# print(dict['cat'], dict['orange'])
# print(dict['dog'])

from itertools import product


A = list(map(int, (input()).split(' ')))
B = list(map(int, (input()).split(' ')))

a = list(product((A), (B)))
for i in a:
    print (i, end=" ")