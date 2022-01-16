"""
동전 거스름돈 문제
- 동전이 d1, d2, ... , dm의 동전으로 n만큼의 금액을 맞추면서, 사용한동전의 최소 갯수를 출력하는 문제
- 각 동전의 갯수는 무한하다.

입력: 동전의 값어치를 나타내는 배열 coins, 금액을 나타내는 정수 n

출력: n만큼의 합을 갖는 동전들의 모임
"""





def solution2(coins, money):
    # dp배열 초기화
    dp = [0] * (money + 1)

    # 1부터 money까지 순회한다.
    for i in range(1, money + 1):
        # temp = 임의의 큰 값
        temp = 9999
        j = 0

        # j가 coins의 갯수보다 작으면서, i의 값이 coins[j]보다 작은 동안 값을 비교한다.
        while j < len(coins) and i >= coins[j]:
            temp = min(dp[i-coins[j]], temp)
            j += 1
        dp[i] = temp + 1

    print(dp)
    return dp[money]

coins = [1,3,4]
money = 6
print(solution2(coins, money))