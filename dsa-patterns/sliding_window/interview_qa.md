# Sliding Window — Interview Q&A (Day 1)

---

## 1. Conceptual Questions

**Q1.** What is the Sliding Window pattern?  
**A.** It’s a technique for solving problems involving *contiguous* subarrays or substrings by maintaining a “window” that slides across input instead of recalculating from scratch.

**Q2.** When should you think of Sliding Window?  
**A.** Whenever the problem says:
- contiguous subarray/substring
- find max/min/sum/length/count
- condition grows or shrinks gradually

**Q3.** Why does it improve performance?  
**A.** Because it reuses previous work — adding one new element and removing one old element instead of recomputing everything. Each element is visited at most twice ⇒ **O(n)**.

---

## 2. Brute Force vs Optimized

**Q4.** What is the brute force approach?  
**A.** Check every possible subarray → nested loops → O(n²).

**Q5.** What’s the optimized approach?  
**A.** Move two pointers (`start`, `end`) to expand and shrink a *window*, maintaining partial results on the fly → O(n).

**Q6.** How do you decide if the window is fixed-size or variable-size?  
**A.**  
- Fixed-size: when k (window length) is given.  
- Variable-size: when the condition depends on data (sum ≥ S, at most K distinct chars).

---

## 3. Implementation Deep Dives

**Q7.** Why do we use `if end >= k - 1` for fixed-size?  
**A.** To ensure the window has reached full size before updating the result and then sliding it forward.

**Q8.** What happens if you forget to decrement the left element (`arr[start]`)?  
**A.** The window sum or frequency map will keep growing → wrong results.

**Q9.** Why do we delete keys from the map when count == 0?  
**A.** To ensure we know exactly how many distinct elements are in the current window (important for K distinct problems).

**Q10.** Can Sliding Window handle negative numbers in sum problems?  
**A.** Only safely for non-negative numbers. If negatives exist, shrinking logic can break → use prefix sums or Kadane’s algorithm instead.

---

## 4. Edge & Trick Questions

**Q11.** What if K = 0 or array is empty?  
**A.** Return 0 (or handle as invalid input).

**Q12.** What’s the max number of times each element is processed?  
**A.** Twice — once when added, once when removed ⇒ O(2n) ≈ O(n).

**Q13.** How to debug if your window over-shrinks?  
**A.** Print start, end, window state, and condition checks at each step. Watch if start passes end prematurely.

**Q14.** How do you adapt this for a string problem (instead of array)?  
**A.** Replace numeric updates with frequency maps (dict/Counter) for character tracking.

---

## 5. Scenario-Based Qs

**Q15.** The interviewer says: “Find the longest substring with at most K distinct characters.”  
→ Recognize: variable-size sliding window + frequency map.

**Q16.** “Find the max sum subarray of size K.”  
→ Recognize: fixed-size sliding window + rolling sum.

**Q17.** “Minimum size subarray with sum ≥ S.”  
→ Recognize: variable-size sliding window (shrink until sum < S).

**Q18.** “Longest substring without repeating characters.”  
→ Sliding window with a hash set or frequency map, shrink when duplicate found.

---

## 6. Short Interview Script (use this to explain)

> “The brute force solution checks every subarray in O(n²).  
> But we can observe that subarrays overlap, so instead of recomputing, we can maintain a window that slides — add the next element on the right, remove the one on the left when it exceeds our condition.  
> This way, each element is processed at most twice, giving O(n) time.  
> It’s called the Sliding Window pattern and is used for contiguous sequence problems like max sum, K distinct, or min length subarrays.”

---

## ⭐ Quick Recap:
| Type | Example | Condition | Complexity |
|------|----------|------------|-------------|
| Fixed-size | Max sum subarray of size K | window length fixed | O(n) |
| Variable-size | Smallest subarray with sum ≥ S | condition-based | O(n) |
| Character window | Longest substring ≤ K distinct | frequency map | O(n) |

---

## Common Follow-ups
- How to modify for circular arrays? (Use modulo indexing or double array)
- Can we parallelize? (Usually no; it’s sequential by nature)
- How to extend to 2D matrix? (Use prefix sums or Kadane on columns)

---
