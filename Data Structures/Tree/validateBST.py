# Problem: Validate Binary Search Tree (BST)

# A valid BST must satisfy:
# - Left subtree values < node value
# - Right subtree values > node value
# - This must hold for ALL nodes (global property)

# -------------------------------------------------------------
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -------------------------------------------------------------
# Recursive DFS with range validation
def validateBST(root):

    def helper(node, low, high):
        # Base case: empty node is valid
        if not node:
            return True

        # Check if current node violates BST property
        if not (low < node.val < high):
            return False

        # Recursively validate left and right subtrees
        return (
            helper(node.left, low, node.val) and   # left < node.val
            helper(node.right, node.val, high)     # right > node.val
        )

    # Initial range is (-inf, +inf)
    return helper(root, float('-inf'), float('inf'))


# -------------------------------------------------------------
# Main function (example usage)
def main():
    # Valid BST example:
    #
    #         5
    #       /   \
    #      3     7
    #     / \   / \
    #    2   4 6   8

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    print("Is valid BST?", validateBST(root))  # True

    root.right.left = TreeNode(2)

    print("Is valid BST?", validateBST(root))  # False


# -------------------------------------------------------------
if __name__ == "__main__":
    main()


# -------------------------------------------------------------
# Complexity Analysis:
#
# Time Complexity: O(n)
# - Each node is visited exactly once
#
# Space Complexity: O(h)
# - h = height of tree (recursive stack)
# - Worst case: O(n), Best case: O(log n)
#
# -------------------------------------------------------------
# Key Insight:
# Use value ranges (low, high) to enforce GLOBAL BST rules
# not just parent-child comparisons
#
# -------------------------------------------------------------
# Common Mistake:
# Only checking:
# node.left < node < node.right
# This fails for deeper violations