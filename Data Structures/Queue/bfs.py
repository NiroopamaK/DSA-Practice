# Breadth-First Search (BFS) using Queue

from collections import deque


def bfs(graph, start):
    visited = set([start])   # mark visited when enqueuing
    q = deque([start])

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


# -------------------------------------------------------------
# Main function
def main():
    # Graph represented as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS Traversal:")
    bfs(graph, 'A')


# -------------------------------------------------------------
if __name__ == "__main__":
    main()


# -------------------------------------------------------------
# Complexity Analysis:
#
# Time Complexity: O(V + E)
# - V = vertices, E = edges
#
# Space Complexity: O(V)
# - visited set + queue
#
# -------------------------------------------------------------
# Key Insight:
# - Use queue (FIFO)
# - Visit nodes level by level
# - Mark visited EARLY (when adding to queue)
#
# -------------------------------------------------------------
# Why visited is needed:
# Prevents infinite loops in cyclic graphs:
#
# A → B → A → B → ...
#
# Without visited → infinite loop