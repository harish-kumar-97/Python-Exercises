# program to illustrate if statement
i = 10
if (i > 15):
    print("10 is less than 15")
print("I am NOT in if")

print('\n')

# program to illustrate if else statement
#!/usr/bin/python
i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if block")
else:
    print("i is greater than 15")
    print("i'm in else block")
print("i'm not in if and not in else block")

print('\n')
# program to illustrate nested if statement
#!/usr/bin/python
i = 10
if(i == 10):
    # first if statement
    if (i < 15):
        print("i is smaller than 15")
    # nested-if statement
    # will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")


print('\n')
# program to illustrate if-else-else ladder
#!/usr/bin/python
i = 20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")

print('\n')
# program to illustrate short hand if
i = 10
if i < 15: print("i is less than 15")

print('\n')
# short hand if-else statement
i = 10
print(True) if i < 15 else print(False)

