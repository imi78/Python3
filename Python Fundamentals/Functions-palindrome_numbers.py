def palindrome(number):
    for digits in num:
        if digits[::] == digits[:: -1]:
            print('True')
        else:
            print('False')


num = input().split(', ')
palindrome(num)