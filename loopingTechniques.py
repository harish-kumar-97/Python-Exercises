# python code to demonstrate working of enumerate()
for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)


print('\n')
# python code to demonstrate working of enumerate()
for key, value in enumerate(['Geeks', 'for', 'Geeks', 'is', 'the', 'Best', 'Coding', 'Platform']):
    print(value, end=' ')

print('\n')
# python code to demonstrate working of zip()
# initializing list
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

print('\n')
# using zip() to combine two containers and print values
for question, answer in zip(questions, answers):
    print('What is your {0}? I am {1}.'.format(question, answer))

print('\n')
# program to demonstrate working of items()
king = {'Akbar' : 'The Great', 'Chandragupta' : 'The Maurya', 'Modi' : 'The Changer'}

# using items to print the dictionary key-value pair
for key, value in king.items():
    print(key, value)

print('\n')
# program to demonstrate the working of sorted()
# initializing list
list1 = [1, 3, 5, 6, 2, 1, 3]

# using sorted() to print the list in sorted order
print("The list in sorted order is: ")
for i in sorted(list1):
    print(i, end=" ")
print("\r")

# using sorted() and set() to print the list in sorted order
# use of set() removes duplicates
print("The list in sorted order (without duplicates) is : ")
for i in sorted(set(list1)):
    print(i, end=" ")

print('\n')
# initializing list
basket = [ 'guava', 'orange', 'apple', 'pear', 'guava', 'banana', 'grape']
# using sorted() and set() to print the list in sorted order
for fruit in sorted(set(basket)):
    print(fruit)

print('\n')
#  program to demonstrate the use of reversed()
# initializing list
print("The list in reversed order is: ")
for i in reversed(basket):
    print(i, end=" ")