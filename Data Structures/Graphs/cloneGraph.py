# Clone Graph (DFS)

# Problem:
# Given a reference node of a connected graph,
# return a deep copy (clone) of the graph.
#
# Each node contains:
# - val
# - neighbors (list of adjacent nodes)
#
# -------------------------------------------------------------
# Idea:
# - Use DFS to traverse graph
# - Use hashmap (old → new) to:
#     1. Avoid cycles
#     2. Prevent duplicate copies
#
# Steps:
# - If node already cloned → return it
# - Create copy
# - Store in hashmap
# - Recursively clone neighbors
#
# -------------------------------------------------------------
# Time Complexity:
# O(V + E)
#
# Space Complexity:
# O(V)
#
# -------------------------------------------------------------


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def cloneGraph(node):
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node) if node else None


# Helper function to print graph (DFS)
def printGraph(node, visited):
    if node in visited:
        return

    visited.add(node)
    print(f"Node {node.val} -> {[n.val for n in node.neighbors]}")

    for nei in node.neighbors:
        printGraph(nei, visited)

# Main function
def main():
    # Create sample graph:
    # 1 -- 2
    # |    |
    # 4 -- 3

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    print("Original Graph:")
    printGraph(node1, set())

    cloned = cloneGraph(node1)

    print("\nCloned Graph:")
    printGraph(cloned, set())


# -------------------------------------------------------------
if __name__ == "__main__":
    main()