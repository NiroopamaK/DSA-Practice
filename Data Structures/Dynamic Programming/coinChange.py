# Coin Change Problem (Minimum Coins - DP)

# Problem:
# Given coins and an amount,
# find minimum number of coins needed to make that amount.
#
# If not possible → return -1
#
# -------------------------------------------------------------
# Idea:
# dp[i] = minimum coins needed to make amount i
#
# Transition:
# dp[i] = min(dp[i], dp[i - coin] + 1)
#
# -------------------------------------------------------------
# Time Complexity: O(amount * len(coins))
# Space Complexity: O(amount)
# -------------------------------------------------------------

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # base case

    for i in range(amount + 1):
        for c in coins:
            if i - c >= 0:   # prevent invalid index
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Main function
def main():
    coins = [1, 2, 5]
    amount = 11

    print("Minimum coins needed:", coinChange(coins, amount))


# -------------------------------------------------------------
if __name__ == "__main__":
    main()