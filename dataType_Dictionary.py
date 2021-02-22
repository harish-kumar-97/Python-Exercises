""" creating an empty Dictionary
"""
print("creating an empty Dictionary")
Dict = {}
print(Dict)

# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)

# with Mixed Keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict)

""" creating a nested dictionary
"""
print("Creating a nested dictionary")
Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)

""" adding elements to a Dictionary
"""
print("adding elements to a Dictionary")
# create an empty dictionary
Dict = {}
# adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict)
# updating existing key's value
Dict[2] = 'Welcome'
print(Dict)

""" accessing elements from a Dictionary
"""
print("Python program to demonstrate accessing an element from a Dictionary")
# creating a dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# accessing a element using key
print(Dict['name'])
# accessing a element using get()
print(Dict.get(3))


""" removing an element from Dictionary
"""
# Initial Dictionary
Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks', 'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'}}
# using pop
Dict.pop(5)
print(Dict)
# using popitem()
Dict.popitem()
print(Dict)
