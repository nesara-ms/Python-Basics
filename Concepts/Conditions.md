
# 🐍 Conditions in Python

In Python, **conditions** are statements that let your program make decisions — they check whether something is **true** or **false** and then perform actions based on that result.

---

## 💡 Example
```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

Here:
- `if` checks a **condition** → `age >= 18`
- If the condition is **True**, it runs the first block (`print("You are an adult.")`)
- Otherwise (`else`), it runs the second block.

---

## 🧠 Common Conditional Statements in Python

| Keyword | Meaning |
|----------|----------|
| `if` | Checks a condition |
| `elif` | Checks another condition if the previous one was false |
| `else` | Runs if none of the above conditions are true |

Example:
```python
marks = 85

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
else:
    print("Needs improvement")
```

---

## ⚙️ Comparison Operators (used in conditions)

| Operator | Meaning | Example | Result |
|-----------|----------|----------|---------|
| `==` | Equal to | `5 == 5` | True |
| `!=` | Not equal to | `5 != 3` | True |
| `>` | Greater than | `10 > 3` | True |
| `<` | Less than | `2 < 5` | True |
| `>=` | Greater than or equal to | `7 >= 7` | True |
| `<=` | Less than or equal to | `4 <= 9` | True |

---

## 🔗 Combining Conditions 

You can also combine conditions using:

- **and** → both must be True  
- **or** → at least one must be True  
- **not** → reverses True/False

Example:
```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can vote.")
```
