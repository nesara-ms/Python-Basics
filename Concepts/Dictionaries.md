# Dictionaries in Python

## What is a Dictionary?
A **dictionary** in Python is an **unordered, mutable collection of key-value pairs**.  
Each value is accessed using its **key**, not by index.

---

## Syntax
```python
# Creating a dictionary
my_dict = {
    "name": "NehaGowda",
    "age": 20,
    "course": "Engineering"
}

# Empty dictionary
empty_dict = {}
```
---

## Characteristics
- **Unordered** → Items don’t have a fixed position.
- **Mutable** → You can add, update, and remove items.
- **Keys must be unique** (no duplicates).
- **Keys must be immutable** (string, number, tuple).
- **Values can be of any data type**.

---

## Accessing Elements
```python
student = {"name": "Nagarjun", "age": 21, "course": "Engineering"}

print(student["name"])       # NehaGowda
print(student.get("age"))    # 20

# Using get with default value
print(student.get("grade", "N/A"))  # N/A (since "grade" does not exist)
```
---

## Modifying Dictionary
```python
student = {"name": "NehaGowda", "age": 20}

# Add new key-value pair
student["course"] = "Engineering"

# Update value
student["age"] = 21

# Remove a key-value pair
del student["age"]

# pop()
student.pop("course")

print(student)
```
---

## Dictionary Methods
```python
person = {"name": "Alice", "age": 25, "city": "Paris"}

print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 25, 'Paris'])
print(person.items())   # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Paris')])

# Iterating
for key, value in person.items():
    print(key, ":", value)

# Clear all items
person.clear()
```
---

## Example Program
```python
marks = {"Math": 90, "Science": 85, "English": 88}

total = sum(marks.values())
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
```
**Output:**
```
Total Marks: 263
Average Marks: 87.66666666666667
```

---

## Key Points
- Dictionary is best for **mapping data**.
- Fast lookups using keys.
- Useful for **JSON data** and **real-world datasets**.
