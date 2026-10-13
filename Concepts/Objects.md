# Python Objects

In Python, **everything is an object**.

- An **object** is an instance of a class.
- Objects are created from classes, and they can hold **data (attributes)** and **functions (methods)**.

---

## Creating a Class and Object

```python
class Student:
    def __init__(self, name, age):
        self.name = name   # attribute
        self.age = age     # attribute

    def greet(self):       # method
        print("Hello, my name is", self.name)

# Create an object
s1 = Student("NehaGowda", 20)

# Access object data
print(s1.name)   # NehaGowda
print(s1.age)    # 20

# Call method
s1.greet()       # Hello, my name is NehaGowda
```

### Key Points

- Class → Blueprint

- Object → Instance of a class

- Objects can have attributes (variables inside class) and methods (functions inside class).

- Multiple objects can be created from the same class.
