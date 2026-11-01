#Functions in python are defined using the def keyword. They can take parameters and return values. Here's a simple example of a function that adds two numbers:
def add_numbers(a, b):
    return a + b

# Example usage:
result = add_numbers(5, 3)
print(result)  # Output: 8

#Average of numbers in a list
def average(numbers):
    return sum(numbers) / len(numbers)

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(average(numbers))  # Output: 3.0

#product of numbers in a list
def product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(product(numbers))  # Output: 120