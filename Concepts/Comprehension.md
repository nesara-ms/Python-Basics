# Comprehensions in Python  

## What is Comprehension?
- **Comprehension** in Python is a **concise way to create collections** (like lists, sets, or dictionaries) using a single line of code.  
- It is more **readable and faster** than using loops to build collections.

---

## Types of Comprehensions

### 1. List Comprehension
Creates a **list** using a single line.

**Syntax:**
```python
[expression for item in iterable if condition]
```

**Example:**
```python
# Square numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Even numbers only
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]
```

---

### 2. Set Comprehension
Creates a **set**.

**Syntax:**
```python
{expression for item in iterable if condition}
```

**Example:**
```python
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # Output: {16, 1, 4, 9}
```

---

### 3. Dictionary Comprehension
Creates a **dictionary**.

**Syntax:**
```python
{key_expression: value_expression for item in iterable if condition}
```

**Example:**
```python
numbers = [1, 2, 3, 4]
squares_dict = {x: x**2 for x in numbers}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16}
```

---

### 4. Nested Comprehension
Comprehensions can be nested for more complex operations.

**Example:**
```python
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
```

---

## Key Points
- Comprehensions **make code shorter and cleaner**.  
- Can include **conditions** using `if`.  
- Can be used for **lists, sets, dictionaries**.  
- Avoid overly complex comprehensions for readability.  

---

💡 Analogy:
- Think of comprehensions like **a shortcut recipe**: you combine all ingredients (loop + condition) in a single step instead of multiple steps.
