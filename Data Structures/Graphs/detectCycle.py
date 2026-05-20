# Detect Cycle in an Undirected Graph using DFS
# -------------------------------------------------------------

# Idea:
# - Traverse graph using DFS
# - Keep track of visited nodes
# - Track parent to avoid false cycle detection
#
# For each neighbor:
# - If not visited → recurse
# - If visited AND not parent → cycle found
#
# -------------------------------------------------------------
# Why parent is needed:
# In undirected graph:
# A --- B
# If we go A → B → A,
# we should NOT detect a cycle
#
# parent helps ignore this back edge
#
# -------------------------------------------------------------
# Time Complexity:
# O(V + E)
#
# Space Complexity:
# O(V)
#
# -------------------------------------------------------------


def hasCycle(graph, node, visited, parent):
    visited.add(node)

    for nei in graph[node]:
        # Case 1: Not visited → explore deeper
        if nei not in visited:
            if hasCycle(graph, nei, visited, node):
                return True

        # Case 2: Visited and not parent → cycle
        elif nei != parent:
            return True

    return False


# Main function
def main():
    # Example 1: Graph WITH cycle
    graph_with_cycle = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3]
    }

    # Example 2: Graph WITHOUT cycle
    graph_without_cycle = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3]
    }

    print("Graph with cycle:",
          hasCycle(graph_with_cycle, 1, set(), -1))

    print("Graph without cycle:",
          hasCycle(graph_without_cycle, 1, set(), -1))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()