def getCount(lst):
  res = 0 # count the similar rectangles
  rows = len(lst)
  
  for i in range(rows): # 0,1,2,3
    for j in range(i+1, rows): # 1, 2, 3
      if lst[i][0] / lst[j][0] == lst[i][1] / lst[j][1]:
        res += 1
                                
  return res
 
# Driver Code
if __name__ == '__main__':
  
  rows = int(input()) # shows how many nested lists will be made
  lst = []
  for _ in range(rows): 
    # [ [4, 8], [10, 20] ] , etc. 
    lst.append(list(map(int, input().split(" "))))
    
  # if printed -> lst =  [[4, 8], [10, 20], .......]
  print(getCount(lst))