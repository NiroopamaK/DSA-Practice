# Product of Array Except Self (Prefix + Suffix)
# -------------------------------------------------------------

# Problem:
# Given an array nums, return an array answer such that:
# answer[i] = product of all elements except nums[i]
#
# Constraints:
# - Do NOT use division
# - Must run in O(n)
#
# -------------------------------------------------------------
# Example:
# nums = [1,2,3,4]
#
# Output:
# [24,12,8,6]
#
# -------------------------------------------------------------
# Idea:
# For each index i:
# answer[i] = (product of elements BEFORE i) *
#             (product of elements AFTER i)
#
# We compute:
# 1. Prefix products (left → right)
# 2. Suffix products (right → left)
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)
# -------------------------------------------------------------


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Step 1: prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

