# Problem: Remove Element In-Place

# Given an integer array nums and an integer val,
# remove all occurrences of val in-place.
#
# Return k = number of elements not equal to val.
# First k elements should contain valid values.
# Order does not matter.

# -------------------------------------------------------------
# Approach 1: Initial Solution (Two Pointer - While Loop)

# Idea:
# Traverse the array using an index pointer.
# Maintain a "unique" pointer to place valid elements.
#
# If nums[index] != val:
#   copy it to nums[unique]
#   move unique forward

# Time Complexity: O(n)
# Space Complexity: O(1)

# Performance Notes:
# - Simple and intuitive two-pointer approach
# - Slightly more verbose than for-loop version
# - Still optimal in time and space


def remove_element_initial(nums, val):
    unique, index = 0, 0

    while index < len(nums):
        if nums[index] != val:
            nums[unique] = nums[index]
            unique += 1
        index += 1

    return unique


# -------------------------------------------------------------
# Approach 2: Optimal Solution (For-Loop Version)

# Idea:
# Same logic as above but cleaner iteration using for-loop.
# Uses overwrite technique with a "unique" pointer.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Performance Notes:
# - 0 ms runtime (Beats 100% on LeetCode)
# - Memory usage: 12.22 MB (Beats 89.25%)
# - Cleaner and more Pythonic than while-loop version
# - Preferred in interviews due to readability


class Solution(object):
    def removeElement(self, nums, val):
        unique = 0

        for num in nums:
            if num != val:
                nums[unique] = num
                unique += 1

        return unique


def main():
    nums = [3, 2, 2, 3, 4, 5, 3, 7]
    val = 3

    # Initial solution
    arr1 = nums.copy()
    k1 = remove_element_initial(arr1, val)
    print("Initial Solution:", arr1[:k1])

    # Optimal solution
    arr2 = nums.copy()
    sol = Solution()
    k2 = sol.removeElement(arr2, val)
    print("Optimal Solution:", arr2[:k2])


if __name__ == "__main__":
    main()