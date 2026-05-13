# Problem:
# Find an index such that:
# Sum of elements to the left == Sum of elements to the right

# Approach:
# Compute total sum of the array.
# Iterate through the array while maintaining left sum.
# For each index:
# right_sum = total_sum - left_sum - current_element
# If left_sum == right_sum → equilibrium index found.

# Time Complexity: O(n)
# Space Complexity: O(1)

def equilibrium_sum(nums):
    total = sum(nums)
    left = 0

    for i in range(len(nums)):
        right = total - left - nums[i]

        if right == left:
            return i

        left += nums[i]

    return -1


def main():
    nums = [1, 3, 5, 2, 2]

    result = equilibrium_sum(nums)
    print("Equilibrium index:", result)


if __name__ == "__main__":
    main()