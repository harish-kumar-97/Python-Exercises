# Python program to demonstrate creation of list

# creating a list
List = []
print(List)

# creating a list of strings
List = ['GeeksForGeeks', 'Geeks']
print(List)

# Creating a Multi-Dimensional List
List = [['Geeks', 'For'], ['Geeks']]
print(List)

# adding element to a list
List = []
# using append
List.append(1)
List.append(2)
print(List)
# using insert()
List.insert(3, 12)
print(List)
List.insert(0, 'Geeks')
print(List)
# using extend()
List.extend([8, 'Geeks', 'Always'])
print(List)

# accessing elements from the list
List = [1, 2, 3, 4, 5, 6]
# accessing elements from the list
print(List[0])
print(List[2])
# negative indexing
# print the last element of list
print(List[-1])
# print the third last element of list
print(List[-3])


# removing elements from a list
# using remove() method
List.remove(1)
print(List)
# using pop()
List.pop()
print(List)
List.pop()
print(List)