# 🧩 Stack Implementation in Python

There are **3 main ways** to implement a stack in Python.  
Each has trade-offs in terms of **simplicity**, **performance**, and **control**.

---

## 🥇 1. Using Python List (Most Common)

Python’s built-in list already provides `append()` and `pop()` which behave like push/pop.

```python
# Stack using Python List
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

# Peek top
print(stack[-1])  # 30

# Pop element
print(stack.pop())  # 30 removed

# Check empty
print(len(stack) == 0)
