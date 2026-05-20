# Number of Islands (DFS - Grid Traversal)
# -------------------------------------------------------------

# Problem:
# Count the number of islands in a grid
# - "1" = land
# - "0" = water
#
# Idea:
# - Traverse each cell
# - When we find an unvisited "1":
#     → run DFS to mark the entire island
#     → increment count
#
# DFS explores 4 directions:
# up, down, left, right
#
# -------------------------------------------------------------
# Time Complexity:
# O(rows * cols)
#
# Space Complexity:
# O(rows * cols)  (visited + recursion stack)
#
# -------------------------------------------------------------


def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        # Base case: out of bounds OR water OR already visited
        if (r < 0 or c < 0 or
            r >= rows or c >= cols or
            grid[r][c] == "0" or
            (r, c) in visited):
            return

        visited.add((r, c))

        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                count += 1

    return count


# Main function
def main():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print("Number of Islands:", numIslands(grid))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()