

# houses = list(map(int, input().split()))
houses = [1, 3, 1, 5]


if __name__ == '__main__':
    dp = [0] * len(houses)
    dp[0] = houses[0]

    for i in range(1, len(houses)):
        if i == 1:
            dp[i] = max(houses[i], dp[i-1])

        else:
            dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    print(dp[-1])