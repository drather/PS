"""
미로의 최단거리 통로(BFS 활용)
7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력하는 프로그램을 작성하세요. 경로수는
출발점에서 도착점까지 가는데 이동한 횟수를 의미한다. 출발점은 격자의 (1, 1) 좌표이고, 탈
출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 도로이다.
격자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면

출발   0    0   0  0   0   0
  0   1    1   1  1   1   0
  0   0    0   1  0   0   0
  1   1    0   1  0   1   1
  1   1    0   1  0   0   0
  1   0    0   0  1   0   0
  1   0    1   0  0   0   도착
위와 같은 경로가 최단 경로이며 경로수는 12이다.
▣ 입력설명
7*7 격자판의 정보가 주어집니다.

▣ 출력설명
첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.

▣ 입력예제 1
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0

▣ 출력예제 1
12
"""
import sys
from _collections import deque as dq
# sys.stdin = open("in1.txt", "rt")

d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]

board = []
for _ in range(7):
    board.append(list(map(int, input().split())))
check = [[0] * 7 for _ in range(7)]
check[0][0] = 1
answer = 0

start = [0, 0]
end = [6, 6]

queue = dq([start])

while queue:
    # print("\nlevel: ", answer)

    for j in range(len(queue)):
        src = queue.popleft()
        # print("src: ", src)
        if src == [6, 6]:
            print(answer)
            sys.exit(0)

        for i in range(4):
            new_row = src[0] + d_row[i]
            new_col = src[1] + d_col[i]

            if 0 <= new_row < 7 and 0 <= new_col < 7 and board[new_row][new_col] == 0 and check[new_row][new_col] == 0:
                # print("new_elem: ", (new_row, new_col))
                queue.append([new_row, new_col])
                check[new_row][new_col] = 1

    answer += 1

else:
    print(-1)