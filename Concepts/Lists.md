# 📘 Lists in Python

## 1. Definition
- A **list** in Python is a **collection of ordered, mutable (changeable) items**.  
- It can hold different types of elements (integers, strings, floats, objects, even other lists).  
- Lists are written using **square brackets `[]`**.

---

## 2. Example
```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

numbers = [10, 20, 30, 40]

mixed = [1, "hello", 3.5, True]   # list with different data types
```

---

## 3. Properties of Lists
1. **Ordered** → Elements have a defined order, and that order will not change.  
2. **Mutable** → You can change, add, or remove items after the list is created.  
3. **Allows duplicates** → Lists can store the same value multiple times.  

```python
fruits = ["apple", "banana", "apple"]
print(fruits)   # ['apple', 'banana', 'apple']
```

---

## 4. Accessing List Elements
- You can access elements by **index** (starting from `0`).

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (negative index = from end)
```

---

## 5. Common List Operations
```python
fruits = ["apple", "banana", "cherry"]

# Add elements
fruits.append("orange")       # add at end
fruits.insert(1, "mango")     # add at index 1

# Remove elements
fruits.remove("banana")       # remove by value
fruits.pop(0)                 # remove by index (0th element)
del fruits[1]                 # delete element at index 1

# Update elements
fruits[0] = "grape"

print(fruits)
```

---

## 6. Useful List Methods
```python
numbers = [5, 2, 9, 1, 7]

print(len(numbers))      # length of list
numbers.sort()           # sort list
numbers.reverse()        # reverse order
print(numbers.index(9))  # index of element
print(numbers.count(2))  # count occurrences
```

---

## 7. Nested Lists (Lists inside Lists)
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])      # [1, 2, 3]
print(matrix[1][2])   # 6 (2nd row, 3rd element)
```

---

## ✅ Summary
- Lists are **ordered, mutable, allow duplicates**, and can store multiple data types.  
- They are one of the most commonly used data structures in Python.  
