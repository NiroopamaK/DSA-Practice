# Depth-First Search (DFS) using Recursion
# -------------------------------------------------------------

# DFS explores as far as possible along each branch before backtracking
#
# Key Ideas:
# - Use recursion (implicit stack)
# - Use a visited set to avoid cycles
# - Traverse neighbors depth-wise
#
# Why visited is needed:
# - Graphs can have cycles (A → B → A)
# - Prevents infinite recursion
# - Ensures each node is processed once
#
# Time Complexity:
# O(V + E)
# - V = vertices, E = edges
#
# Space Complexity:
# O(V)
# - recursion stack + visited set
#
# DFS Order (example):
# 1 → 2 → 4 → 5 → 3 → 6
#
# -------------------------------------------------------------


def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)
    print(node, end=" ")

    for nei in graph[node]:
        dfs(graph, nei, visited)


# Main function
def main():
    # Graph represented as adjacency list
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [6],
        6: []
    }

    visited = set()
    start_node = 1

    print("DFS Traversal starting from node", start_node, ":")
    dfs(graph, start_node, visited)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()