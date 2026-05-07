# Problem: Divide Two Integers

# Given two integers dividend and divisor,
# divide them without using multiplication, division, or mod operator.
#
# Return the quotient after dividing dividend by divisor.

# -------------------------------------------------------------
# Approach 1: Brute Force (Repeated Subtraction)

# Idea:
# Keep subtracting divisor from dividend until remainder < divisor
# Count how many times subtraction happens

# Time Complexity: O(n)
# In worst case, we subtract divisor from dividend repeatedly

# Space Complexity: O(1)
# No extra space used


def divide(dividend, divisor):
    flag = 1

    # Determine sign using XOR:
    # If one is negative and the other is positive → result is negative
    if (dividend < 0) ^ (divisor < 0):
        flag = -1

    # Convert both numbers to positive
    if dividend < 0:
        dividend *= -1

    if divisor < 0:
        divisor *= -1

    rem = dividend
    count = 0

    # Outer loop: subtract divisor repeatedly
    while rem >= divisor:
        rem -= divisor
        count += 1

    return count * flag


# -------------------------------------------------------------
# Approach 2: Optimized (Bit Manipulation / Exponential Search)

# Idea:
# Instead of subtracting divisor one-by-one,
# double the divisor using bit shifting (<<)
#
# This reduces the number of operations significantly

# Time Complexity: O(log n)
# Outer loop runs log n times, inner loop also log n

# Space Complexity: O(1)

# Key Concepts:
# - Left shift (<<) → multiply by 2
# - Right shift (>>) → divide by 2 (not used here)


def divide_optimized(dividend, divisor):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Edge Case:
    # Overflow occurs when dividing INT_MIN by -1
    # Result exceeds 32-bit integer range
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    # Determine sign:
    # True if signs are different → result negative
    sign = (dividend < 0) != (divisor < 0)

    # Work with positive numbers
    dividend = abs(dividend)
    divisor = abs(divisor)

    result = 0

    # Outer Loop:
    # Continue until dividend becomes smaller than divisor
    while dividend >= divisor:

        temp = divisor
        multiple = 1

        # Inner Loop:
        # Keep doubling temp (divisor) using bit shift
        # until it exceeds dividend
        #
        # temp <<= 1  → temp = temp * 2
        # multiple <<= 1 → tracks how many times divisor is doubled
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1

        # Subtract the largest doubled divisor
        dividend -= temp

        # Add corresponding multiple to result
        result += multiple

    # Apply sign
    return -result if sign else result


def main():
    dividend = 7
    divisor = -3

    print("Brute Force:", divide(dividend, divisor))
    print("Optimized:", divide_optimized(dividend, divisor))


if __name__ == "__main__":
    main()