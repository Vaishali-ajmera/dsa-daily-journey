## Problem 2: Max Consecutive Ones III (1004)

### Pattern: Variable-Size Sliding Window

# **Intuition:**  
# Expand window to include more 1’s. Count zeros.  
# If zeros > k, shrink from the left until zeros ≤ k.

# **Algorithm:**  
# 1. Use two pointers `left`, `right`  
# 2. Expand `right`, count zeros  
# 3. Shrink from `left` if zeros > k  
# 4. Track max window length

# **Time Complexity:** O(n)  
# **Space Complexity:** O(1)

# **Python Code:**
# ```python
def longestOnes(nums, k):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_len = max(max_len, right - left + 1)
    return max_len
