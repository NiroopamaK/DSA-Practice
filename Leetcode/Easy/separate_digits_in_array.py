# Problem: Separate Digits in an Array

# Given an array of integers, return a new array consisting
# of all digits of each number in the same order.

# Example:
# Input: [100]
# Output: [1, 0, 0]

# -------------------------------------------------------------
# Approach 1: String Conversion

# Idea:
# Convert each number to string and iterate through digits

# Time Complexity: O(n * k)
# n = number of elements
# k = number of digits per number

# Space Complexity: O(n * k)
# For storing result

# Performance Notes:
# - Simple and readable
# - Uses built-in string conversion (slightly slower but fine in interviews)


def separate_digits_string(nums):
    result = []

    for n in nums:
        for digit in str(n):
            result.append(int(digit))

    return result


# -------------------------------------------------------------
# Approach 2: Mathematical (Modulo + Division)

# Idea:
# Extract digits using:
# - n % 10 → last digit
# - n // 10 → remove last digit
#
# Then reverse to maintain order

# Time Complexity: O(n * k)

# Space Complexity: O(n * k)

# Performance Notes:
# - Avoids string conversion
# - Slightly more efficient in low-level terms
# - Good when string usage is restricted


def separate_digits_math(nums):
    result = []

    for n in nums:
        digits = []

        # Edge case: if number is 0
        if n == 0:
            digits.append(0)

        while n > 0:
            digits.append(n % 10)  # extract last digit
            n //= 10               # remove last digit

        # Reverse to maintain correct order
        result.extend(digits[::-1])

    return result


def main():
    nums = [100, 23, 5]

    print("String Approach:", separate_digits_string(nums))
    print("Math Approach:", separate_digits_math(nums))


if __name__ == "__main__":
    main()