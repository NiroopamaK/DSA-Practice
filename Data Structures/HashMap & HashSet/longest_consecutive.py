# Problem: Longest Consecutive Sequence

# Given an unsorted array of integers, find the length
# of the longest consecutive elements sequence.

# Approach: Hash Set
# Convert array into a set for O(1) lookups
#
# For each number:
# Only start counting if it's the beginning of a sequence
# (i.e., num - 1 is not in the set)
#
# Then expand forward (num + 1, num + 2, ...) to count length

# Time Complexity: O(n)
# Each number is processed at most once

# Space Complexity: O(n)
# Set stores all elements


def longest_consecutive(arr):
    nums = set(arr)
    longest = 0

    for num in nums:
        # Check if it's the start of a sequence
        if num - 1 not in nums:
            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


def main():
    arr = [100, 2, 1, 4, 3, 500, 5]

    result = longest_consecutive(arr)
    print("Longest consecutive length:", result)


if __name__ == "__main__":
    main()