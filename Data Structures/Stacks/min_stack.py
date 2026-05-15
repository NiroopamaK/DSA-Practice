# Problem: Min Stack

# Design a stack that supports:
# - push(val)
# - pop()
# - top()
# - getMin()
# All operations must run in O(1) time.

# -------------------------------------------------------------
# Approach: Two Stacks

# Idea:
# - stack → stores all values
# - min_stack → stores the minimum values
# - min_stack keeps track of the "history" of minimums

# Time Complexity:
# push   -> O(1)
# pop    -> O(1)
# top    -> O(1)
# getMin -> O(1)

# Space Complexity: O(n)
# Extra space used for min_stack


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        # Push to min_stack if:
        # - it's empty OR
        # - new value is smaller or equal
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            print("Stack is empty. Cannot pop.")
            return

        # If popped value is current minimum, pop from min_stack too
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self):
        if not self.stack:
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            print("Stack is empty.")
            return None
        return self.min_stack[-1]


# -------------------------------------------------------------
# Helper function to print stack (for debugging/demo)

def print_stack(stack):
    print("Stack:", stack.stack)
    print("MinStack:", stack.min_stack)
    print("-" * 30)


# -------------------------------------------------------------
# Main function (entry point)

def main():
    stack = MinStack()

    print("Pushing elements...")
    stack.push(10)
    stack.push(20)
    stack.push(6)
    stack.push(15)

    print_stack(stack)

    print("Current Min:", stack.get_min())  # 6

    print("\nPopping...")
    stack.pop()
    print_stack(stack)

    print("Current Min:", stack.get_min())  # 6

    print("\nPopping...")
    stack.pop()
    print_stack(stack)

    print("Current Min:", stack.get_min())  # 10

    print("\nTop element:", stack.top())


# -------------------------------------------------------------
# Run program

if __name__ == "__main__":
    main()