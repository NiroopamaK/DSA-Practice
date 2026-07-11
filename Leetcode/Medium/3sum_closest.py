# 3Sum Closest (Two Pointers + Sorting)
# -------------------------------------------------------------

# Problem:
# Given an integer array nums and an integer target,
# return the sum of three integers in nums such that
# the sum is closest to target.
#
# You may assume that each input has exactly one solution.
#
# -------------------------------------------------------------
# Example:
# nums = [-1, 2, 1, -4], target = 1
#
# Output: 2
# Explanation: (-1 + 2 + 1 = 2), which is closest to target
#
# -------------------------------------------------------------
# Approach:
#
# 1. Sort the array
# 2. Fix one number nums[i]
# 3. Use two pointers:
#       left = i + 1
#       right = end
#
# 4. Compute sum and compare with target:
#       Update closest if needed
#
# 5. Move pointers:
#       sum < target → move left
#       sum > target → move right
#       sum == target → return immediately
#
# -------------------------------------------------------------
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# -------------------------------------------------------------


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        # Initialize with first possible triplet
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # Move pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # exact match

        return closest
