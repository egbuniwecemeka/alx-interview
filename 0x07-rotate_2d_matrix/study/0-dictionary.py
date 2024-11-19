#!/usr/bin/env python3
"""Dictionary examples"""

contacts = {'lawal': 801, 'emma': 234}
contacts['shola'] = 456
print(contacts)
print(contacts['lawal'])

del contacts['shola']
contacts['samson'] = 789
print(contacts)

# Lists the keys available in the dictionary
listed_contacts = list(contacts)
print(listed_contacts)

# Sort the lists result
sort = sorted(listed_contacts)
print(sort)

# test membership of key in dictionary
test_membership = 'lawal' in sort
print(test_membership)

# test non-membership of key in dictionary
non_membership = 'lawal' not in sort
print(non_membership)

# dict() builds a dictionary from key:value pairs sequences
create_dict = dict([('a', 1), ('b', 2), ('c', 3)])
print(create_dict)

# Looping techniques - the items() method can be used in retrieving keys and methods in dictionaries
vals = [(k, v) for k, v in create_dict.items()]
print(vals)

# When looping through a sequenence the position index and corresponding value can be retrieved using the enumerate() function
seq = ['Officer', 'Artist', 'Doctor']
for i, v in enumerate(seq):
    print(i, v)

# Loop through multiple sequences using the zip method.
question = ['name']
answer = ['Manchester United']
for q, a in zip(question, answer):
    print(f'What is the {q} of your favourite club {a}')
