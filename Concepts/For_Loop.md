# For Loop in Python  

## What is a For Loop?  
A **for loop** in Python is used to **iterate over a sequence** (like a list, tuple, string, dictionary, or range) and execute a block of code for each element.  

It is commonly used when the **number of iterations is known** or when looping through a collection.  

---

## Syntax
```python
for variable in sequence:
    # Code block
```
---

## Example 1: Iterating over a List
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

---

## Example 2: Iterating over a String
```python
for char in "NehaGowda":
    print(char)
```
**Output:**
```
N
e
h
a
G
o
w
d
a
```

---

## Example 3: Using `range()`
```python
for i in range(5):
    print(i)
```
**Output:**
```
0
1
2
3
4
```

---

## Example 4: Loop with Step
```python
for i in range(1, 10, 2):
    print(i)
```
**Output:**
```
1
3
5
7
9
```

---

## Example 5: Using `break` and `continue`
```python
for i in range(1, 6):
    if i == 3:
        continue  # Skip 3
    if i == 5:
        break     # Stop loop
    print(i)
```
**Output:**
```
1
2
4
```

---

## Example 6: For with Else
```python
for i in range(3):
    print("Iteration", i)
else:
    print("Loop finished")
```
**Output:**
```
Iteration 0
Iteration 1
Iteration 2
Loop finished
```

---

## Key Points
- Use **for loop** when iterating over sequences or when number of iterations is known.  
- Works with **lists, tuples, strings, dictionaries, sets, and ranges**.  
- Can use `break`, `continue`, and `else`.  
