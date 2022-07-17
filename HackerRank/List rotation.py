def list_rotation(lst, n):
  
  # Rotate the last element to index [0] n times
  for i in range(n):
    
    # if lenght of the list is equal to the rotation cycles it shoud return the same list
    if n == len(lst):   
      return(lst)
      break
      
      # or cut the last element, add it at index[0] and replace the original list
    else:
      lst = lst[-1:] + lst[:-1]
  return lst

if __name__ == '__main__':
  lst = [0,1,4,4,5,6,7]
  n = 6
  print(list_rotation(lst, n))
  