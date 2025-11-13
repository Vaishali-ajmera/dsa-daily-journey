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

```
## List of major questions
| #   | Pattern                                | Problem                                                                                                                             | Why It’s Important                                     |
| --- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| 1️⃣ | **Basic Stack Simulation**             | [LeetCode 20 – Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                                                 | Teaches basic push/pop logic, bracket matching         |
| 2️⃣ | **Min Stack / Track Minimum**          | [LeetCode 155 – Min Stack](https://leetcode.com/problems/min-stack/)                                                                | Learn to maintain auxiliary stack for min tracking     |
| 3️⃣ | **Next Greater Element**               | [LeetCode 496 – Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)                                      | Introduces monotonic stack pattern                     |
| 4️⃣ | **Next Greater Element II (Circular)** | [LeetCode 503 – Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)                                    | Extend monotonic stack with circular logic             |
| 5️⃣ | **Remove Adjacent Duplicates**         | [LeetCode 1047 – Remove All Adjacent Duplicates in String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | Stack for string reduction pattern                     |
| 6️⃣ | **Decode String / Expression Parsing** | [LeetCode 394 – Decode String](https://leetcode.com/problems/decode-string/)                                                        | Nested stack use – handling brackets and repetition    |
| 7️⃣ | **Evaluate Reverse Polish Notation**   | [LeetCode 150 – Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)                  | Stack for expression evaluation pattern                |
| 8️⃣ | **Largest Rectangle in Histogram**     | [LeetCode 84 – Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)                       | Hardest monotonic stack classic                        |
| 9️⃣ | **Daily Temperatures**                 | [LeetCode 739 – Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)                                              | Practice “Next Greater Element” variation              |
| 🔟  | **Asteroid Collision**                 | [LeetCode 735 – Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)                                              | Real-world simulation with direction-based stack logic |


