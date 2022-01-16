"""
등산경로(DFS)
등산을 매우 좋아하는 철수는 마을에 있는 뒷산에 등산경로를 만들 계획을 세우고 있습니다.
마을 뒷산의 형태를 나타낸 지도는 N*N 구역으로 나뉘어져 있으며, 각 구역에는 높이가 함께
나타나 있습니다.
N=5이면 아래와 같이 표현됩니다.

2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100

어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은
구역으로만 이동할 수 있도록 등산로를 설계하려고 합니다. 등산로의 출발지는 전체 영역에서
가장 낮은 곳이고, 목적지는 가장 높은 곳입니다. 출발지와 목적지는 유일합니다.

지도가 주어지면 출발지에서 도착지로 갈 수 있는 등산 경로가 몇 가지 인지 구하는 프로그
램을 작성하세요.

▣ 입력설명
첫 번째 줄에 N(5<=N<=13)주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.

▣ 출력설명
등산경로의 가지수를 출력한다.

▣ 입력예제 1
5
2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100

▣ 출력예제 1
5

"""
import sys
sys.stdin = open("in1.txt", "rt")


def dfs(row, col):
    global answer

    if row == end[0] and col == end[1]:
        # print("찾음")
        answer += 1

    else:
        for x in range(4):
            new_row = row + d_row[x]
            new_col = col + d_col[x]

            if 0 <= new_row < length and 0 <= new_col < length and mtns[row][col] < mtns[new_row][new_col]:
                check[new_row][new_col] = 1
                dfs(new_row, new_col)
                check[new_row][new_col] = 0


if __name__ == "__main__":
    answer = 0
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    length = int(input())

    mtns = []
    for _ in range(length):
        mtns.append(list(map(int, input().split())))

    end = (0, 0)
    max_h = -1
    start = (0, 0)
    min_h = 2147000

    for i in range(length):
        for j in range(length):
            if mtns[i][j] > max_h:
                max_h = mtns[i][j]
                end = (i, j)
            if mtns[i][j] < min_h:
                min_h = mtns[i][j]
                start = (i, j)

    check = [[0] * length for _ in range(length)]

    dfs(start[0], start[1])
    print(answer)



