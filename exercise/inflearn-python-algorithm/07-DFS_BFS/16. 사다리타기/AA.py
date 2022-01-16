"""
사다리 타기(DFS)
현수와 친구들은 과자를 사먹기 위해 사다리 타기를 합니다. 사다리 표현은 2차원 평면은 0으
로 채워지고, 사다리는 1로 표현합니다. 현수는 특정도착지점으로 도착하기 위해서는 몇 번째
열에서 출발해야 하는지 알고싶습니다. 특정 도착지점은 2로 표기됩니다. 여러분이 도와주세
요. 사다리의 지도가 10*10이면

0 1 2 3 4 5 6 7 8 9

1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1

특정목적지인 2에 도착하려면 7번 열 출발지에서 출발하면 됩니다.
▣ 입력설명
10*10의 사다리 지도가 주어집니다.

▣ 출력설명
출발지 열 번호를 출력하세요.

▣ 입력예제 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1

▣ 출력예제 1
7
"""
import sys


def dfs(row, col):
    global answer
    # print("\n현재 위치: ", (row, col))
    if row < 0 or row >= length:
        # print("row 인덱스 초과")
        return
    if col < 0 or col >= length:
        # print("row 인덱스 초과")
        return
    if board[row][col] == 0:
        # print("길 없음")
        return

    if row == 0:
        answer = col
        print(answer)
        sys.exit(0)

    else:
        # print("\n현재 위치: ", (row, col))

        for k in range(3):
            new_row = row + d_idx[k][0]
            new_col = col + d_idx[k][1]

            if 0 <= new_row < length and 0 <= new_col < length and check[new_row][new_col] == 0:
                check[new_row][new_col] = 1
                dfs(new_row, new_col)
                check[new_row][new_col] = 0



if __name__ == "__main__":
    # sys.stdin = open("in5.txt", "rt")

    d_idx = [(0, -1), (0, 1), (-1, 0)]

    answer = -10
    length = 10
    board = []

    for _ in range(length):
        board.append(list(map(int, input().split())))
    check = [[0] * 10 for _ in range(10)]

    for i in range(length):
        if board[length-1][i] == 2:
            check[length-1][i] = 1
            dfs(length-1, i)


