# Binary Tree Traversals (Preorder, Inorder, Postorder)

# -------------------------------------------------------------
# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# -------------------------------------------------------------
# Preorder Traversal (Root → Left → Right)
def preOrderTraversal(root):
    if not root:
        return

    print(root.data, end=", ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


# -------------------------------------------------------------
# Inorder Traversal (Left → Root → Right)
def inOrderTraversal(root):
    if not root:
        return

    inOrderTraversal(root.left)
    print(root.data, end=", ")
    inOrderTraversal(root.right)


# -------------------------------------------------------------
# Postorder Traversal (Left → Right → Root)
def postOrderTraversal(root):
    if not root:
        return

    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=", ")


# -------------------------------------------------------------
# Main function (Entry point)
def main():
    # Creating the following binary tree:
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

    print("Preorder Traversal:")
    preOrderTraversal(root)

    print("\n\nInorder Traversal:")
    inOrderTraversal(root)

    print("\n\nPostorder Traversal:")
    postOrderTraversal(root)


# -------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    main()


# -------------------------------------------------------------
# Complexity Analysis:
#
# Time Complexity:
# O(n) → Each node is visited exactly once
#
# Space Complexity:
# O(h) → Recursive stack space (h = height of tree)
# Worst case: O(n) (skewed tree)
# Best case: O(log n) (balanced tree)
#
# -------------------------------------------------------------
# Notes:
# - Preorder → Useful for copying tree
# - Inorder → Gives sorted order (BST)
# - Postorder → Useful for deleting tree