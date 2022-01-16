"""
동전 분배하기(DFS)
N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다.
세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 총액이 가장 큰
사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
단 세 사람의 총액은 서로 달라야 합니다.

▣ 입력설명
첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다.
그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.

▣ 출력설명
총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.

▣ 입력예제 1
7
8
9
11
12
23
15
17

▣ 출력예제 1
5
"""
import sys


def dfs(level):
    global answer

    if level == num_coin:
        if len(set(result)) == len(result):
            temp = max(result) - min(result)
            # print("\nlevel: ", level)
            # print("result: ", result)
            if temp < answer:
                answer = temp

    else:
        for i in range(3):
            result[i] += value_coin[level]
            dfs(level+1)
            result[i] -= value_coin[level]


if __name__ == "__main__":
    # sys.stdin = open("in1.txt", "rt")

    num_coin = int(input())
    value_coin = []
    for _ in range(num_coin):
        value_coin.append(int(input()))

    result = [0] * 3
    answer = 2147000
    dfs(0)
    print(answer)

