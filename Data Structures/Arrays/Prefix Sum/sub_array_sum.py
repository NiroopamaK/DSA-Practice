# Problem:
# Given an array nums and integer k,
# return the number of continuous subarrays whose sum equals k.

# Approach:
# Prefix Sum + Hash Map (Frequency Map)
#
# Idea:
# If current_sum - k has been seen before,
# it means there exists a subarray ending at current index with sum k.
#
# We store frequency of prefix sums to count all valid subarrays.

# Time Complexity: O(n)
# Space Complexity: O(n)

def subArraySum(nums, k):
    count = 0
    current_sum = 0
    freq = {0: 1}

    for n in nums:
        current_sum += n

        if current_sum - k in freq:
            count += freq[current_sum - k]

        freq[current_sum] = freq.get(current_sum, 0) + 1

    return count


def main():
    nums = [3, 4, 1, 2, 5, 6]
    k = 3

    result = subArraySum(nums, k)
    print("Number of subarrays:", result)


if __name__ == "__main__":
    main()