# Prefix Sum Technique

The **Prefix Sum** technique is used to preprocess an array so that range-based queries (like sum of elements between two indices) can be answered efficiently without recomputing values repeatedly.

It works by storing cumulative sums of the array, allowing fast calculation of subarray sums.

---

##  When to Use Prefix Sum?

Use this technique when:

- You need to answer **range sum queries**
- Problems involve **subarray sums**
- You see repeated sum calculations over different ranges
- You want to optimize brute force range queries
- Problems mention:
  - "sum of elements between L and R"
  - "subarray sum equals K"
  - "find equilibrium index"

---

##  Core Idea

The main idea is to build a prefix array where:

- `prefix[i]` stores the sum of all elements from index `0` to `i`

Then, any range sum can be computed as:

- If `left == 0` → `prefix[right]`
- Otherwise → `prefix[right] - prefix[left - 1]`

---

##  Why Use Prefix Sum?

- Converts range sum queries from **O(n) → O(1)**
- Reduces repeated computations
- Useful in both arrays and matrices (2D prefix sum)
- Frequently used in coding interviews

---

## Common Problems

- Range Sum Query
- Equilibrium Index
- Subarray Sum Equals K
- Maximum Subarray (variations)
- 2D Matrix Sum Queries

---

## Summary

Prefix Sum is a preprocessing technique that transforms an array into a cumulative sum structure, enabling fast and efficient range query computations.
