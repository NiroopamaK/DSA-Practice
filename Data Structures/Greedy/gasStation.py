# Gas Station (Greedy)

# Problem:
# Find the starting gas station index from which you can travel
# around the circuit once. Return -1 if impossible.
#
# -------------------------------------------------------------
# Idea:
# - Track total_tank (global feasibility)
# - Track curr_tank (local segment)
#
# If curr_tank becomes negative:
# → cannot start from current start
# → move start to next index
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------


def canCompleteCircuit(gas, cost):
    total_tank = 0
    curr_tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]

        total_tank += diff
        curr_tank += diff

        # If we can't reach next station
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0

    return start if total_tank >= 0 else -1


# Main function
def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    print("Starting index:", canCompleteCircuit(gas, cost))  # Expected: 3


# -------------------------------------------------------------
if __name__ == "__main__":
    main()