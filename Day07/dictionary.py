#dictionary methods

'1. clear() - removes all the elements from the dictionary'
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict1.clear()  # Clear all elements from the dictionary
print(dict1)  # Output: {}

'2. copy() - returns a shallow copy of the dictionary'
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = dict1.copy()  # Create a shallow copy of the dictionary
print(dict2)  # Output: {'a': 1, 'b': 2, 'c': 3}

'3. fromkeys() - creates a new dictionary with keys from an iterable and values set to a specified value'
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict3 = dict.fromkeys(keys, values)  # Create a new dictionary with the specified keys and values
print(dict3)  # Output: {'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]}    

'4. get() - returns the value for the specified key if the key is in the dictionary'
dict1 = {'a': 1, 'b': 2, 'c': 3}
value = dict1.get('b')  # Get the value for key 'b'
print(value)  # Output: 2

'5. items() - returns a view object that displays a list of a dictionarys key-value tuple pairs'
dict1 = {'a': 1, 'b': 2, 'c': 3}
items = dict1.items()  # Get the key-value pairs as tuples
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

'6. keys() - returns a view object that displays a list of all the keys in the dictionary'
dict1 = {'a': 1, 'b': 2, 'c': 3}
keys = dict1.keys()  # Get the keys of the dictionary
print(keys)  # Output: dict_keys(['a', 'b', 'c'])

'7. pop() - removes the item with the specified key and returns its value'
dict1 = {'a': 1, 'b': 2, 'c': 3}
value = dict1.pop('b')  # Remove the item with key 'b' and return its value
print(value)  # Output: 2
print(dict1)  # Output: {'a': 1, 'c': 3}

'8. popitem() - removes and returns the last inserted key-value pair as a tuple'
dict1 = {'a': 1, 'b': 2, 'c': 3}
item = dict1.popitem()  # Remove and return the last inserted key-value pair
print(item)  # Output: ('c', 3)
print(dict1)  # Output: {'a': 1, 'b': 2}

'9. setdefault() - returns the value of a key if it is in the dictionary, otherwise inserts the key with a specified value'
dict1 = {'a': 1, 'b': 2, 'c': 3}
value = dict1.setdefault('d', 4)  # Get the value for key 'd', or insert it with value 4 if it doesn't exist
print(value)  # Output: 4
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

'10. update() - updates the dictionary with the key-value pairs from another dictionary or iterable'
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4}
dict1.update(dict2)  # Update dict1 with key-value pairs from dict2
print(dict1)  # Output: {'a': 1, 'b': 20, 'c': 3, 'd': 4}

'11. values() - returns a view object that displays a list of all the values in the dictionary'
dict1 = {'a': 1, 'b': 2, 'c': 3}
values = dict1.values()  # Get the values of the dictionary
print(values)  # Output: dict_values([1, 2, 3])

