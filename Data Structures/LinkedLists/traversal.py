# Problem: Linked List Traversal

# Given the head of a singly linked list,
# traverse the list and print all elements.

# -------------------------------------------------------------
# Approach: Iterative Traversal

# Idea:
# Start from the head node
# Move through each node using the `next` pointer
# Stop when we reach None (end of list)

# Time Complexity: O(n)
# We visit each node exactly once

# Space Complexity: O(1)
# No extra space is used (only a pointer)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traversal(head):
    current = head

    # Traverse until we reach the end (None)
    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")  # Indicates end of linked list


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

    # Head of the list is node1
    traversal(node1)


if __name__ == "__main__":
    main()