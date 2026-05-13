# Problem: Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes
# and return its head.

# Example:
# Input: 1 -> 2 -> 3 -> 4
# Output: 2 -> 1 -> 4 -> 3

# -------------------------------------------------------------
# Approach: Iterative Pointer Manipulation (Dummy Node)

# Idea:
# - Use a dummy node to simplify edge cases
# - Swap nodes in pairs using pointer re-linking
# - Move forward after each swap

# Time Complexity: O(n)
# Each node is visited once

# Space Complexity: O(1)
# In-place swapping (no extra memory used)

# Performance Notes:
# - Optimal iterative solution
# - Common linked list pointer manipulation pattern


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):

        # Edge case: 0 or 1 node
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Traverse in pairs
        while prev.next and prev.next.next:

            first = prev.next
            second = prev.next.next

            # -------------------------------------------------
            # Swap logic:
            # prev -> first -> second -> next
            #
            # After swap:
            # prev -> second -> first -> next
            # -------------------------------------------------

            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev two steps forward
            prev = first

        return dummy.next