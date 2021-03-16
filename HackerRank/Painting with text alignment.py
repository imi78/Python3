import string
alpha = string.ascii_lowercase  # whole alphabet with lowercase

n = 5   #int(input())

for i in range(n-1, 0, -1):  # the upper part. Loop is in reverse
    s = "-".join(alpha[i:n]) # makes the rigt part of the middle string
    l = s[::-1]  # right side of the middle part in reverse
    r = s[1:]  # left side of the middle string
    all = l+r  # the whole middle string
    print(all.center(4*n-3, '-'))  # the whole lenght of the string is 3 * n

for i in range(0, n+1):
    s = "-".join(alpha[i:n]) # makes the rigt part of the middle string
    l = s[::-1]  # right side of the middle part in reverse
    r = s[1:]  # left side of the middle string
    all = l+r  # the whole middle string
    print(all.center(4*n-3, '-'))  # the whole lenght of the string is 4 * n - 3
