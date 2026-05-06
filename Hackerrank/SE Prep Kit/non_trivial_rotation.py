# Problem: Non-Trivial String Rotation

# Given two strings s1 and s2, return 1 if s2 is a rotation of s1
# but NOT identical to s1, otherwise return 0.

# Approach 1: Brute Force Rotation
# Generate all possible rotations of s2 and compare with s1
#
# For each index:
# Rotate string using slicing and check equality

# Time Complexity: O(n^2)
# n rotations × O(n) comparison

# Space Complexity: O(n)
# Temporary rotated string


def is_non_trivial_rotation(s1, s2):
    if len(s1) != len(s2) or s1 == s2:
        return 0

    for i in range(1, len(s2)):
        rotated = s2[i:] + s2[:i]
        if rotated == s1:
            return 1

    return 0


# -------------------------------------------------------------

# Approach 2: Optimized (String Trick)
# Key idea:
# If s1 is a rotation of s2, then s1 will be a substring of (s2 + s2)
#
# Example:
# s2 = "cdeab"
# s2 + s2 = "cdeabcdeab"
# Contains "abcde"

# Time Complexity: O(n)
# String search

# Space Complexity: O(n)
# Concatenated string


def is_non_trivial_rotation_optimal(s1, s2):
    if len(s1) != len(s2) or s1 == s2:
        return 0

    return 1 if s1 in (s2 + s2) else 0


def main():
    s1 = "abcde"
    s2 = "cdeab"

    print("Brute Force:", is_non_trivial_rotation(s1, s2))
    print("Optimal:", is_non_trivial_rotation_optimal(s1, s2))


if __name__ == "__main__":
    main()