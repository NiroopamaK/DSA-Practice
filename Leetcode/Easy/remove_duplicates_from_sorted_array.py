# Problem: Remove Duplicates from Sorted Array

# Given a sorted integer array, remove duplicates in-place
# such that each element appears only once.
#
# Return the number of unique elements (k).
# First k elements of nums should be the unique values.

# -------------------------------------------------------------
# Approach: Two Pointers (Slow & Fast)

# Idea:
# - slow pointer tracks position of last unique element
# - fast pointer scans the array
# - when a new value is found, move slow and overwrite

# Time Complexity: O(n)
# Single pass through the array

# Space Complexity: O(1)
# In-place modification

# Performance Notes:
# - Optimal solution for sorted arrays
# - Classic two-pointer pattern


class Solution(object):
    def removeDuplicates(self, nums):

        # Edge case: empty array
        if not nums:
            return 0

        slow = 0

        # Fast pointer scans entire array
        for fast in range(1, len(nums)):

            # Found a new unique element
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1