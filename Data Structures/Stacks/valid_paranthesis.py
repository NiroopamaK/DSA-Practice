# Problem: Valid Parentheses (Extended Version)

# Given a string, determine if the parentheses are valid.
# The string may contain other characters (ignore them).

# Valid pairs:
# ()  {}  []

# -------------------------------------------------------------
# Approach: Stack

# Idea:
# - Push opening brackets onto stack
# - When encountering a closing bracket:
#     - Check if it matches the top of the stack
# - If mismatch or stack empty → invalid

# Time Complexity: O(n)
# Space Complexity: O(n)

# Performance Notes:
# - Optimal solution
# - Handles mixed characters (not just brackets)


def validParenthesis(s):

    stack = []

    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:

        # If opening bracket → push
        if ch in mapping.values():
            stack.append(ch)

        # If closing bracket → validate
        elif ch in mapping:
            # Case 1: stack empty OR mismatch
            if not stack or stack[-1] != mapping[ch]:
                return False

            # Valid pair → pop
            stack.pop()

        # Ignore non-bracket characters

    # Valid if no unmatched brackets remain
    return len(stack) == 0


# -------------------------------------------------------------
# Main function

def main():

    test_cases = [
        "I (love [coding {a} lot})",   # True
        "(]",                         # False
        "([{}])",                     # True
        "(((",                        # False
        "abc",                        # True (no brackets)
    ]

    for s in test_cases:
        print(f"Input: {s}")
        print("Valid:", validParenthesis(s))
        print("-" * 30)


# -------------------------------------------------------------
# Run

if __name__ == "__main__":
    main()