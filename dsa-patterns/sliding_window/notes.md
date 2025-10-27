# Sliding Window Pattern — Notes (Day 1)

## 1. Overview
Sliding Window: use when you must find something (sum/length/count/substring) over a **contiguous** block of an array/string. Move a window (start..end) and update state incrementally.

## 2. Easy Intuition
Think of a window that slides over the array: when you move right, add the new element; when you move left, remove the old element. This avoids recomputing overlapping work.

## 3. Brute-force Approach
- Try every possible window: for start in 0..n-1, for end in start..n-1, evaluate property.
- Time complexity: O(n^2) (or O(n^2 * k) if inner work is O(k)).
- Space: O(1) (if no extra data structures).

## 4. Optimized (Sliding Window)
- Maintain `start` and `end`.
- Expand with `end` (add arr[end] to state).
- Shrink with `start` while condition requires it.
- Each element enters and leaves window at most once → O(n).
- Time complexity: O(n). Space: O(1) or O(alphabet) for frequency maps.

## 5. Two main variants
1. Fixed-size window (size k) — e.g., maximum sum of size k.  
2. Variable-size window (condition-based) — e.g., smallest subarray with sum >= S or longest substring with ≤ K distinct chars.

## 6. Templates (Python)

### Fixed-size window (size = k)
```python
def max_sum_subarray(arr, k):
    # returns maximum sum of any contiguous subarray of size k
    n = len(arr)
    if n < k or k <= 0:
        return 0  # or appropriate value per problem

    start = 0
    window_sum = 0
    max_sum = -float('inf')

    for end in range(n):
        window_sum += arr[end]
        if end >= k - 1:    # window has k elements
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum
