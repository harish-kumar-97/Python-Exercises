my_string = "Cisco"
for each_vendor in my_string:
    print(each_vendor)
    print(each_vendor * 2)
    print(each_vendor * 3)
    
    
r = range(10)
for i in r:
    print(i * 2)
    

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
len(vendors)
list(range(5))
for element_index in range(len(vendors)):
    print(vendors[element_index])
    
for index, element in enumerate(vendors):
    print(index, element)
    
for element in vendors:
    print(element)
else:
    print("The end of the list has been reached")