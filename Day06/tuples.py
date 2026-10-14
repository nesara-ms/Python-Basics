#tuples methods

'01. count() - returns the number of occurrences of a specified value in a tuple'
mytuple = (1, 2, 3, 4, 5, 3, 3)
count = mytuple.count(3)  # Count occurrences of 3
print(count)  # Output: 3

'02. index() - returns the index of the first occurrence of a specified value in a tuple'
mytuple = (1, 2, 3, 4, 5)
index = mytuple.index(3)  # Find index of first occurrence of 3
print(index)  # Output: 2

'03. len() - returns the number of elements in a tuple'
mytuple = (1, 2, 3, 4, 5)
length = len(mytuple)  # Get the number of elements in the tuple
print(length)  # Output: 5

'04. slicing - allows you to access a range of elements in a tuple'
mytuple = (1, 2, 3, 4, 5)
sliced_tuple = mytuple[1:4]  # Access elements from index 1 to 3
print(sliced_tuple)  # Output: (2, 3, 4)

'05. concatenation - allows you to combine two or more tuples'
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # Combine the two tuples
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

'06. repetition - allows you to repeat a tuple a specified number of times'
mytuple = (1, 2, 3)
repeated_tuple = mytuple * 3  # Repeat the tuple 3 times
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

'07. membership - allows you to check if an element exists in a tuple'
mytuple = (1, 2, 3, 4, 5)
is_present = 3 in mytuple  # Check if 3 is in the tuple
print(is_present)  # Output: True

'08. unpacking - allows you to assign the elements of a tuple to variables'
mytuple = (1, 2, 3)
a, b, c = mytuple  # Assign each element to a separate variable
print(a, b, c)  # Output: 1 2 3

'09. immutability - tuples are immutable, meaning their elements cannot be changed after creation'
mytuple = (1, 2, 3)
# mytuple[0] = 10  # This would raise an error since tuples are immutable

'10. nested tuples - tuples can contain other tuples as elements'
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))

