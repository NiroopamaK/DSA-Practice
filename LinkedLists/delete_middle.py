# Problem: Delete the Middle Node of a Linked List

# Given the head of a linked list,
# delete the middle node and return the modified list.

# -------------------------------------------------------------
# Approach 1: Two Pass (Count + Traverse)

# Idea:
# 1. Count total nodes
# 2. Find middle index (n // 2)
# 3. Traverse again to node before middle
# 4. Delete it

# Time Complexity: O(n)
# First pass → O(n), Second pass → O(n)

# Space Complexity: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_mid(head):

    # Edge case: single node → result is empty list
    if head is None or head.next is None:
        return None

    # First pass: count nodes
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next

    # Find middle index
    middle = count // 2

    # Second pass: reach node before middle
    current = head
    for _ in range(middle - 1):
        current = current.next

    # Delete middle node
    current.next = current.next.next

    return head


# -------------------------------------------------------------
# Approach 2: Optimal (Slow & Fast Pointer)

# Idea:
# Use two pointers:
# - slow moves 1 step
# - fast moves 2 steps
#
# When fast reaches end, slow is at middle
# Track previous node to delete middle

# Time Complexity: O(n)
# Single traversal

# Space Complexity: O(1)

# Performance Notes:
# - More efficient than two-pass approach
# - Preferred in interviews


def delete_mid_optimized(head):

    # Edge case
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    # Traverse list
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # slow is at middle → remove it
    prev.next = slow.next

    return head


# Helper function
def traversal(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def main():
    # Create list: 5 -> 10 -> 15 -> 20 -> 25
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(15)
    node4 = Node(20)
    node5 = Node(25)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Original List:")
    traversal(node1)

    print("After deleting middle (two-pass):")
    head1 = delete_mid(node1)
    traversal(head1)

    # Recreate list for second approach
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(15)
    node4 = Node(20)
    node5 = Node(25)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("After deleting middle (optimized):")
    head2 = delete_mid_optimized(node1)
    traversal(head2)


if __name__ == "__main__":
    main()