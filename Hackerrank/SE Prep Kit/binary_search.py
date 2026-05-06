# Problem: Binary Search

# Given a sorted array of distinct integers and a target value,
# return the index of the target if found, otherwise return -1.

# Approach: Binary Search
# Use two pointers (left and right) to repeatedly divide the search space in half
#
# Steps:
# 1. Find the middle element
# 2. If it matches target → return index
# 3. If target is smaller → search left half
# 4. If target is larger → search right half

# Time Complexity: O(log n)
# Each step halves the search space

# Space Complexity: O(1)
# No extra space used (iterative approach)


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def main():
    nums = [2, 4, 6, 8, 10]
    target = 6

    result = binary_search(nums, target)
    print("Index:", result)


if __name__ == "__main__":
    main()