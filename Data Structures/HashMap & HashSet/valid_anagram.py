# Problem: Valid Anagram

# Given two strings s and t, determine if t is an anagram of s.
# An anagram means both strings contain the same characters
# with the same frequency.

# Approach 1: Frequency Map (Hash Map)
# Count characters in string s
# Decrease counts using string t
# If all counts return to zero → valid anagram

# Time Complexity: O(n)
# We iterate through both strings once

# Space Complexity: O(1)
# At most 26 characters (assuming lowercase English letters)


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    seen = {}

    for ch in s:
        seen[ch] = seen.get(ch, 0) + 1

    for ch in t:
        if ch not in seen:
            return False
        seen[ch] -= 1

    return all(v == 0 for v in seen.values())


# Approach 2: Using Counter (Built-in)

# Time Complexity: O(n)
# Space Complexity: O(1) (bounded character set)


from collections import Counter

def is_anagram_easy(s, t):
    return Counter(s) == Counter(t)


def main():
    s = "abcdef"
    t = "abcde"

    print("Hash Map Approach:", is_anagram(s, t))
    print("Counter Approach:", is_anagram_easy(s, t))


if __name__ == "__main__":
    main()