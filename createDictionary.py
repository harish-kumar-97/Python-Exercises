# create a dictionary with integer keys
Dict = {1: 'Geeks', 2: 'For', 3:'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# creating a dictionary with mixed keys
Dict = {'Name': 'Geeks', 1:[1, 2, 3, 4]}
print("\nDictionary with the use of mixed keys: ")
print(Dict)
print()
####################################################
# creating an empty dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# creating a dictionary with dict() method
Dict = dict({1: 'Geeks', 2:'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# creating a dictionary with each item as a pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair")
print(Dict)
####################################################
# creating a nested dictionary as shown in the below image
Dict = {1: 'Geeks', 2: 'For', 3:{'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)