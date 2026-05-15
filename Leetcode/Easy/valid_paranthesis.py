# Problem: Valid Parentheses

# Given a string s containing just the characters:
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# A string is valid if:
# 1. Open brackets are closed by the same type
# 2. Open brackets are closed in the correct order

# -------------------------------------------------------------
# Approach: Stack

# Idea:
# - Push opening brackets onto stack
# - For closing brackets:
#     → Check if it matches top of stack
# - If mismatch or stack empty → invalid

# Time Complexity: O(n)
# Space Complexity: O(n)

# Performance Notes:
# - Optimal solution
# - Standard stack pattern


class Solution(object):
    def isValid(self, s):

        stack = []

        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            # If opening bracket → push
            if ch in mapping.values():
                stack.append(ch)

            # If closing bracket → validate
            elif ch in mapping:

                # Case 1: stack empty OR mismatch
                if not stack or stack[-1] != mapping[ch]:
                    return False

                # Valid pair → pop
                stack.pop()

        # Valid if no unmatched brackets remain
        return len(stack) == 0