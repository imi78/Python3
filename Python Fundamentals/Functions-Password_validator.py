def password_validator(password):
    num = 0  # numbers counter
    is_valid = True  # conditions flag for further processing outside this function

    if not 6 <= len(password) <= 10:   # checks 1st condition
        print("Password must be between 6 and 10 characters")
        is_valid = False # sets flag

    for char in password: # checks for each symbol if it is digit or letter
        if char.isdigit():
            num += 1  # counts digits in the password
        if not char.isalnum():  # checks if there is a special character
            print('Password must consist only of letters and digits')
            is_valid = False
            break
    if num < 2:
        print('Password must have at least 2 digits')
        is_valid = False
    return is_valid


pswd = input()
is_valid = password_validator(pswd)

if is_valid:
    print('Password is valid')
