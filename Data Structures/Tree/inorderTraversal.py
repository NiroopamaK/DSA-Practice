from collections import deque

# -------------------------------------------------------------
# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -------------------------------------------------------------
# Level Order Traversal (BFS)
def levelOrderTraversal(root):
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        level = []
        size = len(q)  # number of nodes at current level

        for _ in range(size):
            node = q.popleft()
            level.append(node.data)  # store value (not node)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.append(level)

    return res


# -------------------------------------------------------------
# Main function
def main():
    # Creating tree:
    #
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    result = levelOrderTraversal(root)
    print("Level Order Traversal:", result)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()


# -------------------------------------------------------------
# Complexity Analysis:
#
# Time Complexity: O(n)
# - Every node is processed once
#
# Space Complexity: O(n)
# - Queue stores nodes level by level
#
# -------------------------------------------------------------
# Key Insight:
# Use queue size to separate levels
#
# -------------------------------------------------------------
# Output:
# [[1], [2, 3], [4, 5, 6, 7]]