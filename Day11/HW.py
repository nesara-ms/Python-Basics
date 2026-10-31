#Example 1-Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

foods = ["pasta","fried rice","biryani"]
upper_case = [food.upper() for food in foods]
print(upper_case)

#Example 2-Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.

stationary_price = {"pen":10, "book":25,"eraser":5,"scale":10,"pencil": 6}
total_price =0
for value in stationary_price.values():
    total_price += value
print(total_price)

#Example 3-Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.
numbers = [1,2,3,4,5,6,7,8,9,10]
squares = [num ** 2 for num in numbers]
print(squares)

#Example 4-Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.
students = [
    {"name": "Neha", "age": 20, "marks": 85},
    {"name": "Kushal", "age": 22, "marks": 90},
    {"name": "Karuna", "age": 19, "marks": 88}
]
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

#Example 5- Write a Python program that takes a list of lists (a 2D list) as input and:
#Prints the entire matrix row by row.
#Prints the sum of each row in the matrix.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    print(row)
    print("Sum of row:", sum(row))