s = 'hello   world      lol  3g'.split(' ')  # when you have a separator in split() it preserves the spaces between th words
# l = []                            ////
# for i in range(len(s)):           ////  loop to append the string in another list,
#     lst = s[i].capitalize()       ////  so the letters can be capitalized. if there is a non alphabetical character,
#     l.append(lst)                 ////  the next alphabetical is capitalized. This is why .title() cannot be used

lst = [s[i].capitalize() for i in range(len(s))]
print(' '.join(lst))
