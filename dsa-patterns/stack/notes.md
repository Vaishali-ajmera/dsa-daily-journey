# 🧱 Stack - Notes

## 🎯 What & Why
A **Stack** is a **linear data structure** that follows the **LIFO (Last In, First Out)** principle.  
Think of it like a stack of plates — the last plate placed on top is the first one removed.

We use stacks when we need to **reverse order**, **track operations**, or **handle nested structures** (like parentheses or recursive calls).  
Common operations are:
- **Push:** Add an element on top.
- **Pop:** Remove the top element.
- **Peek/Top:** View the top element without removing it.

---

## 🔍 When to Use (Pattern Recognition)
**Keywords:**  
`LIFO`, `Undo/Redo`, `Balanced Brackets`, `Next Greater Element`, `Expression Evaluation`, `Backtracking`, `Recursive Simulation`

**Problem Types:**  
- Check for **balanced parentheses**
- Implement **browser history** or **undo stack**
- Find **Next Greater Element**
- Convert **infix to postfix**
- Perform **DFS manually** without recursion

---

## 💡 How It Works (Intuition)
Imagine stacking plates vertically:
- You can only **add** or **remove** from the **top**.  
- The most recently added plate is always the **first to be removed**.  
This structure helps when you need to **reverse or backtrack** through actions.

## Time Complexity
Time complexity for all major operations:  
✅ Push → O(1)  
✅ Pop → O(1)  
✅ Peek → O(1)


## 📝 Python Implementation
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)   # Add item to top

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove top item
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]   # View top item
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
