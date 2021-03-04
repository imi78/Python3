# n = int(input())
# phonebook = {}
# for _ in range(n):
#     phonebook_entry = input().split()  # takes 2 argv and removes the space between them
#     phonebook[phonebook_entry[0]] = phonebook_entry[1] # populate the dictionary with key, value pairs
# while True: # infinite loop
#     try:
#         query = input()
#         if query in phonebook:
#             print(f'{query}={phonebook.get(query)}')  # prints the needed name and the value fro the dict
#         else:
#             print('Not found')
#     except EOFError:  # or just 'except:' breaks the infinite loop
#         break
# # ---------------------------------------------------
n = int(input())
phonebook_entry = [input().split() for _ in range(n)]
phonebook = {k: v for k, v in phonebook_entry}
print(phonebook)
