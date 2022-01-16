"""
미로탐색(DFS)
7*7 격자판 미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요. 출발점은 격
자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 통로이다. 격
자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면

출발 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 도착

위의 지도에서 출발점에서 도착점까지 갈 수 있는 방법의 수는 8가지이다.

▣ 입력설명
7*7 격자판의 정보가 주어집니다.

▣ 출력설명
첫 번째 줄에 경로의 가지수를 출력한다.

▣ 입력예제 1
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0

▣ 출력예제 1
8
"""

import sys

from _collections import deque as dq


def dfs(v):
    global answer
    print("\n현재 위치: ", v)
    if v[0] == 6 and v[1] == 6:
        print("찾음, answer:", answer)
        answer += 1
        return

    else:
        for j in range(4):
            new_row = v[0] + d_row[j]
            new_col = v[1] + d_col[j]

            if 0 <= new_row < 7 and 0 <= new_col < 7 and check[new_row][new_col] == 0 and board[new_row][new_col] == 0:
                print("다음 위치: ", [new_row, new_col])
                target = [new_row, new_col]
                check[new_row][new_col] = 1
                dfs(target)
                check[new_row][new_col] = 0


if __name__ == "__main__":
    sys.stdin = open("in.txt", "rt")

    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    board = []
    for _ in range(7):
        board.append(list(map(int, input().split())))

    check = [[0] * 7 for i in range(7)]
    start = [0, 0]
    end = [6, 6]

    answer = 0

    check[0][0] = 1
    dfs(start)
    print(answer)




