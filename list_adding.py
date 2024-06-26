#Inserting at a specific index: Use the insert() method.
a = [1,2,3,4,5]
a.insert(1,1.2)
print(a)

#Extending a list at a specific index: Use slicing.
my_list = [1, 2, 3]
my_list[1:1] = [1.5, 1.75]  
print(my_list)