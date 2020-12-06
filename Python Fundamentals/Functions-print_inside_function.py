def char_in_range(a, b):
    for i in range(a + 1, b):
        print(chr(i), end=' ')


char1 = ord(input())
char2 = ord(input())
char_in_range(char1, char2)