# Problem: Container With Most Water

# Given an array where each element represents the height of a vertical line,
# find two lines that together with the x-axis form a container that holds the most water.

# Brute Force Approach
# Try all possible pairs of lines

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def max_area_brute(height):
    max_area = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            current_area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, current_area)

    return max_area

# Approach: Two Pointers
# Start with two pointers at both ends of the array.
# Calculate area between them.
# Move the pointer pointing to the smaller height inward,
# since that is the limiting factor.

# Time Complexity: O(n)
# Space Complexity: O(1)

def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, current_area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_area


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    result = max_area(height)
    print("Maximum water container area:", result)


if __name__ == "__main__":
    main()