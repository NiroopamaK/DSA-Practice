# -------------------------------------------------------------
# Valid Anagram (Hash Map)
# -------------------------------------------------------------

# Problem:
# Given two strings s and t, return True if t is an anagram of s,
# otherwise return False.
#
# -------------------------------------------------------------
# Example:
# s = "anagram", t = "nagaram" → True
# s = "rat", t = "car"         → False
#
# -------------------------------------------------------------
# Approach:
#
# - Count frequency of characters in s
# - Subtract using t
# - Ensure all counts return to zero
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(k)  (unique characters)
# -------------------------------------------------------------


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Subtract using t
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        # Ensure all counts are zero
        return all(v == 0 for v in count.values())