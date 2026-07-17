# Linked List Cycle Detection

# Problem:
# Given the head of a linked list, determine if the list
# contains a cycle.
#
# -------------------------------------------------------------
# Example:
# 3 → 2 → 0 → -4
#     ↑       ↓
#     ← ← ← ←
#
# Output: True
#
# -------------------------------------------------------------
# Approaches:
# 1. Floyd’s Cycle Detection (Tortoise & Hare)
# 2. Hash Set (Visited Nodes)
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity:
#   - Floyd’s: O(1)
#   - Set:     O(n)
# -------------------------------------------------------------


# -------------------------------------------------------------
# Definition for singly-linked list
# -------------------------------------------------------------
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1: Floyd’s Cycle Detection (Optimal)
class SolutionFloyd:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                return True

        return False


# Solution 2: Hash Set (Visited Nodes)
class SolutionSet:
    def hasCycle(self, head):
        seen = set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False

