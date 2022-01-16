"""
섬나라 아일랜드(BFS 활용)
섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다. 각 섬은 1로 표시되어 상하좌우와 대
각선으로 연결되어 있으며, 0은 바다입니다. 섬나라 아일랜드에 몇 개의 섬이 있는지 구하는
프로그램을 작성하세요.

1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0

만약 위와 같다면

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다.
두 번째 줄부터 격자판 정보가 주어진다.

▣ 출력설명
첫 번째 줄에 섬의 개수를 출력한다.

▣ 입력예제 1
7
1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0

▣ 출력예제 1
5
"""
import sys
from _collections import deque as dq

# sys.stdin = open("in1.txt", "rt")

answer = 0

drow = [-1, 0, 1]
dcol = [-1, 0, 1]


length = int(input())
board = []

for _ in range(length):
    board.append(list(map(int, input().split())))

check = [[0] * length for _ in range(length)]

for r in range(length):
    for c in range(length):
        if board[r][c] != 0 and check[r][c] == 0:
            answer += 1
            queue = dq([(r, c)])

            while queue:
                q_size = len(queue)

                for i in range(q_size):
                    src = queue.popleft()
                    row = src[0]
                    col = src[1]
                    # print("\nsrc: ", (row, col))
                    for j in range(9):
                        for m in drow:
                            for n in dcol:
                                new_row = row + m
                                new_col = col + n

                                if 0 <= new_row < length and 0 <= new_col < length and check[new_row][new_col] == 0 and board[new_row][new_col] == 1:
                                    nw = (new_row, new_col)
                                    # print("\t", nw)
                                    queue.append((new_row, new_col))
                                    check[new_row][new_col] = 1

# for i in range(length):
#     print(board[i])
#
# print()
#
# for i in range(length):
#     print(check[i])
print(answer)

