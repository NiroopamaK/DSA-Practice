# Problem: Check if two strings are anagrams

# Two strings are anagrams if they contain the same characters
# with the same frequency.

# Approach 1: Sorting
# Sort both strings and compare them
# Time Complexity: O(n log n)

# Approach 2: Hash Map (Frequency Counting)
# Count characters in one string and reduce using the other
# Time Complexity: O(n)

# Approach 3: Fixed Array (Optimized for lowercase a-z)
# Use a fixed size array instead of a dictionary
# Time Complexity: O(n)
# Space Complexity: O(1)


def is_anagram1(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


def is_anagram2(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1

    return all(value == 0 for value in freq.values())


def is_anagram3(s1, s2):
    if len(s1) != len(s2):
        return False

    count = [0] * 26

    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1
        count[ord(s2[i]) - ord('a')] -= 1

    return all(c == 0 for c in count)


def main():
    s1 = "apple"
    s2 = "apple"

    print("Sorting approach:", is_anagram1(s1, s2))
    print("HashMap approach:", is_anagram2(s1, s2))
    print("Optimized array approach:", is_anagram3(s1, s2))


if __name__ == "__main__":
    main()