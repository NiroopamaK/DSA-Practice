# Problem: Smallest subarray with sum >= target

# Approach (Variable Sliding Window):
# We expand the window by moving the right pointer and adding elements.
# Once the window sum becomes >= target, we try to shrink it from the left
# to find the smallest valid window.
#
# This ensures we always maintain the minimum possible subarray length.

# Time Complexity: O(n)
# Space Complexity: O(1)

def smallest_sub_arry_with_target(arr, target):
    left = 0
    window_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_len if min_len != float('inf') else 0


def main():
    arr = [1, 2, 3, 5, 1, 3, 6, 7]
    target = 9

    result = smallest_sub_arry_with_target(arr, target)
    print("Smallest subarray length:", result)


if __name__ == "__main__":
    main()