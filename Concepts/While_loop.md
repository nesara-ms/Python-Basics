# While Loop in Python  

## What is a While Loop?  
A **while loop** in Python is used to repeatedly execute a block of code **as long as a given condition is `True`**.  
When the condition becomes `False`, the loop stops.  

---

## Syntax
```python
while condition:
    # Code block
    # Update condition (otherwise loop may run forever)
```
---

## Example 1: Basic While Loop
```python
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1
```
**Output:**
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

---

## Example 2: Infinite Loop
⚠️ Be careful! If the condition never becomes `False`, the loop runs forever.  
```python
while True:
    print("This will run forever!")  # Stop using Ctrl+C
```
---

## Example 3: Using `break`
```python
num = 1

while num <= 10:
    if num == 5:
        break  # Exit loop
    print(num)
    num += 1
```
**Output:**
```
1
2
3
4
```

---

## Example 4: Using `continue`
```python
num = 0

while num < 5:
    num += 1
    if num == 3:
        continue  # Skip this iteration
    print(num)
```
**Output:**
```
1
2
4
5
```

---

## Example 5: While with Else
```python
x = 1

while x <= 3:
    print("x =", x)
    x += 1
else:
    print("Loop finished")
```
**Output:**
```
x = 1
x = 2
x = 3
Loop finished
```

---

## Key Points
- Use while loop when **number of iterations is not fixed**.  
- Always make sure the loop has a **stopping condition** to avoid infinite loops.  
- `break`, `continue`, and `else` can be used inside while loops.  
