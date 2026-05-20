# Rotting Oranges (Multi-source BFS)

# Problem:
# Given a grid:
# 0 = empty cell
# 1 = fresh orange
# 2 = rotten orange
#
# Each minute:
# Rotten oranges spread to adjacent fresh ones (4 directions)
#
# Return:
# - Minimum minutes until all oranges rot
# - OR -1 if impossible
#
# -------------------------------------------------------------
# Idea:
# - Start BFS from ALL rotten oranges at once
# - Each BFS level = 1 minute
# - Track fresh oranges count
#
# -------------------------------------------------------------
# Time Complexity: O(rows * cols)
# Space Complexity: O(rows * cols)
# -------------------------------------------------------------


from collections import deque


def rottingOranges(grid):
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    # Step 1: Initialize queue + count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    # Edge case: no fresh oranges
    if fresh == 0:
        return 0

    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Step 2: BFS
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1

        minutes += 1

    return minutes if fresh == 0 else -1


# Main function
def main():
    grid1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    grid2 = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]

    print("Minutes (grid1):", rottingOranges(grid1))  # Expected: 4
    print("Minutes (grid2):", rottingOranges(grid2))  # Expected: -1


# -------------------------------------------------------------
if __name__ == "__main__":
    main()