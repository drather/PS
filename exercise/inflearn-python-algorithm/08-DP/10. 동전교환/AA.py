"""
동전교환
다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환
해주려면 어떻게 주면 되는가? 각 단위의 동전은 무한정 쓸 수 있다.

▣ 입력설명
첫 번째 줄에는 동전의 종류개수 N(1<=N<=100)이 주어진다. 두 번째 줄에는 N개의 동전의
종류가 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=10,000)이 주어진다.
각 동전의 종류는 100원을 넘지 않는다.

▣ 출력설명
첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.

▣ 입력예제 1
3
1 2 5
15

▣ 출력예제 1
3

설명 : 5 5 5 동전 3개로 거슬러 줄 수 있다.
"""
import sys

if __name__ == "__main__":
    # sys.stdin = open("in1.txt", "rt")
    num_coin = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [111] * (target+1)
    dp[0] = 0
    for i in range(num_coin):
        # print("\ni: ", i)
        for j in range(coins[i], target+1):
            # print("\tj: ", j)
            # print("\tdp[j]: ", dp[j])
            # print("\tdp[j-coins[i]] + 1: ", dp[j-coins[i]] + 1)
            dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        # print("dp: ", dp)
    print(dp[target])
