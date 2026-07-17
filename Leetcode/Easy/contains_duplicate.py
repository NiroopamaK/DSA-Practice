# Contains Duplicate

# Problem:
# Given an integer array nums, return True if any value appears
# at least twice in the array, and return False if every element
# is distinct.
#
# -------------------------------------------------------------
# Example:
# nums = [1,2,3,1] → True
# nums = [1,2,3,4] → False
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------


# Solution 1: Hash Map (Frequency Count)
class SolutionHashMap:
    def containsDuplicate(self, nums):
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        return any(count >= 2 for count in seen.values())


# Solution 2: Set (Optimal - Early Exit)
class SolutionSet:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


# Solution 3: Pythonic One-Liner
class SolutionOneLiner:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
