n, m = map(int, input().split())
pattern = '.|.'

# print((pattern).center(m, '-'))
# print((pattern*3).center(m, '-'))

for i in range(0, n-1, 2):  # first rows with the pattern
    print((pattern*(i+1)).center(m, '-'))

print('WELCOME'.center(m, '-'))  # prints in the middle

for i in range(n, 1, -2):  # last rows with pattern
    print((pattern*(i-2)).center(m, '-'))