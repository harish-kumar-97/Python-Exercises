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
# program to demonstrate working of iteritems(), items()
d = {"geeks" : "for", "only" : "geeks"}
# using iteritems to print the dictionary key-value pair
print("The key value pair using iteritems is: ")
for i,j in d.iteritems():
    print(i,j)
# using items to print the dictionary key-value pair
print("The key value pair using items is:")
for i,j in d.items():
    print(i,j)
