"""
마찬가지로 점화식을 떠올려라

알고리즘 수업떄도 나왔던 대표적인 예제이다. 못풀면 안된다.

동전 갯수는 2, 값어치는 15, 동전의 가치는 [2, 3] 이라 하자.

점화식은 다음과 같다.
a[i] = min(a[i-2], a[i-3]) + 1

이를 일반화하자면 다음과 같다.
동전의 가치를 각각 c1, c2, ... , cn 이라 할 때,

a[i] = min(a[i-c1], a[i-c2], ... a[i-cm]), m 은 i 보다 작거나 같은 자연수로, i 보다 같거나 작으면서 동전의 가치중 가장 큰 값임

이러한 점화식이 나오는 이유는 전에 풀었던 DP 문제와 마찬가지로,
dp[i] 를 결정하는데, dp[i-c] 값이 있다면, 그값에 1을 더한 값들 중에서 가장 최소값이 되기 때문이다.

다음 순서로 코드를 작성한다.

0. 인풋 입력
1. 값 초기화
2. dp 배열 루핑 돌면서,
    2.1 인덱스 i, 즉 만들고자 하는 값어치 보다 작거나 같은 가치를 가진 동전이 있는지를 확인
        - 없으면, 해당 값어치는 만들 수 없는 숫자로, 무한대가 남음
    2.2 있으면, 가능한 동전들을 루핑 돌면서,
        - dp[i - coin_value] 의 값 중 가장 작은 값을 찾아서, 1을 더한 값을 dp[i] 의 값으로 함
3. 정답 출력
"""

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
