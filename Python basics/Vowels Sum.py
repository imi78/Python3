n = input()
vowels = {'a':1, 'e':2, 'i':3 , 'o':4, 'u':5}
count = 0
for i in n:
    if i in vowels:
        count += vowels[i]
print(count)
