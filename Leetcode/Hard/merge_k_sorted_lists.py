# Problem: Merge K Sorted Linked Lists

# Given an array of k sorted linked lists,
# merge them into one sorted linked list and return its head.

# -------------------------------------------------------------
# Approach 1: Brute Force (Min Selection)

# Idea:
# - Maintain a list of current nodes (one from each list)
# - Repeatedly pick the smallest node
# - Add its next node back into the list

# Time Complexity: O(N * K)
# N = total number of nodes
# K = number of lists
# Each selection takes O(K) using min()

# Space Complexity: O(K)

# Performance Notes:
# - Simple and intuitive
# - Not efficient for large K


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists_bruteforce(lists):

    dummy = ListNode(0)
    tail = dummy

    current = []

    # Initialize with head nodes
    for node in lists:
        if node:
            current.append(node)

    while current:

        # Find minimum node
        minimum_node = min(current, key=lambda x: x.val)

        # Attach to result
        tail.next = minimum_node
        tail = tail.next

        # Add next node if exists
        if minimum_node.next:
            current.append(minimum_node.next)

        # Remove processed node
        current.remove(minimum_node)

    return dummy.next


# -------------------------------------------------------------
# Approach 2: Optimal (Min Heap / Priority Queue)

# Idea:
# - Use a heap to always get the smallest node efficiently
# - Push first node of each list into heap
# - Pop smallest, attach it, then push its next node

# Time Complexity: O(N log K)
# Heap operations take O(log K)

# Space Complexity: O(K)

# Performance Notes:
# - Optimal solution
# - Standard interview expectation
# - Efficient for large number of lists


import heapq


def merge_k_lists_heap(lists):

    heap = []

    # Push initial nodes into heap
    for i, node in enumerate(lists):
        if node:
            # (value, index, node)
            # index prevents comparison issues when values are equal
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    tail = dummy

    while heap:

        val, i, node = heapq.heappop(heap)

        # Attach smallest node
        tail.next = node
        tail = tail.next

        # Push next node into heap
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# -------------------------------------------------------------
# Helper function

def traversal(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def main():
    # Example:
    # List1: 1 -> 4 -> 5
    # List2: 1 -> 3 -> 4
    # List3: 2 -> 6

    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))

    lists = [l1, l2, l3]

    print("Brute Force:")
    merged1 = merge_k_lists_bruteforce(lists)
    traversal(merged1)

    # Recreate lists (since they were modified)
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))

    lists = [l1, l2, l3]

    print("Optimal (Heap):")
    merged2 = merge_k_lists_heap(lists)
    traversal(merged2)


if __name__ == "__main__":
    main()