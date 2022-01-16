"""
단지 번호 붙이기(DFS, BFS)
그림1과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸
다.철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한
다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.

그림2는 그림1을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지
에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

0 1 1 0 1 0 0
0 1 1 0 1 0 1
1 1 1 0 1 0 1
0 0 0 0 1 1 1
0 1 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 0 0 0
[그림 1]

0 1 1 0 2 0 0
0 1 1 0 2 0 2
1 1 1 0 2 0 2
0 0 0 0 2 2 2
0 3 0 0 0 0 0
0 3 3 3 3 3 0
0 3 3 3 0 0 0
[그림 2]
▣ 입력설명
첫 번째줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력
되고 그 다음 N줄에는 각각 N개의 자료(0 혹은 1)가 입력된다

▣ 출력설명
첫 번째줄에는 총 단지수를 출력하시오. 그리고 각 단지내의 집의 수를 오름차순으로 정렬하
여 한줄에 하나씩 출력하시오

▣ 입력예제 1
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

▣ 출력예제 1
3
7
8
9
출처 : 한국정보올림피아드
"""
import sys
from _collections import deque as dq


def dfs(_r, _c):
    # print("\nr, c: ", (_r, _c))
    global cnt
    cnt += 1
    check[_r][_c] = 1

    for k in range(4):
        new_row = _r + d_row[k]
        new_col = _c + d_col[k]

        if 0 <= new_row < length and 0 <= new_col < length and board[new_row][new_col] != 0 and check[new_row][new_col] == 0:
            # print("\tnew_row, new_col: ", (new_row, new_col))
            # board[new_row][new_col] = _cnt
            # check[new_row][new_col] = 1
            dfs(new_row, new_col)


if __name__ == "__main__":
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    # sys.stdin = open("in1.txt", "rt")
    length = int(input())
    board = []
    for _ in range(length):
        board.append(list(map(int, input())))

    check = [[0] * length for _ in range(length)]
    result = []

    for i in range(length):
        for j in range(length):
            if board[i][j] != 0 and check[i][j] == 0:
                cnt = 0
                dfs(i, j)
                result.append(cnt)

    print(len(result))
    result.sort()
    for r in result:
        print(r)



# !!!!!!!!!!!!!!!!!! BFS 기반 풀이 !!!!!!!!!!!!!!!!!!
# if __name__ == "__main__":
#     d_row = [-1, 0, 1, 0]
#     d_col = [0, 1, 0, -1]
#
#     # sys.stdin = open("in1.txt", "rt")
#     length = int(input())
#     board = []
#     for _ in range(length):
#         board.append(list(map(int, input())))
#
#     check = [[0] * length for _ in range(length)]
#     table = {}
#
#     cnt = 0
#     for row in range(length):
#         for col in range(length):
#             if board[row][col] == 1 and check[row][col] == 0:
#                 check[row][col] = 1
#                 queue = dq([(row, col)])
#
#                 cnt += 1
#                 table[cnt] = 0
#                 # print("\ncount: ", cnt)
#
#                 while queue:
#                     q_size = len(queue)
#                     for _ in range(q_size):
#                         # print("\tqueue: ", queue)
#
#                         src = queue.popleft()
#                         table[cnt] += 1
#                         now_row, now_col = src[0], src[1]
#                         board[now_row][now_col] = cnt
#
#                         # print("\tsrc: ", src)
#                         for j in range(4):
#                             # print("\t\tj: ", j)
#                             new_row = now_row + d_row[j]
#                             new_col = now_col + d_col[j]
#                             # print("\t\tcand: ", (new_row, new_col))
#
#                             if 0 <= new_row < length and 0 <= new_col < length and check[new_row][new_col] == 0 and board[new_row][new_col] != 0:
#                                 # print("\t\tnew: ", (new_row, new_col))
#                                 queue.append((new_row, new_col))
#                                 check[new_row][new_col] = 1
#                                 # board[new_row][new_col] = count
#
#     print(cnt)
#     arr = list(table.values())
#     arr.sort()
#     for a in arr:
#         print(a)