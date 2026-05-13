# Problem: Range Sum Query (Inclusive)

# Given an array, answer multiple range sum queries efficiently.

# Approach: Prefix Sum Array
# We precompute prefix sums so that:
# sum(left, right) = prefix[right] - prefix[left - 1]
#
# This reduces each query from O(n) to O(1)

# Time Complexity:
# Preprocessing: O(n)
# Query: O(1)

# Space Complexity: O(n)

class RangeSum:

    def __init__(self, arr):
        self.prefix = [0] * len(arr)
        self.prefix[0] = arr[0]

        for i in range(1, len(arr)):
            self.prefix[i] = self.prefix[i - 1] + arr[i]

    def sum_range(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


def main():
    arr = [3, 4, 1, 2, 5, 6]

    rs = RangeSum(arr)

    result = rs.sum_range(2, 5)
    print("Range sum:", result)


if __name__ == "__main__":
    main()