# dict = {'orange': 'портокал', 'car': 'кола'}
# # second = {'cat': 'котка', 'dog': 'куче'}
# for k, v in {'cat': 'котка', 'dog': 'куче'}.items():
#   dict.update({k:v})


# print(dict['cat'], dict['orange'])
# print(dict['dog'])

shoes = int(input())

sizes = list(map(int, input().split(" ")))

dict = {}
count = 1
for i in sizes:
    if i not in dict:
        dict[i] = count
    else:
        dict[i] = dict.get(i)+1

customers = int(input())
profit = 0
for number in range(customers):
    size, amount = map(int, input().split(" ")) 
    if size in dict and dict[size] > 0:
        dict[size] -=1
        profit += amount
        
print(profit)