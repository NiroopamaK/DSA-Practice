# Problem: Reverse an array

# Approach:
# Use two pointers:
# left starts from beginning, right starts from end
# Swap elements until both pointers meet in the middle

# Time Complexity: O(n)
# Space Complexity: O(1)

def rev_arr(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def main():
    arr = [3, 4, 1, 5, 5, 5, 6, 4, 7, 9]

    result = rev_arr(arr)
    print("Reversed array:", result)


if __name__ == "__main__":
    main()