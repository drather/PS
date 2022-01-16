"""
최대점수 구하기(냅색 알고리즘)
이번 정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를
풀려고 합니다. 각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩
니다. 제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다. (해당문제는
해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다.)

▣ 입력설명
첫 번째 줄에 문제의 개수N(1<=N<=100)과 제한 시간 M(10<=M<=1000)이 주어집니다.
두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.

▣ 출력설명
첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.

▣ 입력예제 1
5 20
10 5
25 12
15 8
6 3
7 4

▣ 출력예제 1
41
"""
import sys


def dfs():
    pass


if __name__ == "__main__":
    sys.stdin = open("in2.txt", "rt")

    q_num, t_limit = map(int, input().split())

    dp = [0] * (t_limit+1)

    for i in range(q_num):
        score, time = map(int, input().split())

        for j in range(t_limit, time-1, -1):
            dp[j] = max(dp[j], dp[j-time] + score)

    print(dp[t_limit])

    # # 이 아래는 2차원배열로 해결한 것.
    # dp = [[0] * (t_limit+1) for _ in range(q_num+1)]

    # for i in range(1, q_num+1):
    #     for k in range(t_limit+1):
    #         dp[i][k] = dp[i-1][k]
    #
    #     score, time = map(int, input().split())
    #
    #     for j in range(time, t_limit+1):
    #         dp[i][j] = max(dp[i][j], dp[i-1][j-time] + score)
    #
    # print(dp[-1][-1])