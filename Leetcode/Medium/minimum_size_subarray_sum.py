# Minimum Size Subarray Sum (Sliding Window)
# -------------------------------------------------------------

# Problem:
# Given an array of POSITIVE integers nums and a target,
# return the minimal length of a subarray whose sum ≥ target.
#
# If no such subarray exists, return 0.
#
# -------------------------------------------------------------
# Example:
# target = 7, nums = [2,3,1,2,4,3]
#
# Output: 2
# Explanation: [4,3] is the smallest subarray with sum ≥ 7
#
# -------------------------------------------------------------
# Idea (Sliding Window):
# - Expand window by moving 'right'
# - Shrink window from 'left' while sum ≥ target
# - Track minimum window length
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------


class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            # Expand window
            current_sum += nums[right]

            # Shrink window while condition satisfied
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)

                current_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

