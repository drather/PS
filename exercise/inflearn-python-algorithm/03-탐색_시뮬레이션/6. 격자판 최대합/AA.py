"""
격자판 최대합
5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다.

▣ 출력설명
최대합을 출력합니다.

▣ 입력예제 1
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

▣ 출력예제 1
155
"""
import sys
# sys.stdin = open("in1.txt", "rt")

width = int(input())
board = []
for _ in range(width):
    board.append(list(map(int, input().split())))

max_value = -1

for i in range(len(board)):
    sum1 = 0
    sum2 = 0
    for j in range(len(board)):
        sum1 += board[i][j]
        sum2 += board[j][i]

    if sum1 > sum2:
        temp = sum1

    else:
        temp = sum2

    if temp > max_value:
        max_value = temp

sum3 = 0
for i in range(len(board)):
    sum3 += board[i][i]

sum4 = 0
for i in range(len(board)):
    sum4 += board[i][width-i-1]

print(max(max_value, sum3, sum4))







