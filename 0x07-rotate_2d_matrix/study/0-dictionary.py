#!/usr/bin/env python3
"""Dictionary examples"""

contacts = {'lawal': 801, 'emma': 234}
contacts['shola'] = 456
print(contacts)
print(contacts['lawal'])

del contacts['shola']
contacts['samson'] = 789
print(contacts)

listed_contacts = list(contacts)
print(listed_contacts)