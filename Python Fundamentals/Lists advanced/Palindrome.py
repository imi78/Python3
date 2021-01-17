words = input().split(' ')
searched_word = input()
palindrome = [word for word in words if word == word[:: -1]]

if searched_word == searched_word[:: -1]:
  occ = palindrome.count(searched_word)
  print(f'Found palindrome {occ} times')
  
else:
  print('Searched word is not palindrome')
