# Problem: Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring
# without repeating characters.

# -------------------------------------------------------------
# Approach 1: Sliding Window + HashSet (Your Version)

# Idea:
# Use a set to track characters in current window
# If duplicate found → shrink window from left

# Time Complexity: O(n)
# Each character is added and removed at most once

# Space Complexity: O(n)


def length_of_longest_substring_set(s):
    left, maximum = 0, 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        maximum = max(maximum, right - left + 1)

    return maximum


# -------------------------------------------------------------
# Approach 2: Sliding Window + HashMap (Optimized)

# Idea:
# Instead of removing characters one by one,
# store the last seen index of each character
#
# When duplicate is found:
# jump left pointer directly instead of moving step-by-step

# Time Complexity: O(n)
# Each character processed once

# Space Complexity: O(n)

# Performance Notes:
# - Faster in practice than set approach
# - Avoids unnecessary shrinking loops
# - Common interview "optimal" solution


def length_of_longest_substring_map(s):
    char_map = {}  # char -> last index
    left = 0
    maximum = 0

    for right in range(len(s)):
        char = s[right]

        # If character seen before AND inside current window
        if char in char_map and char_map[char] >= left:
            # Jump left pointer directly
            left = char_map[char] + 1

        # Update last seen index
        char_map[char] = right

        # Update max length
        maximum = max(maximum, right - left + 1)

    return maximum


def main():
    s = "abcabcbb"

    print("Set Approach:", length_of_longest_substring_set(s))
    print("HashMap Approach:", length_of_longest_substring_map(s))


if __name__ == "__main__":
    main()