import random

def word_list():
  words = []
  f = open('5_letter_words.txt','r')

  for line in f:
    words.append(line.strip())
  return words


def random_word(lst):
  random_item = random.choice(lst)
  return random_item


def is_real_word(guess, lst):
  if guess in lst:
    return True
  else:
    return False


def check_guess(guess, word):
    word = list(word)
    result = ["_"] * len(word)
    
 # check for exact matches chars
    for i, l in enumerate(guess):
        if l == word[i]:
            result[i] = "X"
            word[i] = " "
        
     # check for chars are at wrong position    
    for i, l in enumerate(guess):
        if l in word:
            if result[i] != "X":
                result[i] = "O"
                word[word.index(l)] = " "
    
    return "".join(result)


def next_guess(words):
  user_guess = input().lower()

  while user_guess:
    if user_guess in words:
      return user_guess
      break
    else:
      user_guess = input().lower()


def play():
  count = 1
  wrd_lst = word_list()
  random_wrd = random_word(wrd_lst)
   
  while count <= 6:
      
    guess = input("Please enter a guess: ")
    real_word = is_real_word(guess, wrd_lst)
    
    if count >= 6:
      print("You lost!")
      print(f"The word was: {random_wrd}")
      break
  
    if real_word == True:
      check_user_guess = check_guess(guess,random_wrd)
      print(check_user_guess)
      
      if check_user_guess == "XXXXX":
        print("You won!")
        break
      count += 1
      continue
      
    else:
        print("That's not a real word!")
        count += 1
        continue
 
    
play()
