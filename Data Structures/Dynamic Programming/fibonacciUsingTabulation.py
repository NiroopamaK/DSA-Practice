# Fibonacci using Tabulation (Bottom-Up Dynamic Programming)

# Problem:
# Compute the nth Fibonacci number
#
# Fibonacci:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)
#
# -------------------------------------------------------------
# Idea:
# - Build solution iteratively from smallest subproblems
# - Use an array (dp) to store results
#
# dp[i] = dp[i-1] + dp[i-2]
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------


def fibTabulation(n):
    # Edge cases
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Space Optimized Version (BEST)
# -------------------------------------------------------------
# Instead of storing full array, keep only last two values
# Space Complexity → O(1)

def fibOptimized(n):
    if n <= 1:
        return n

    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


# Main function
def main():
    n = 10

    print("Tabulation:", fibTabulation(n))
    print("Optimized:", fibOptimized(n))

    # Edge cases
    print("n = 0:", fibTabulation(0))
    print("n = 1:", fibTabulation(1))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()