# Breadth-First Search (BFS) using Queue

from collections import deque


def bfs(graph, start):
    visited = set([start])
    q = deque([start])

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


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

    start_node = 1

    print("BFS Traversal starting from node", start_node, ":")
    bfs(graph, start_node)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()


# -------------------------------------------------------------
# Complexity Analysis:
#
# Time Complexity:
# O(V + E)
# - V = number of vertices
# - E = number of edges
#
# Space Complexity:
# O(V)
# - visited set + queue
#
# -------------------------------------------------------------
# Key Insight:
# - Use queue (FIFO) for level-by-level traversal
# - visited prevents infinite loops in cyclic graphs
#
# -------------------------------------------------------------
# Interview Tip:
# Always say:
# "We use a visited set to avoid revisiting nodes
# and ensure O(V + E) complexity."