lst = [1, 2, 3, 4, 5, 6, 1, 2, 4, 3, 2, 1]
dct = {}
for i in lst:
    dct[i] = dct.get(i, 0) + 1
  

print('Original list', lst)
print('Counted items in dict', dct)