# Problem: Daily Temperatures

# Given a list of daily temperatures,
# return a list such that for each day tells you
# how many days you would have to wait until a warmer temperature.
#
# If there is no future day, put 0.

# Example:
# Input:  [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# -------------------------------------------------------------
# Approach: Monotonic Stack (Decreasing Stack)

# Idea:
# - Use a stack to store indices of temperatures
# - Maintain decreasing order in stack
# - When current temperature is higher:
#     → resolve previous colder days

# Time Complexity: O(n)
# Each index is pushed and popped at most once

# Space Complexity: O(n)
# Stack + result array


def dailyTemperatures(T):

    stack = []  # stores indices
    res = [0] * len(T)

    for i in range(len(T)):

        # If current temperature is higher than stack top
        while stack and T[i] > T[stack[-1]]:

            index = stack.pop()
            res[index] = i - index  # days waited

        # Push current index
        stack.append(i)

    return res


# -------------------------------------------------------------
# Main function

def main():

    T = [73, 74, 75, 71, 69, 72, 76, 73]

    print("Temperatures:", T)
    print("Days to wait:", dailyTemperatures(T))


# -------------------------------------------------------------
# Run

if __name__ == "__main__":
    main()