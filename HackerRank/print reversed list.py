N = int(input())
arr = list(map(int, input().strip().split()))


if len(arr) <= N:
    
    arr.reverse()
    
    for i in arr:
        print(i, end=' ')
# -------- or -------
print(" ".join(map(str, arr[::-1])))
