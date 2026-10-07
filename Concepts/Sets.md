# 📘 Sets in Python

## 1. Definition
- A **set** in Python is a **collection of unordered, unindexed, unique items**.  
- Sets are written using **curly braces `{}`** or the `set()` function.  
- They automatically **remove duplicate values**.  

---

## 2. Example
```python
# Creating sets
fruits = {"apple", "banana", "cherry"}

numbers = {1, 2, 3, 4, 5}

# Using set() constructor
letters = set(["a", "b", "c", "a"])
print(letters)   # {'a', 'b', 'c'} (duplicates removed)
```

---

## 3. Properties of Sets
1. **Unordered** → Elements have no defined order.  
2. **Unindexed** → You cannot access elements using an index (like lists/tuples).  
3. **No duplicates** → Each value appears only once.  
4. **Mutable** → You can add or remove items after a set is created.  

---

## 4. Accessing Elements
Since sets are **unordered**, you can’t access items by index.  
Instead, you can loop through them:

```python
fruits = {"apple", "banana", "cherry"}

for f in fruits:
    print(f)
```

---

## 5. Common Set Operations
```python
fruits = {"apple", "banana", "cherry"}

# Add elements
fruits.add("orange")

# Add multiple elements
fruits.update(["mango", "grape"])

# Remove elements
fruits.remove("banana")   # raises error if not found
fruits.discard("kiwi")    # does not raise error if not found
fruits.pop()              # removes a random element
```

---

## 6. Set Operations in Mathematics
Python sets support **union, intersection, difference, symmetric difference**.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        # {1, 2, 3, 4, 5, 6}
print(a.intersection(b)) # {3, 4}
print(a.difference(b))   # {1, 2}
print(b.difference(a))   # {5, 6}
print(a.symmetric_difference(b))  # {1, 2, 5, 6}
```

---

## 7. Frozen Sets
- A **frozenset** is an **immutable version of a set** (you cannot add or remove elements).  

```python
frozen = frozenset([1, 2, 3, 2, 1])
print(frozen)  # frozenset({1, 2, 3})
```

---

## ✅ Summary
- **Set** = unordered, unindexed, unique collection of elements.  
- Used when you want to avoid duplicates and perform **mathematical set operations** like union and intersection.  
