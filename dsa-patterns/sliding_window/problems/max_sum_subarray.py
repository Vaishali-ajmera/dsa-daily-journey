### Pattern: Fixed-Size Sliding Window
# **Problem:** Maximum Average Subarray I (643)

# **Idea:** Maintain running sum for size k window. Slide window by removing first element, adding next element.  

# **Time Complexity:** O(n)  
# **Space Complexity:** O(1)  



# Brute Force Approach
# Time Complexity: o(n*k)

from typing import List 

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        for i in range(len(nums) - k + 1):
            window_sum = sum(nums[i:i+k])
            max_avg = max(max_avg, window_sum / k)
        return max_avg
    

# Optimized approach
# Time Complexity: o(n)
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k