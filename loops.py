from __future__ import print_function
# program to illustrate while loop
count = 0
while(count < 3):
    count = count + 1
    print("Hello Geek")

###
print('\n')
# using else statement with while loops
count = 0
while(count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")

print('\n')
###
# Python program to illustrate single statement while block
"""
count = 0
while(count == 0): print("Hello Geek") # results in infinite loop
"""

# program to demonstrate for loop in python
n = 4
for i in range(0, n):
    print(i)

print('\n')
###
# program to illustrate 
#iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over a string
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" %(i, d[i]))

print('\n')
# iterating by index
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

print('\n')
# combining else with for
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")

print('\n')
# nested for loops in python
#from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


print('\n')
# program to illustrate 'continue' statement
# prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter:', letter)


print('\n')
# program to illustrate 'break' statement
for letter in 'geeksforgeeks':
    # break the loop as soon as it sees 'e' or 's'
    if letter == 'e' or letter == 's':
        break
print('Current Letter:', letter)

print('\n')
# program to illustrate 'pass' statement
for letter in 'geeksforgeeks':
    pass
print('Last Letter:', letter);
