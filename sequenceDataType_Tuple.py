# Python program to demonstrate the creation of a set

# creating an empty tuple
Tuple1 = ()
print(Tuple1)
# creating a tuple of strings
print(('Geeks', 'For'))

# creating a tuple of list
print(tuple([1, 2, 3, 4, 5]))

# creating a nested tuple
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

# accessing element of a tuple
tuple1 = tuple([1, 2, 3, 4, 5])
# accessing element using indexing 
print(tuple1[0])
# accessing element using negative indexing
print(tuple1[-1])

# deleting or updating elements of tuple is not possible as they are immutable in Python
tuple1 = tuple([1, 2, 3, 4, 5])
# updating an element
tuple1[0] = -1
# deleting an element
del tuple1[2]
