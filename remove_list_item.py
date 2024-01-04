#remove specific item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#remove specific index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#remove last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


#remove first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#clear list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)