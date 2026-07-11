# Maximum Subarray (Kadane's Algorithm)

# Problem:
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum,
# and return its sum.
#
# -------------------------------------------------------------
# Example:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
#
# Output: 6
# Explanation: [4,-1,2,1] → sum = 6
#
# -------------------------------------------------------------
# Idea (Kadane’s Algorithm):
# - At each index, decide:
#     start a new subarray OR extend the current one
#
# current_sum = max(nums[i], current_sum + nums[i])
#
# Track the maximum seen so far
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------


class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # Decide: start new or extend
            current_sum = max(nums[i], current_sum + nums[i])

            # Update global max
            max_sum = max(max_sum, current_sum)

        return max_sum

