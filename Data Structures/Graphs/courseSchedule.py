# Course Schedule (Detect Cycle in Directed Graph using DFS)

# Problem:
# Determine if all courses can be finished given prerequisites
#
# Graph:
# b → a means:
# must take course b before course a
#
# Idea:
# - Detect cycle in directed graph
# - Use DFS with:
#   visited  → fully processed nodes
#   recStack → current DFS path
#
# If a node appears again in recStack → cycle exists
#
# -------------------------------------------------------------
# Time Complexity:
# O(V + E)
#
# Space Complexity:
# O(V)
#
# -------------------------------------------------------------


def canFinish(numOfCourses, prerequisites):
    # Build graph
    graph = {i: [] for i in range(numOfCourses)}

    for a, b in prerequisites:
        graph[b].append(a)

    visited = set()
    recStack = set()

    def dfs(course):
        # Cycle detected
        if course in recStack:
            return False

        # Already processed
        if course in visited:
            return True

        recStack.add(course)

        for nei in graph[course]:
            if not dfs(nei):
                return False

        recStack.remove(course)
        visited.add(course)   # mark safe AFTER processing
        return True

    # Check all components
    for c in range(numOfCourses):
        if not dfs(c):
            return False

    return True


# Main function
def main():
    numCourses = 4

    # Case 1: No cycle
    prerequisites1 = [[1, 0], [2, 1], [3, 2]]
    print("Can finish (no cycle):",
          canFinish(numCourses, prerequisites1))

    # Case 2: Has cycle
    prerequisites2 = [[1, 0], [0, 1]]
    print("Can finish (cycle):",
          canFinish(numCourses, prerequisites2))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()