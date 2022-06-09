lst = [0,1,4,4,5,6,7]
n = 6

# Rotate the last element to index [0] n times
for i in range(n):
  # if lenght of the list is equal to the rotation cycles it shoud return the same list
    if n == len(lst):
        print(lst)
        break
      
      # or cut the last element, add it at index[0] and replace the original list
    else:
        lst = lst[-1:] + lst[:-1]
      
      # checks if the loop has finished to print the list
        if i == (n-1):
            print(lst)