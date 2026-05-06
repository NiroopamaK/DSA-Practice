# Problem: First Occurrence of a Target in a Sorted Array

# Given a sorted array of integers (which may contain duplicates),
# return the index of the first occurrence of the target value.
# If the target is not found, return -1.

# Approach: Modified Binary Search
# Standard binary search is modified to continue searching left
# even after finding the target.

# Steps:
# 1. Perform binary search
# 2. If nums[mid] == target:
#    - store index in result
#    - move search to left half (high = mid - 1)
# 3. If nums[mid] < target → move right
# 4. If nums[mid] > target → move left

# Time Complexity: O(log n)
# Each step halves the search space

# Space Complexity: O(1)
# No extra space used


def find_first_occurrence(nums, target):
    if len(nums) == 0:
        return -1

    low, high = 0, len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            result = mid
            high = mid - 1  # continue searching left side
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return result


def main():
    nums = [2, 2, 2, 2]
    target = 2

    result = find_first_occurrence(nums, target)
    print("First occurrence index:", result)


if __name__ == "__main__":
    main()