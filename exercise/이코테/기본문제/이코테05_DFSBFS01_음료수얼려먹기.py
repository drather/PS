col_num, row_num = map(int, input().split())

board = []
for _ in range(row_num):
    row = list(map(int, input()))
    board.append(row)

# col_num, row_num = 5, 4
# board = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
#
# print(board)

# 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

visited = [[0 for _ in range(col_num)] for _ in range(row_num)]
answer = 0


def dfs(row, col):
    global answer
    print(f"연쇄 방문, row, col: {row}, {col}")
    visited[row][col] = 1

    for i in range(4):
        new_row = row + d_row[i]
        new_col = col + d_col[i]

        if 0 <= new_row < row_num and\
                0 <= new_col < col_num and \
                not board[new_row][new_col] and \
                not visited[new_row][new_col]:

            dfs(new_row, new_col)


if __name__ == '__main__':
    for r in range(row_num):
        for c in range(col_num):
            if visited[r][c] == 0 and board[r][c] == 0:
                print(f"해당 지역 첫 방문 {r} {c}")
                dfs(r, c)
                answer += 1

    for v in visited:
        print(v)

    print(answer)
