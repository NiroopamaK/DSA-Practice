# Problem: Maximum sum of a subarray of size k

# Brute Force Approach:
# Try every possible subarray of size k
# Compute sum each time and track maximum
# Time Complexity: O(n * k)

# Optimized Approach (Sliding Window):
# Compute sum of first window
# Slide the window by removing left element and adding new right element
# Time Complexity: O(n)

def max_sub_array(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def main():
    arr = [3, 4, 1, 5, 5, 5, 6, 4, 7, 9]
    k = 3

    result = max_sub_array(arr, k)
    print("Maximum subarray sum:", result)


if __name__ == "__main__":
    main()