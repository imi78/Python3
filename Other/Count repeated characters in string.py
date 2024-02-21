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
