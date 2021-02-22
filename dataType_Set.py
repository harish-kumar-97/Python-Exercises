""" python program to demonstrate creation of
a Set in Python
"""
print("python program to demonstrate creation of a Set in Python")
# creating a Set
set1 = set()

# creating a Set of String
set1 = set("GeeksForGeeks")
print(set1)

# creating a Set of List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)


""" program to demonstrate adding elements in a Set
"""
print("program to demonstrate adding elements in a Set")
set1 = set()
# Adding to the Set using add()
set1.add(8)
set1.add((6, 7))
print(set1)

# Addition to the Set using Update()
set1.update([10, 11])
print(set1)

""" accessing elements in a Set
"""
print("program to demonstrate accessing elements in a Set")
# Creating a set
set1 = set(["Geeks", "For", "Geeks"])
# Accessing using for loop
for i in set1:
    print(i, end = " ")

""" removing elements from a Set
"""
print("python program to demonstrate deletion of elements in a Set")
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# using Remove() method
set1.remove(5)
set1.remove(6)
print(set1)

# using Discard() method
set1.discard(8)
set1.discard(9)
print(set1)

# set using the pop() method
set1.pop()
print(set1)

# set using clear() method
set1.clear()
print(set1)
