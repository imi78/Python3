journal = input().split(', ')

command = input()

while command != 'Craft!':
  command, item = command.split(' - ')
  
  if command == 'Collect':
    if item not in journal:
      journal.append(item)

  elif command == 'Drop':
    if item in journal:
      journal.remove(item)
    else:
      pass

  elif command == 'Combine Items':
    item = item.split(':')
    if item[0] in journal:
      journal.insert(journal.index(item[0])+1, item[1])
    

  elif command == 'Renew':
    if item in journal:
      journal.append(journal.pop(journal.index(item)))
    

  command = input()
  
print(', '.join(journal))