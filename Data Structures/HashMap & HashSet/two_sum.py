# Problem: Two Sum

# Given an array, find two different indices such that:
# arr[i] + arr[j] == target

# Approach:
# Use a hash map (dictionary) to store values and their indices
# Iterate through the array:
# For each element, compute diff = target - current number
# If diff exists in the map → we found the pair
# Otherwise, store the current number with its index

# Time Complexity: O(n)
# Single pass through the array

# Space Complexity: O(n)
# Extra space used for the hash map


def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):
        num = arr[i]
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return None


def main():
    arr = [2, 3, 7, 1, 6, 8]
    target = 8

    result = two_sum(arr, target)
    print("Indices:", result)


if __name__ == "__main__":
    main()