# Longest Increasing Subsequence (LIS) - Dynamic Programming

# Problem:
# Find the length of the longest strictly increasing subsequence.
#
# A subsequence is not necessarily contiguous.
#
# -------------------------------------------------------------
# Idea:
# dp[i] = length of LIS ending at index i
#
# Transition:
# For each i, check all j < i:
# if nums[j] < nums[i]:
#     dp[i] = max(dp[i], dp[j] + 1)
#
# -------------------------------------------------------------
# Base Case:
# Every element is a subsequence of length 1
#
# -------------------------------------------------------------
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# -------------------------------------------------------------


def lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Main function
def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    print("Length of LIS:", lis(nums))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()