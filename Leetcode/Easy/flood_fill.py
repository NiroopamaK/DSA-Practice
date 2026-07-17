# Flood Fill (DFS)

# Problem:
# Given a 2D image, a starting pixel (sr, sc),
# and a new color, fill all connected pixels
# (4-directionally) with the same original color.
#
# -------------------------------------------------------------
# Example:
#
# Input:
# image = [
#   [1,1,1],
#   [1,1,0],
#   [1,0,1]
# ]
# sr = 1, sc = 1, color = 2
#
# Output:
# [
#   [2,2,2],
#   [2,2,0],
#   [2,0,1]
# ]
#
# -------------------------------------------------------------
# Approach:
#
# - Use DFS to explore connected cells
# - Replace only cells matching original color
#
# -------------------------------------------------------------
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) (recursion stack)
# -------------------------------------------------------------


class Solution:
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]

        # Edge case: no change needed
        if original == color:
            return image

        def dfs(r, c):
            # Boundary + color check
            if (
                r < 0 or r >= len(image) or
                c < 0 or c >= len(image[0]) or
                image[r][c] != original
            ):
                return

            # Fill color
            image[r][c] = color

            # Explore neighbors (4 directions)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image