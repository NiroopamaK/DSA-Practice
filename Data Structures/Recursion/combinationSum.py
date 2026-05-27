# Combination Sum (Backtracking)

# Problem:
# Given a list of DISTINCT integers (candidates) and a target integer,
# return all UNIQUE combinations where the chosen numbers sum to target.
#
# Rules:
# - You can use the same number UNLIMITED times
# - Order does NOT matter → avoid duplicate combinations
#
# -------------------------------------------------------------
# Example:
# candidates = [2, 3, 6, 7], target = 7
#
# Output:
# [
#   [2,2,3],
#   [7]
# ]
#
# -------------------------------------------------------------
# Idea (Backtracking):
# - Try each number starting from "start" index
# - Stay at same index to reuse elements
# - Stop if sum exceeds target
#
# Key Trick:
# - Use "start" to avoid duplicates
# - Reuse allowed → pass i (not i+1)
#
# -------------------------------------------------------------
# Time Complexity: Exponential (depends on combinations)
# Space Complexity: O(target)
# -------------------------------------------------------------


def combinationSum(candidates, target):
    res = []

    def backtrack(start, path, total):
        # Found valid combination
        if total == target:
            res.append(path.copy())
            return

        # Exceeded target → stop
        if total > target:
            return

        for i in range(start, len(candidates)):
            # Choose
            path.append(candidates[i])

            # Explore (reuse allowed → i)
            backtrack(i, path, total + candidates[i])

            # Backtrack
            path.pop()

    backtrack(0, [], 0)
    return res


# Main function
def main():
    candidates = [2, 3, 6, 7]
    target = 7

    result = combinationSum(candidates, target)

    print("Combinations:")
    for combo in result:
        print(combo)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()