
# swaping two variables
a = 10
b = 20

print("Before swapping: a =", a, ", b =", b)

a= a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)

# another way to swap two variables
c = 30
d = 40

print("Before swapping using temp: c =", c, ", d =", d)

temp = c
c = d
d = temp

print("After swapping using temp: c =", c, ", d =", d)

# simple greeting program

name = input("Enter your name: ")
age = int(input("enter your age: "))

print("Hello", name, "! You are", age, "years old.")

# string manipulation example

sentence = "Hello, World!"

print("Original sentence:", sentence)

print(sentence.upper())  # Convert to uppercase

print(sentence.lower()) # Convert to lowercase

print(sentence.split()) # Split into words

print(sentence.replace("World", "Python"))  # Replace a word

print(sentence.find("World"))  # Find the index of a word

print(sentence.count("o"))  # Count occurrences of a character

#  comparison operators example

age = int(input("Enter your age: "))

if age == 0:
    print("You are a newborn!")
elif age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")