if __name__ == '__main__':
    INF = 99999

    coin_num, target = map(int, input().split())
    coin_values = []
    for _ in range(coin_num):
        coin_values.append(int(input()))

    dp = [INF] * (target+1)
    dp[0] = 0

    for i in range(1, target+1):
        possible_coins = [cv for cv in coin_values if cv <= i]

        if not possible_coins:
            continue

        dp[i] = min([dp[i-pc] for pc in possible_coins]) + 1

    if dp[-1] >= INF:
        print(-1)
    else:
        print(dp[-1])
