# Valid Palindrome (Two Pointers)

# Problem:
# Given a string s, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
#
# -------------------------------------------------------------
# Example:
# s = "A man, a plan, a canal: Panama" → True
# s = "race a car" → False
#
# -------------------------------------------------------------
# Approach:
#
# - Use two pointers (left, right)
# - Skip non-alphanumeric characters
# - Compare lowercase characters
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------


class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
