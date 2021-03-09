# Task
#
# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#
# Input Format
#
# A single line containing a string .
#
# Constraints
#
#
# Output Format
#
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
#

#  for ANY method you need an iterable, that's why for loop is used... The method itself returns True or False

if __name__ == '__main__':
    str = input()
    print (any(c.isalnum() for c in str))
    print (any(c.isalpha() for c in str))
    print (any(c.isdigit() for c in str))
    print (any(c.islower() for c in str))
    print (any(c.isupper() for c in str))