"""
알리바바와 40인의 도둑(Bottom-Up)
알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다.
알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다.
계곡의 돌다리는 N×N개의 돌들로 구성되어 있다. 각 돌다리들은 높이가 서로 다릅니다.
해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 이동은 최단거리 이동을 합니다.
즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다.
N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의
최소량을 구하는 프로그램을 작성하세요.

만약 N=3이고, 계곡의 돌다리 격자 정보가 다음과 같다면
3 3 5
2 3 4
6 5 2
(1, 1)좌표에서 (3, 3)좌표까지 가는데 드는 최소 에너지는 3+2+3+4+2=14이다.

▣ 입력설명
첫 번째 줄에는 자연수 N(1<=N<=20)이 주어진다.
두 번째 줄부터 계곡의 N*N 격자의 돌다리 높이(10보다 작은 자연수) 정보가 주어진다.

▣ 출력설명
첫 번째 줄에 (1, 1)출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.

▣ 입력예제 1
5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4

▣ 출력예제 1
25
"""
import sys
import copy


# TOP-DOWN 방식 기반 풀이
def dfs(row, col):
    # print("\nrow, col: ", (row, col))
    if row == 0 and col == 0:
        return board[0][0]

    elif dp[row][col] > 0:
        return dp[row][col]

    elif row == 0:
        dp[row][col] = dfs(row, col-1) + board[row][col]

    elif col == 0:
        dp[row][col] = dfs(row-1, col) + board[row][col]

    else:
        dp[row][col] = min(dfs(row-1, col), dfs(row, col-1)) + board[row][col]

    return dp[row][col]


if __name__ == "__main__":
    # sys.stdin = open("in1.txt", "rt")
    length = int(input())

    board = []
    for _ in range(length):
        board.append(list(map(int, input().split())))

    dp = [[0] * length for _ in range(length)]

    dfs(length-1, length-1)
    print(dp[length-1][length-1])




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # BOTTOM-UP 방식 기반 풀이
# if __name__ == "__main__":
#     # sys.stdin = open("in1.txt", "rt")
#     MAX = 2147000
#     length = int(input())
#     board = [[MAX] * (length+1)]
#     for _ in range(length):
#         temp = list(map(int, input().split()))
#         temp.insert(0, MAX)
#         board.append(temp)
#
#     for i in range(1, length + 1):
#         for j in range(1, length + 1):
#             if i == 1 and j == 1:
#                 continue
#             else:
#                 board[i][j] = min(board[i-1][j], board[i][j-1]) + board[i][j]
#
#     print(board[length][length])