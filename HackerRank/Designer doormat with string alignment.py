n, m = map(int, input().split())
pattern = '.|.'

# print((pattern).center(m, '-'))
# print((pattern*3).center(m, '-'))

for i in range(0, n-1, 2):
    print((pattern*(i+1)).center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(n, 1, -2):
    print((pattern*(i-2)).center(m, '-'))