# Problem: Remove Nth Node From End of Linked List

# Given the head of a linked list, remove the nth node from the end
# and return the head of the modified list.

# -------------------------------------------------------------
# Approach: Two Pointers (Fast & Slow) + Dummy Node

# Idea:
# 1. Use two pointers (fast & slow)
# 2. Move fast pointer n+1 steps ahead
# 3. Move both pointers together until fast reaches end
# 4. Slow will be just before the node to delete

# Time Complexity: O(n)
# Single pass through the list

# Space Complexity: O(1)
# No extra space used

# Why Dummy Node?
# Handles edge case where head needs to be deleted


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

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


# Helper function
def traversal(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def main():
    # Creating linked list: 5 -> 10 -> 15 -> 20 -> 25
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

    print("After deleting 2nd node from end:")
    new_head = delete_nth_from_end(node1, 2)
    traversal(new_head)


if __name__ == "__main__":
    main()