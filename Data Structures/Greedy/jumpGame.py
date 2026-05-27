# Jump Game (Greedy)
# -------------------------------------------------------------

# Problem:
# You are given an array nums where each element represents
# the maximum jump length from that position.
#
# Goal:
# Determine if you can reach the last index starting from index 0.
#
# -------------------------------------------------------------
# Example:
# nums = [2, 3, 1, 1, 4]
# You can jump:
# index 0 → index 1 → index 4 → True
#
# nums = [3, 2, 1, 0, 4]
# You get stuck at index 3 → False
#
# -------------------------------------------------------------
# Idea (Greedy):
# - Track the farthest index we can reach (max_reach)
# - Iterate through the array:
#     - If current index > max_reach → we are stuck → return False
#     - Otherwise, update max_reach = max(max_reach, i + nums[i])
# - If at any point max_reach reaches or exceeds last index → return True
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------


def canJump(nums):
    max_reach = 0
    n = len(nums)

    for i in range(n):
        # If current index is beyond what we can reach → stuck
        if i > max_reach:
            return False

        # Update the farthest we can reach
        max_reach = max(max_reach, i + nums[i])

        # If we can reach or pass last index → success
        if max_reach >= n - 1:
            return True

    return True


# Main function
def main():
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]

    print("Can jump (nums1):", canJump(nums1))  # Expected: True
    print("Can jump (nums2):", canJump(nums2))  # Expected: False


# -------------------------------------------------------------
if __name__ == "__main__":
    main()