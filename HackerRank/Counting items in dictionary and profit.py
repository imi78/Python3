# receives pairs of shoes and sizes
shoes = int(input())
sizes = list(map(int, input().split(" ")))
# transfers th list into a dict with key, value pairs
dict = {}
count = 1
for i in sizes:
    if i not in dict:
        dict[i] = count
    else:
        dict[i] = dict.get(i)+1

# how many customers the store has and sets the profit
customers = int(input())
profit = 0
for number in range(customers):
    size, amount = map(int, input().split(" ")) 

# checks if item is in the dictionary and sets the value and profit
    if size in dict and dict[size] > 0:
        dict[size] -=1
        profit += amount
        
print(profit)

######################################################
# with itertools library
#####################################################
from collections import Counter
