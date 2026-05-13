# Problem: Remove duplicates from an array

# Approach:
# slow -> tracks last unique element position
# fast -> iterates through the array
# If arr[fast] != arr[slow], we found a new unique element
# Move slow pointer forward and update value

# Note: Array is sorted first to group duplicates together
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) extra (ignoring sorting overhead)

def remove_duplicates(arr):
    arr = sorted(arr)
    slow = 0

    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]

    return arr[:slow + 1]


def main():
    arr = [3, 4, 1, 5, 5, 5, 6, 4, 7, 9]

    result = remove_duplicates(arr)
    print("Array after removing duplicates:", result)


if __name__ == "__main__":
    main()