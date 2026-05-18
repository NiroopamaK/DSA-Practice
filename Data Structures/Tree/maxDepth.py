# Problem: Maximum Depth of Binary Tree

# The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.

# -------------------------------------------------------------
# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -------------------------------------------------------------
# Recursive DFS Solution
def maxDepth(root):
    # Base case: empty tree
    if not root:
        return 0

    # Recursively find depth of left and right subtree
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # Return max depth + current node
    return 1 + max(left_depth, right_depth)


# -------------------------------------------------------------
# Main function (example usage)
def main():
    # Creating the following tree:
    #
    #         1
    #       /   \
    #      2     3
    #     / \
    #    4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    depth = maxDepth(root)
    print("Maximum Depth of Tree:", depth)


# -------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    main()


# -------------------------------------------------------------
# Complexity Analysis:
#
# Time Complexity: O(n)
# - We visit every node exactly once
#
# Space Complexity: O(h)
# - h = height of tree (recursive stack)
# - Worst case: O(n) (skewed tree)
# - Best case: O(log n) (balanced tree)
#
# -------------------------------------------------------------
# Key Insight:
# This is a classic DFS problem:
# depth = 1 + max(left_subtree, right_subtree)
#
# -------------------------------------------------------------
# Interview Tip:
# If interviewer asks for iterative:
# → Use BFS (level order traversal with queue)