# Problem: Subarray Sum Equals K

# Given an array of integers and an integer target,
# return the total number of continuous subarrays
# whose sum equals target.

# Approach: Prefix Sum + Hash Map
# We keep track of cumulative (prefix) sums while iterating.
#
# If at any point:
# prefix_sum - target exists in the hashmap,
# it means there is a subarray ending at current index
# with sum equal to target.
#
# The hashmap stores:
# prefix_sum -> frequency

# Time Complexity: O(n)
# Single pass through the array

# Space Complexity: O(n)
# In worst case, storing all prefix sums


def sub_array_sum(arr, target):
    prefix_sum = 0
    count = 0
    hashmap = {0: 1}  # Handles subarrays starting from index 0

    for num in arr:
        prefix_sum += num

        if (prefix_sum - target) in hashmap:
            count += hashmap.get(prefix_sum - target)

        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count


def main():
    arr = [2, 3, 7, 1, 6, 8]
    target = 7

    result = sub_array_sum(arr, target)
    print("Number of subarrays:", result)


if __name__ == "__main__":
    main()