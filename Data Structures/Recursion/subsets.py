# Subsets (Backtracking)

# Problem:
# Given a list of unique integers nums,
# return all possible subsets (the power set).
#
# A subset:
# - Can include or exclude each element
# - Total subsets = 2^n
#
# -------------------------------------------------------------
# Example:
# nums = [1, 2]
#
# Output:
# [
#   [], 
#   [1], 
#   [2], 
#   [1,2]
# ]
#
# -------------------------------------------------------------
# Idea (Backtracking):
# For each element, we have 2 choices:
# - Include it
# - Exclude it
#
# Build all combinations recursively
#
# -------------------------------------------------------------
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)
# -------------------------------------------------------------


def subsets(nums):
    res = []

    def backtrack(i, path):
        # Base case: reached end
        if i == len(nums):
            res.append(path.copy())
            return

        # Choice 1: include nums[i]
        path.append(nums[i])
        backtrack(i + 1, path)

        # Choice 2: exclude nums[i]
        path.pop()
        backtrack(i + 1, path)

    backtrack(0, [])
    return res

# Main function
def main():
    nums = [1, 2, 3]

    result = subsets(nums)
    print("Subsets:")
    for subset in result:
        print(subset)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()