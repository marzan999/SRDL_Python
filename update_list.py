#add extra item 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#nsert an item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#add another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)