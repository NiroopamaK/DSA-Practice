# Problem: Check if a string is a palindrome

# Approach:
# Use two pointers:
# left starts at beginning, right starts at end
# Compare characters at both pointers
# If mismatch → not a palindrome
# Move pointers inward until they meet

# Time Complexity: O(n)
# Space Complexity: O(1)

def check_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def main():
    s = "abcddcba"

    result = check_palindrome(s)
    print("Is palindrome:", result)


if __name__ == "__main__":
    main()