# Problem: Longest subarray without repeating characters

# Approach: Variable Sliding Window
# Use a set to track current window elements
# Expand right pointer, and shrink left pointer when duplicates are found
# Maintain maximum window size

# Time Complexity: O(n)
# Space Complexity: O(n)

def max_sub_without_duplicates(arr):
    left = 0
    seen = set()
    maximum = 0
    best_subarray = []

    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])
        if right - left + 1 > maximum:
            maximum = right - left + 1
            best_subarray = arr[left:right + 1]

    return maximum, best_subarray


def main():
    arr = ['a', 'b', 'c', 'd', 'b', 'f', 'g']

    result = max_sub_without_duplicates(arr)
    print("Maximum length and sub array without duplicates:", result)


if __name__ == "__main__":
    main()