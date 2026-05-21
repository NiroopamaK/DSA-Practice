# House Robber Problem (Dynamic Programming)

# Problem:
# Maximize money robbed from houses
# Constraint: cannot rob adjacent houses

# -------------------------------------------------------------
# Idea:
# At each step:
# - rob current house + prev non-adjacent
# - or skip current house
#
# Keep only two variables:
# prev = dp[i-2]
# curr = dp[i-1]
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------


def rob(nums):
    prev, curr = 0, 0

    for num in nums:
        prev, curr = curr, max(curr, prev + num)

    return curr


# Main function
def main():
    nums = [2, 7, 9, 3, 1]

    print("Maximum robbed money:", rob(nums))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()