````markdown
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
````

✅ **Pros:**

* Easiest to use
* O(1) push/pop for operations at end
* No extra imports

❌ **Cons:**

* Not thread-safe
* No overflow/underflow checks
* Can misuse list operations like insert/remove and break efficiency

---

## 🥈 2. Using `collections.deque` (Recommended for Production)

`deque` (double-ended queue) gives **O(1)** time for append/pop from both ends and is more efficient for stack/queue use.

```python
from collections import deque

stack = deque()

stack.append('A')
stack.append('B')
stack.append('C')

print(stack[-1])   # Peek top → C
print(stack.pop()) # Pop top → C
print(stack.pop()) # Pop top → B
```

✅ **Pros:**

* Thread-safe for appends/pops
* Better performance for large data
* Cleaner and faster than list

❌ **Cons:**

* Slightly more syntax (`from collections import deque`)

---

## 🥉 3. Using a Custom Class (OOP Approach)

Good for interviews and clarity — lets you define stack operations explicitly.

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example use
s = Stack()
s.push(1)
s.push(2)
print(s.peek())   # 2
print(s.pop())    # 2
print(s.is_empty())  # False
```

✅ **Pros:**

* Encapsulated structure (cleaner design)
* Easy to extend for custom operations (e.g., Min Stack, Max Stack)
* Good for interview explanations

❌ **Cons:**

* Slightly more verbose

---

## ⚙️ Time Complexity

| Operation   | List | Deque | Custom Class |
| ----------- | ---- | ----- | ------------ |
| Push        | O(1) | O(1)  | O(1)         |
| Pop         | O(1) | O(1)  | O(1)         |
| Peek        | O(1) | O(1)  | O(1)         |
| Check Empty | O(1) | O(1)  | O(1)         |

---

## 🧠 Pro Tip

If you’re just solving coding problems — **use list**.
If you’re building an app or library — **use deque**.
If you’re in an **interview** — **use custom class** (shows understanding).

---
