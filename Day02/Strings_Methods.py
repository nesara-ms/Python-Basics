# String Methods in Python

# 1. len() - Returns the length of the string
text = "Hello, World!"
print(len(text))  # Output: 13

# 2. lower() - Converts the string to lowercase
print(text.lower())  # Output: hello, world!

# 3. upper() - Converts the string to uppercase
print(text.upper())  # Output: HELLO, WORLD!

# 4. strip() - Removes whitespace from the beginning and end of the string
text_with_whitespace = "   Hello, World!   "
print(text_with_whitespace.strip())  # Output: Hello, World!

# 5. split() - Splits the string into a list of substrings
print(text.split(","))  # Output: ['Hello', ' World!']

# 6. join() - Joins a list of strings into a single string
words = ["Python", "is", "awesome"]
print(" ".join(words))  # Output: Python is awesome

# 7. replace() - Replaces a substring with another substring
print(text.replace("World", "Python"))  # Output: Hello, Python!

# 8. find() - Returns the index of the first occurrence of a substring
print(text.find("World"))  # Output: 7

# 9. count() - Returns the number of occurrences of a substring
print(text.count("l"))  # Output: 3

# 10. startswith() - Checks if the string starts with a specified prefix
print(text.startswith("Hello"))  # Output: True

# 11. endswith() - Checks if the string ends with a specified suffix
print(text.endswith("World!"))  # Output: True

# 12. capitalize() - Capitalizes the first character of the string
print(text.capitalize())  # Output: Hello, world!