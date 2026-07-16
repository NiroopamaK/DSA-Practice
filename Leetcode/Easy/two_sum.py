# Two Sum (Hash Map)


# Problem:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input has exactly one solution,
# and you may not use the same element twice.
#
# -------------------------------------------------------------
# Example:
# nums = [2,7,11,15], target = 9
#
# Output: [0,1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9
#
# -------------------------------------------------------------
# Approach:
#
# - Use a hash map (dictionary) to store:
#     value → index
#
# - For each number:
#     remainder = target - current number
#
# - If remainder exists in map → we found the answer
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------


class Solution:
    def twoSum(self, nums, target):
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            remainder = target - num

            # Check if complement exists
            if remainder in seen:
                return [seen[remainder], i]

            # Store current number
            seen[num] = i

        return []  

