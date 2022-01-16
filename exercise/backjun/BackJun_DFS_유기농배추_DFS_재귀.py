"""
백준 1012 유기농 배추 문제를 DFS로 풀 것
1. 재귀 DFS
2. 반복 DFS
"""

import sys
sys.setrecursionlimit(100000)

visited = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# 1. 재귀 DFS 풀이
def dfs(row, col, count, width, height):
    global visited
    visited[row][col] = True
    # print("방문한 지점: ", row, col)
    for idx in range(4):
        next_row = row + dx[idx]
        next_col = col + dy[idx]
        if 0 <= next_row < height and 0 <= next_col < width \
                and not visited[next_row][next_col] \
                and mat[next_row][next_col] == 1:
            dfs(next_row, next_col, count, width, height)


case_num = int(input())
# print("case_num: ", case_num)
for i in range(case_num):
    # print("\n---------", i+1, "번 case 풀이---------")
    width, height, baechu_num = map(int, input().split())
    mat = [[0 for col in range(width)] for row in range(height)]
    visited = [[False for col in range(width)] for row in range(height)]
    count = 0
    # print("width, height, baechu_num: ", width, height, baechu_num)

    for j in range(baechu_num):
        col, row = map(int, input().split())
        mat[row][col] = 1

    for m in range(len(mat)):
        for n in range(len(mat[m])):
            if mat[m][n] == 0:
                continue
            else:
                if not visited[m][n]:
                    count += 1
                    # print("\n", m, n, "에서 dfs시작")
                    dfs(m, n, count, width, height)

    print(count)
