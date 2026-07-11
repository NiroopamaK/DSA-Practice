# 3Sum Problem (Two Pointers + Sorting)
# -------------------------------------------------------------

# Problem:
# Given an integer array nums, return all the unique triplets
# [nums[i], nums[j], nums[k]] such that:
#
#     i != j, i != k, j != k
#     nums[i] + nums[j] + nums[k] == 0
#
# The solution set must NOT contain duplicate triplets.
#
# -------------------------------------------------------------
# Example:
# nums = [-1,0,1,2,-1,-4]
#
# Output:
# [[-1,-1,2], [-1,0,1]]
#
# -------------------------------------------------------------
# Approach:
#
# 1. Sort the array
# 2. Fix one number nums[i]
# 3. Use two pointers:
#       left = i + 1
#       right = end of array
#
# 4. Move pointers based on sum:
#       sum < 0 → move left forward
#       sum > 0 → move right backward
#       sum == 0 → record result
#
# 5. Skip duplicates to ensure unique triplets
#
# -------------------------------------------------------------
# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding output)
# -------------------------------------------------------------


class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):

            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
