# Problem: Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node
# from the end and return its head.

# -------------------------------------------------------------
# Approach: Two Pointers (Fast & Slow) + Dummy Node

# Idea:
# 1. Create a dummy node pointing to head (handles edge cases)
# 2. Move fast pointer n+1 steps ahead
# 3. Move both slow and fast until fast reaches end
# 4. Slow will be just before the node to delete

# Time Complexity: O(n)
# Single pass through the list

# Space Complexity: O(1)

# Performance Notes:
# - Optimal solution (one pass)
# - Common interview pattern (two-pointer gap technique)


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):

    # Dummy node simplifies deletion (especially head removal)
    dummy = ListNode(0, head)

    slow = dummy
    fast = dummy

    # Move fast pointer n+1 steps ahead
    # This creates a gap of n nodes between slow and fast
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Delete the nth node from end
    slow.next = slow.next.next

    return dummy.next


# Helper function to print list
def traversal(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def main():
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1,
           ListNode(2,
           ListNode(3,
           ListNode(4,
           ListNode(5)))))

    print("Original List:")
    traversal(head)

    print("After removing 2nd node from end:")
    new_head = remove_nth_from_end(head, 2)
    traversal(new_head)


if __name__ == "__main__":
    main()