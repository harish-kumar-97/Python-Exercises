# Python program to update character of a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a character of the String
# String1[2] = 'p' # will cause error
print("\nUpdating character at 2nd Index: ")
print(String1)

#################################################
print()
print()
# update entire string
print("update entire string")
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)

##################################################
print()
print()
# Python program to delete characters from a String
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a character of the String
# del String1[2] # causes error
print("\nDeleting character at 2nd Index: ")
print(String1)

###############################################
# Deleting Entire String
# Python program to Delete entire String
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a String with the use of del
del String1
print("\nDeleting entire String: ")
# print(String1) # will result in error as 'String1' was deleted

################################################
# Python program Escape sequencing of String
# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quotes
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)

# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)
