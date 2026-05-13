# Problem: Longest substring without repeating characters

# Approach:
# Use Sliding Window with a set to track characters in the current window.
# Expand the right pointer and add characters to the set.
# If a duplicate is found, shrink the window from the left until valid again.
#
# Keep track of the maximum window size during the process.

# Time Complexity: O(n)
# Space Complexity: O(k) where k is size of character set

def longest_substring(s):
    left = 0
    max_len = 0
    charset = set()

    for right in range(len(s)):
        while s[right] in charset:
            charset.remove(s[left])
            left += 1

        charset.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    s = "abcdcb"

    result = longest_substring(s)
    print("Longest substring length:", result)


if __name__ == "__main__":
    main()