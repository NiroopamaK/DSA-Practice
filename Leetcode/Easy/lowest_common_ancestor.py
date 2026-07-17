# Lowest Common Ancestor of a Binary Tree (DFS)

# Problem:
# Given a binary tree, find the lowest common ancestor (LCA)
# of two given nodes p and q.
#
# The LCA is defined as the lowest node that has both
# p and q as descendants (a node can be a descendant of itself).
#
# -------------------------------------------------------------
# Example:
#
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
#
# LCA(5, 1) = 3
# LCA(5, 4) = 5
#
# -------------------------------------------------------------
# Approach:
#
# - Use DFS recursion
# - If current node is p or q → return it
# - Recurse left and right
# - If both sides return non-null → current node is LCA
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(h)
# -------------------------------------------------------------


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Base case
        if not root or root == p or root == q:
            return root

        # Search left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides found → this is LCA
        if left and right:
            return root

        # Otherwise return the non-null side
        return left if left else right