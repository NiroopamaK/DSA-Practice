# Best Time to Buy and Sell Stock (Greedy)


# Problem:
# Given an array prices where prices[i] is the price of a stock
# on day i, find the maximum profit you can achieve.
#
# You may choose ONE day to buy and ONE later day to sell.
#
# Return the maximum profit. If no profit is possible, return 0.
#
# -------------------------------------------------------------
# Example:
# prices = [7,1,5,3,6,4]
#
# Output: 5
# Explanation:
# Buy at 1, sell at 6 → profit = 5
#
# -------------------------------------------------------------
# Idea:
#
# - Track the minimum price seen so far
# - At each day:
#     profit = current price - min_price
# - Keep updating maximum profit
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------


class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update minimum buying price
            min_price = min(min_price, price)

            # Calculate profit if sold today
            profit = price - min_price

            # Update max profit
            max_profit = max(max_profit, profit)

        return max_profit


# -------------------------------------------------------------
# Main function
# -------------------------------------------------------------
def main():
    prices = [7, 1, 5, 3, 6, 4]

    sol = Solution()
    result = sol.maxProfit(prices)

    print("Maximum Profit:", result)  # Expected: 5


# -------------------------------------------------------------
if __name__ == "__main__":
    main()