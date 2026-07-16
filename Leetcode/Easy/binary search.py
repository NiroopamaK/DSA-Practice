# Binary Search (Iterative)

# Problem:
# Given a sorted array nums and a target value,
# return the index if the target is found.
# Otherwise, return -1.
#
# -------------------------------------------------------------
# Example:
# nums = [-1,0,3,5,9,12], target = 9 → 4
# nums = [-1,0,3,5,9,12], target = 2 → -1
#
# -------------------------------------------------------------
# Approach:
#
# - Use two pointers (left, right)
# - Find middle element
# - Eliminate half of the search space each time
#
# -------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# -------------------------------------------------------------


class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1