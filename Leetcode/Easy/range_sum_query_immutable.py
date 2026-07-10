# Range Sum Query - Immutable (Prefix Sum)
# -------------------------------------------------------------

# Problem:
# Given an integer array nums, handle multiple queries of:
# sumRange(left, right) → sum of elements from index left to right (inclusive)
#
# -------------------------------------------------------------
# Idea (Prefix Sum):
# prefix[i] = sum of elements from index 0 to i
#
# Then:
# sumRange(left, right) =
#   prefix[right] - prefix[left - 1]
#
# Special case:
# if left == 0 → just prefix[right]
#
# -------------------------------------------------------------
# Time Complexity:
# - Initialization: O(n)
# - Query: O(1)
#
# Space Complexity: O(n)
# -------------------------------------------------------------


class NumArray:

    def __init__(self, nums):
        if not nums:
            self.prefix = []
            return

        self.prefix = [0] * len(nums)
        self.prefix[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left, right):
        if not self.prefix:
            return 0

        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]
