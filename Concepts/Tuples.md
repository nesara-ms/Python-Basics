# Tuples in Python

## What is a Tuple?
A **tuple** in Python is an ordered, immutable collection of items.  
This means once a tuple is created, you cannot change (add, remove, or modify) its elements.

---

## Syntax
```python
# Creating a tuple
my_tuple = (1, 2, 3)

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.5)

# Tuple with nested list
nested_tuple = (1, [2, 3], (4, 5))

# Single element tuple (must have a comma)
single_element = (10,)
```
---

## Characteristics
- **Ordered** → Items have a fixed order.
- **Immutable** → Cannot be modified after creation.
- **Allows duplicates** → Same values can appear multiple times.
- **Can contain different data types**.

---

## Accessing Elements
```python
numbers = (10, 20, 30, 40, 50)

print(numbers[0])   # First element → 10
print(numbers[-1])  # Last element → 50

# Slicing
print(numbers[1:4])  # (20, 30, 40)
```
---

## Tuple Operations
```python
# Concatenation
a = (1, 2)
b = (3, 4)
print(a + b)  # (1, 2, 3, 4)

# Repetition
print(a * 3)  # (1, 2, 1, 2, 1, 2)

# Membership test
print(2 in a)  # True
```
---

## Tuple Methods
```python
fruits = ("apple", "banana", "cherry", "apple")

print(fruits.count("apple"))  # 2 → Counts occurrences
print(fruits.index("banana")) # 1 → Returns index of first occurrence
```
---

## Example Program
```python
student = ("NehaGowda", 20, "Engineering")

# Unpacking tuple
name, age, course = student

print(f"Name: {name}, Age: {age}, Course: {course}")
```
**Output:**
```
Name: NehaGowda, Age: 20, Course: Engineering
```

---

## Key Points
- Tuples are **faster** than lists (due to immutability).
- Good for **fixed collections** of data.
- Commonly used for **returning multiple values** from a function.
