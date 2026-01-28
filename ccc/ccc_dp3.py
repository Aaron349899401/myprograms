def max_snack_value(values):
    if not values:
        return 0
    if len(values) == 1:
        return values[0]

    # dp[i] = max value using boxes up to index i
    dp = [0] * len(values)
    dp[0] = values[0]
    dp[1] = max(values[0], values[1])

    for i in range(2, len(values)):
        dp[i] = max(dp[i-1], dp[i-2] + values[i])

    return dp[-1]

# Example
print(max_snack_value([5, 1, 2, 10, 6, 2]))  # Output: 17