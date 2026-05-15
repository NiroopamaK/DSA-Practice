# Problem: Next Greater Element (Right Side)

# Given an array, for each element find the next greater element to its right.
# If no greater element exists, return -1 for that position.

# Example:
# Input:  [2, 1, 2, 4, 3]
# Output: [4, 2, 4, -1, -1]

# -------------------------------------------------------------
# Approach: Monotonic Stack (Decreasing)

# Idea:
# - Use a stack to store indices
# - Maintain decreasing order in stack
# - When a greater element is found:
#     → resolve previous smaller elements

# Time Complexity: O(n)
# Each element is pushed and popped once

# Space Complexity: O(n)


def nextGreaterElement(nums):

    stack = []              # stores indices
    res = [-1] * len(nums)  # default -1

    for i in range(len(nums)):

        # Resolve elements smaller than current
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            res[index] = nums[i]

        # Store index for future comparison
        stack.append(i)

    return res


# -------------------------------------------------------------
# Main function

def main():

    nums = [2, 1, 2, 4, 3]

    print("Input:", nums)
    print("Next Greater Elements:", nextGreaterElement(nums))


# -------------------------------------------------------------
# Run

if __name__ == "__main__":
    main()