# Problem: Merge Two Sorted Linked Lists

# Given two sorted linked lists, merge them into one sorted list
# and return the head of the new list.

# -------------------------------------------------------------
# Approach: Iterative (Dummy Node)

# Idea:
# Compare nodes from list1 and list2
# Attach the smaller node to the result list
# Move pointers forward

# Time Complexity: O(n + m)
# Traverse both lists once

# Space Complexity: O(1)
# In-place merge (no extra space)

# Performance Notes:
# - Optimal solution
# - Preferred in interviews
# - Dummy node simplifies edge cases


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)
        current = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next