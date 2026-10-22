# Sets in Python 
"Collection of unordered, unindexed, and mutable data types that do not allow duplicate elements."

'1. add() - adds an element to the set'
set = {1, 2, 3}
set.add(4)  # Add an element to the set
print(set)  # Output: {1, 2, 3, 4}

'2. clear() - removes all the elements from the set'
set = {1, 2, 3}
set.clear()  # Remove all elements from the set
print(set)  # Output: set()

'3. copy() - returns a shallow copy of the set'
set1 = {1, 2, 3}
set2 = set1.copy()  # Return a shallow copy of the set
print(set2)  # Output: {1, 2, 3}

'4. union() - returns a set containing the union of two or more sets'
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

'5. intersection() - returns a set containing the intersection of two or more sets'
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))  # Output: {3, 4}

'6. difference() - returns a set containing the difference between two or more sets'
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.difference(set2))  # Output: {1, 2}

'7. remove() - removes the specified element from the set'
set = {1, 2, 3}
set.remove(2)  # Remove the element 2 from the set
print(set)  # Output: {1, 3}

'8. pop() - removes and returns an arbitrary element from the set'
set = {1, 2, 3}
element = set.pop()  # Remove and return an arbitrary element from the set
print(element)  # Output: 1 (or 2 or 3)
print(set)  # Output: {2, 3}

