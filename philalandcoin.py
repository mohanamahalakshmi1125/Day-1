def minCoins(coins, amount):
    # Create a table to store the minimum number of coins for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Fill the dp table
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
print("Minimum coins needed =", minCoins([1, 2, 5], 11))