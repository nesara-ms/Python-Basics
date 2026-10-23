#WAP to create a list and perform the following operations on it: insert, append, pop, remove, sort, reverse, index, display the length of the list, clear.

my_list = [10, 20, 30, 40,]
print(my_list)

my_list.insert(2, 25)  # Insert 25 at index 2
print("After insert:", my_list)

my_list.append(50)  # Append 50 to the end of the list
print("After append:", my_list)

my_list.remove(20)  # Remove the first occurrence of 20
print("After remove:", my_list)

print("length of the list:", len(my_list))  # Display the length of the list

popped_element = my_list.pop()  # Remove and return the last element
print("popped_element = ", popped_element)
print("After pop:", my_list)

my_list.sort()  # Sort the list in ascending order
print("After sort:", my_list)

my_list.reverse()  # Reverse the order of the list
print("After reverse:", my_list)  

my_list.index(30)  # Get the index of the first occurrence of 30
print("Index of 30:", my_list.index(30))

my_list.clear()  # Clear all elements from the list
print("After clear:", my_list)
