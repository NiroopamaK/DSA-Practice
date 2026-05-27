# Merge Intervals (Greedy)

# Problem:
# Given a collection of intervals, merge all overlapping intervals.
#
# -------------------------------------------------------------
# Idea:
# 1. Sort intervals by start time
# 2. Iterate through intervals:
#    - If overlap → merge
#    - Else → add new interval
#
# -------------------------------------------------------------
# Time Complexity: O(n log n) (sorting)
# Space Complexity: O(n)
# -------------------------------------------------------------


def merge(intervals):
    if not intervals:
        return []

    # Step 1: sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    # Step 2: merge intervals
    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        # Overlap
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged

# Main function
def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    print("Merged intervals:", merge(intervals))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()