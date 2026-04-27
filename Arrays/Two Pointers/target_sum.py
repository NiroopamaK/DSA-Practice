# Problem: Find two numbers that sum to target

# Brute Force Approach:
# Use two nested loops to check every pair
# Time Complexity: O(n^2)

# Optimized Approach (Two Pointers):
# Sort the array and use left + right pointers
# Time Complexity: O(n log n) for sorting + O(n) traversal

# If the sum of the values in left and right indices are higher than the target
# right index is reduced
# If the sum of the values in left and right indices are lower than the target
# left index is increased

def target_sum(arr, target):
    ar = sorted(arr)
    left = 0
    right = len(ar) - 1

    while left < right:
        if ar[left] + ar[right] == target:
            return [left, right]
        elif ar[left] + ar[right] > target:
            right -= 1
        else:
            left += 1

    return None


def main():
    arr = [2, 7, 11, 15]
    target = 9

    result = target_sum(arr, target)

    if result:
        print(f"Indices in sorted array: {result}")
    else:
        print("No pair found")


if __name__ == "__main__":
    main()