
info = {'person':
            {'age': '28', 'hair': 'brown', 'eyes': 'blue', 'tattoos': 'No'},
        'person_details':
            {'title': 'accountant', 'Position': 'Lead', 'level': 'senior'},
        'account':
            {'corporate': None, 'personal': None}
        }


for val in info.values():
    for k, v in val.items():
        print(f'{k} --> {v}')
        print('--------------')

# d = [val for val in info.values() for k, v in val.items()]
# print(d)

#######           Comprehension not working as expected            #####

