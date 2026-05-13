# Two Pointers Technique

The **Two Pointers** technique uses two indices (pointers) to traverse an array instead of using a single pointer or nested loops.

Typically, one pointer starts at the beginning of the array and the other at the end, and both move based on a defined condition.

---

## When to Use Two Pointers?

Use this technique when:

- The array is sorted or can be sorted
- You are looking for pairs or triplets
- You need to remove duplicates
- You want to optimize from O(n²) to O(n)
- You need to shrink or expand a window efficiently

---

## Core Idea

The approach generally follows this pattern:

- Initialize two pointers:
  - `left` → starts at index 0
  - `right` → starts at the last index
- Evaluate a condition using elements at both pointers
- Move pointers based on the result:
  - Increase `left` to increase value
  - Decrease `right` to decrease value
- Stop when both pointers meet or cross each other

---

## Why Use It?

- Reduces time complexity from **O(n²) → O(n)**
- Avoids unnecessary nested loops
- Very useful in array and string problems
- Common in coding interviews

---

## Common Problems

- Two Sum (sorted array)
- Remove duplicates from sorted array
- Reverse an array
- Container With Most Water
- Pair sum problems

---

## Summary

Two pointers is a powerful optimization technique that helps solve array and string problems efficiently by reducing redundant computations and enabling linear-time solutions.
