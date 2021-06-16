substrings = input().split(', ')
words = input().split(', ')
result = [substring for substring in substrings for word in words if substring in word]


print(sorted(set(result), key=result.index))