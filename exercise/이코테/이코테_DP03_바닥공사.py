

if __name__ == '__main__':
    width = int(input())

    dp = [0] * (width + 1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, width + 1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    print(dp[-1] % 796796)



