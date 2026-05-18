# Problem: Lowest Common Ancestor (LCA) in a Binary Tree

# The LCA of two nodes p and q is the lowest node in the tree
# that has both p and q as descendants.

# -------------------------------------------------------------
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -------------------------------------------------------------
# Recursive DFS Solution
def lowestCommonAncestor(root, p, q):
    # Base case:
    # - If root is None
    # - If root matches p or q
    if not root or root == p or root == q:
        return root

    # Search left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # Case 1: p and q found in different subtrees
    if left and right:
        return root

    # Case 2: Either one side found p/q
    return left if left else right


# -------------------------------------------------------------
# Main function (example usage)
def main():
    # Creating tree:
    #
    #         3
    #       /   \
    #      5     1
    #     / \   / \
    #    6   2 0   8
    #       / \
    #      7   4

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left              # Node 5
    q = root.left.right.right # Node 4

    lca = lowestCommonAncestor(root, p, q)

    print("LCA of", p.val, "and", q.val, "is:", lca.val)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()


# -------------------------------------------------------------
# Complexity Analysis:
#
# Time Complexity: O(n)
# - In worst case, we traverse all nodes
#
# Space Complexity: O(h)
# - h = height of tree (recursive stack)
# - Worst case: O(n), Best case: O(log n)
#
# -------------------------------------------------------------
# Key Insight:
# - If both left and right return non-null → current node is LCA
# - If only one side returns → propagate it upward
#
# -------------------------------------------------------------
# Intuition:
#
# The recursion "bubbles up" nodes:
#
# - If p and q are in different branches → they meet at LCA
# - If both are in same branch → LCA is deeper