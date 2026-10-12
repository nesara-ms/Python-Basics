#list methods

'01. append() - adds an element at the end of the list'
mylist = [1,2,3,4,5]
mylist.append(6)
print(mylist)

'02. extend() - adds the elements of a list (or any iterable), to the end of the current list'
mylist = [1,2,3,4,5]
mylist.extend([6,7,8])
print(mylist)

'03. insert() - adds an element at the specified position'
mylist = [1,2,3,4,5]
mylist.insert(2, 10)  # Insert 10 at index 2
print(mylist)

'04. remove() - removes the first item with the specified value'
mylist = [1,2,3,4,5]
mylist.remove(3)  # Remove the first occurrence of 3
print(mylist)

'05. pop() - removes the element at the specified position'
mylist = [1,2,3,4,5]
mylist.pop(2)  # Remove the element at index 2
print(mylist)

'06. clear() - removes all the elements from the list'
mylist = [1,2,3,4,5]
mylist.clear()  # Clear all elements from the list
print(mylist)

'07. index() - returns the index of the first element with the specified value'
mylist = [1,2,3,4,5]
index = mylist.index(3)  # Get the index of the first occurrence of 3
print(index)

'08. count() - returns the number of elements with the specified value'
mylist = [1,2,3,4,5,3,3]
count = mylist.count(3)  # Count occurrences of 3
print(count)

'09. sort() - sorts the list in ascending order'
mylist = [5,2,8,1,9]
mylist.sort()  # Sort the list in ascending order
print(mylist)

'10. reverse() - reverses the order of the list'
mylist = [1,2,3,4,5]
mylist.reverse()  # Reverse the order of the list
print(mylist)

'11. copy() - returns a shallow copy of the list'
mylist = [1,2,3,4,5]
newlist = mylist.copy()  # Create a shallow copy of the list
print(newlist)
