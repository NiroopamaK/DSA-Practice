# Permutations (Backtracking)

# Problem:
# Given a list of distinct integers nums,
# return all possible permutations.
#
# A permutation:
# - Uses all elements
# - Order matters
#
# -------------------------------------------------------------
# Example:
# nums = [1, 2, 3]
#
# Output:
# [
#   [1,2,3], [1,3,2],
#   [2,1,3], [2,3,1],
#   [3,1,2], [3,2,1]
# ]
#
# -------------------------------------------------------------
# Idea (Backtracking):
# - Build permutations step by step
# - Use a "used" array to track chosen elements
# - At each step:
#     pick an unused number
#     recurse
#     backtrack (undo choice)
#
# -------------------------------------------------------------
# Time Complexity: O(n * n!)
# Space Complexity: O(n)
# -------------------------------------------------------------


def permute(nums):
    res = []
    used = [False] * len(nums)

    def backtrack(path):
        # Base case: full permutation formed
        if len(path) == len(nums):
            res.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            # Choose
            used[i] = True
            path.append(nums[i])

            # Explore
            backtrack(path)

            # Un-choose (backtrack)
            path.pop()
            used[i] = False

    backtrack([])
    return res


# Main function
def main():
    nums = [1, 2, 3]

    result = permute(nums)

    print("Permutations:")
    for p in result:
        print(p)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()