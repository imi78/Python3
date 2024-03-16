a = ['aabbcc', 'ddeff', 'ghijkk']
count = 1
d = {}
for i in a:
    for j in i:
        if count >= len(i):
            continue
        if j not in d:
            d[j] = 1
        if j == i[count]:
            d[j] += 1
        count +=1
    count =1


# l = ['aabbcc', 'ddeff', 'ghijkk']
# d = {}
# for i in l:
#     for j in i:
#         d[j] = d.get(j, 0) + 1

# for k,v in d.items():
#     print(f"{k} --> {v}")
