from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = deque()

        for ch in s:
            # Opening bracket → push
            if ch in "([{":
                stack.append(ch)

            else:
                # Closing bracket → check top match
                if not stack:
                    return False   # closing comes with no opening
                
                if stack[-1] != pairs[ch]:
                    return False   # mismatch
                
                stack.pop()

        return len(stack) == 0


# 📌 Time Complexity
# ✔ O(n)

# We process each character exactly once.

# 📌 Space Complexity
# ✔ O(n) worst-case

# If string is all openings "((([{{[" → stack stores all of them.