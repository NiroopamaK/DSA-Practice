# Balanced Binary Tree (Optimized DFS)

# Problem:
# Given a binary tree, determine if it is height-balanced.
#
# A binary tree is balanced if:
# The depth of the two subtrees of every node never differs by more than 1.
#
# -------------------------------------------------------------
# Approach:
#
# - Use DFS to compute height
# - Return -1 immediately if subtree is unbalanced
# - Avoid recomputing heights (O(n))
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(h)
# -------------------------------------------------------------


class Solution:
    def isBalanced(self, root):

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1  # left subtree already unbalanced

            right = height(node.right)
            if right == -1:
                return -1  # right subtree already unbalanced

            # Check balance condition
            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1