# Problem: Detect Cycle in a Linked List

# Given the head of a linked list,
# determine if the list contains a cycle.

# -------------------------------------------------------------
# Approach: Floyd’s Cycle Detection (Tortoise & Hare)

# Idea:
# Use two pointers:
# - slow → moves 1 step at a time
# - fast → moves 2 steps at a time
#
# If there is a cycle:
# fast will eventually meet slow
#
# If there is no cycle:
# fast will reach the end (None)

# Time Complexity: O(n)
# Each pointer traverses at most n nodes

# Space Complexity: O(1)
# No extra space used (constant pointers only)

# Why this works:
# Fast pointer "laps" the slow pointer in a cycle


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    # Traverse the list
    while fast and fast.next:
        slow = slow.next          # move 1 step
        fast = fast.next.next     # move 2 steps

        # If they meet → cycle exists
        if slow == fast:
            return True

    # If fast reaches None → no cycle
    return False


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

    # Create cycle: node5 → node2
    node5.next = node2

    print("Cycle detected:", has_cycle(node1))


if __name__ == "__main__":
    main()