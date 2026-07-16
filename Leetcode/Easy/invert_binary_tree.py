# Invert Binary Tree (Recursive DFS)

# Problem:
# Given the root of a binary tree, invert the tree
# (swap every left and right child).
#
# -------------------------------------------------------------
# Example:
#
# Input:        Output:
#    4             4
#   / \           / \
#  2   7   →     7   2
# / \ / \       / \ / \
#1  3 6  9     9  6 3  1
#
# -------------------------------------------------------------
# Approach:
#
# - Swap left and right children
# - Recursively invert subtrees
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(h)  (recursion stack)
# -------------------------------------------------------------


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Recurse on subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root