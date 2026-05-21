# Fibonacci using Memoization (Top-Down Dynamic Programming)

# Problem:
# Compute the nth Fibonacci number
#
# Fibonacci sequence:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)
#
# -------------------------------------------------------------
# Idea:
# - Use recursion + caching (memoization)
# - Store already computed values to avoid recomputation
#
# Without memoization:
# Time Complexity = O(2^n) (exponential)
#
# With memoization:
# Time Complexity = O(n)    
# Space Complexity = O(n)
#
# -------------------------------------------------------------
# Key Concept:
# "Don't recompute subproblems"
#
# Example:
# fib(5) → fib(4) + fib(3)
# fib(4) → fib(3) + fib(2)
# fib(3) gets recomputed multiple times 
#
# Memoization stores results → avoids repetition 
# -------------------------------------------------------------


def fibMemoization(n, memo=None):
    if memo is None:
        memo = {}

    # Check cache
    if n in memo:
        return memo[n]

    # Base case
    if n <= 1:
        return n

    # Store result in memo
    memo[n] = fibMemoization(n - 1, memo) + fibMemoization(n - 2, memo)

    return memo[n]


# -------------------------------------------------------------
# Main function
# -------------------------------------------------------------
def main():
    n = 10

    print(f"Fibonacci({n}) =", fibMemoization(n))

    # Additional test cases
    print("Fibonacci(0) =", fibMemoization(0))
    print("Fibonacci(1) =", fibMemoization(1))
    print("Fibonacci(5) =", fibMemoization(5))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()