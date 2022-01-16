"""
네트워크 선 자르기(Top-Down : 재귀, 메모이제이션)
현수는 네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다.
예를 들어 4m의 네트워크 선이 주어진다면

1) 1m+1m+1m+1m
2) 2m+1m+1m
3) 1m+2m+1m
4) 1m+1m+2m
5) 2m+2m

의 5가지 방법을 생각할 수 있습니다. (2)와 (3)과 (4)의 경우 왼쪽을 기준으로 자르는 위치가
다르면 다른 경우로 생각한다.
그렇다면 네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?

▣ 입력설명
첫째 줄은 네트워크 선의 총 길이인 자연수 N(3≤N≤45)이 주어집니다.

▣ 출력설명
첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.

▣ 입력예제 1
7

▣ 출력예제 1
21
"""
import sys


def dfs(n):
    global dp

    if n == 1 or n == 2:
        return n

    elif dp[n] > 0:
        return dp[n]

    else:
        dp[n] = dfs(n-1) + dfs(n-2)


def top_down(length):
    dp = [0] * (length + 1)
    dp[1] = 1
    dp[2] = 2
    dfs(length)


def bottom_up(length):
    for i in range(3, length+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[length]


if __name__ == "__main__":
    sys.stdin = open("in1.txt", "rt")
    num = int(input())

    dp = [0] * (num + 1)
    dp[1] = 1
    dp[2] = 2

    # print(top_down(num))
    print(bottom_up(num))

