# Detect Cycle in a Directed Graph using DFS

# Idea:
# - Use DFS traversal
# - Track:
#   1. visited → nodes already processed
#   2. recStack → nodes in current DFS path
#
# Cycle Condition:
# - If we revisit a node in recStack → cycle exists
#
# -------------------------------------------------------------
# Why recStack is needed:
#
# Directed graph example:
# 1 → 2 → 3 → 4
#       ↑     ↓
#       ← ← ←
#
# When DFS reaches 3 again while still in recursion path,
# we detect a cycle
#
# -------------------------------------------------------------
# Time Complexity:
# O(V + E)
#
# Space Complexity:
# O(V)
#
# -------------------------------------------------------------


def hasCycleDirected(graph):
    visited = set()
    recStack = set()

    def dfs(node):
        # Case 1: Node is in current recursion path → cycle
        if node in recStack:
            return True

        # Case 2: Already processed → no cycle from here
        if node in visited:
            return False

        visited.add(node)
        recStack.add(node)

        for nei in graph[node]:
            if dfs(nei):
                return True

        # Backtrack
        recStack.remove(node)
        return False

    # Handle disconnected components
    for node in graph:
        if dfs(node):
            return True

    return False


# Main function
def main():
    # Graph WITH cycle
    graph_with_cycle = {
        1: [2],
        2: [3],
        3: [4],
        4: [2]   # cycle here
    }

    # Graph WITHOUT cycle
    graph_without_cycle = {
        1: [2],
        2: [3],
        3: [],
        4: [1]
    }

    print("Graph with cycle:",
          hasCycleDirected(graph_with_cycle))

    print("Graph without cycle:",
          hasCycleDirected(graph_without_cycle))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()