# Sliding Window Technique

The **Sliding Window** technique is used to efficiently solve problems involving **contiguous subarrays or substrings** by maintaining a dynamic range between two pointers (`left` and `right`) instead of recomputing values repeatedly.

---

## When to Use Sliding Window?

Use this technique when:

- Working with **subarrays (arrays)** or **substrings (strings)**
- Problem involves words like:
  - "longest"
  - "shortest"
  - "maximum"
  - "minimum"
  - "count"
  - "at most / at least"
- You are dealing with **continuous elements where order matters**

---

## Core Idea

The sliding window approach follows this pattern:

- Start with an **empty or minimal window**
- Expand the window by moving the `right` pointer
- Check if the current window satisfies the condition
- If the condition becomes invalid:
  - Shrink the window by moving the `left` pointer
- Continuously track the best possible answer during the process

---

## Why Use Sliding Window?

- Avoids nested loops in subarray/substring problems
- Reduces time complexity from **O(n²) → O(n)**
- Efficient for real-time range-based calculations
- One of the most common interview patterns

---

## Common Problems

- Maximum sum subarray of size k
- Longest substring without repeating characters
- Minimum window substring
- Subarray sum equals K
- Smallest subarray with sum ≥ target

---

## Summary

Sliding Window is a powerful optimization technique that helps process contiguous data efficiently by dynamically expanding and shrinking a window while maintaining required conditions.
