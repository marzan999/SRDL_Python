#6.1.5
#create a list and remove some items from the list and also add some items to the list

a = [1, 2, 3, 4, 5, 6, 7]  #main list
print(a)

a.pop()  #remove last item
print(a)

del a[3]  #remove 3rd index 
print(a)

a.append(8)  #add an item to the last index
print(a)

a.insert(2, 9)  #insert an item to a specific index
print(a)