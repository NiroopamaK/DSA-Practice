# Problem: Count frequency of each character in a string

# Approach:
# Use a hash map (dictionary) to store frequency of each character.
# Traverse the string and update counts.

# Time Complexity: O(n)
# Space Complexity: O(k) where k is number of unique characters

def frequency_check(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    return freq


def main():
    s = "abbbcdde"

    result = frequency_check(s)
    print("Character frequencies:", result)


if __name__ == "__main__":
    main()