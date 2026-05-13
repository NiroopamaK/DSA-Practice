# Problem: Reverse a Linked List

# Given the head of a singly linked list,
# reverse the list and return the new head.

# -------------------------------------------------------------
# Approach: Iterative Pointer Reversal

# Idea:
# We reverse the direction of each node's `next` pointer
#
# previous <- current <- next
#
# At each step:
# 1. Store next node
# 2. Reverse the link
# 3. Move pointers forward

# Time Complexity: O(n)
# We traverse the list once

# Space Complexity: O(1)
# In-place reversal (no extra space used)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    current = head
    previous = None

    # Traverse the list
    while current:
        nxt = current.next       # Step 1: store next node
        current.next = previous  # Step 2: reverse pointer
        previous = current       # Step 3: move previous forward
        current = nxt            # Step 4: move current forward

    # previous becomes the new head
    return previous


# Helper function to print list
def traversal(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def main():
    # Creating nodes
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(15)
    node4 = Node(20)
    node5 = Node(25)

    # Linking nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Original List:")
    traversal(node1)

    # Reverse the list
    new_head = reverse_list(node1)

    print("Reversed List:")
    traversal(new_head)


if __name__ == "__main__":
    main()