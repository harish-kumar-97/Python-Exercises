# initial dictionary
Dict = {5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 'A' : {1 : 'Geeks', 2 : 'for', 3 : 'Geeks'}, 'B' : {1 : 'Geeks', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from nested dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

# remove elements using pop() method
pop_ele = Dict.pop(5)
print('\nDictionary after deletion using pop(): ' + str(Dict))
print('Value asssociated to popped key is: ' + str(pop_ele))

Dict.clear()
print("\nDictionary after clearing using clear()")
print(Dict)