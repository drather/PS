# col_num, row_num = map(int, input().split())
#
# board = []
# for _ in range(row_num):
#     row = list(map(int, input()))
#     board.append(row)

col_num, row_num = 5, 4
board = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

print(board)

# 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

visited = [[0 for _ in range(col_num)] for _ in range(row_num)]
stack = []
answer = 0


def dfs(row, col):
    global answer

    # 족
    if 0 <= row <= row_num and \
            0 <= col <= col_num and \
            not visited[row][col] and \
            not board[row][col]:
        dfs(row, col)
        return True

    return False


if __name__ == '__main__':
    for r in range(row_num):
        for c in range(col_num):
            if visited[r][c] == 0 and board[r][c] == 0:
                print(f"{r} {c} 해당 지역 첫 방문")
                visited[r][c] = 1

                for i in range(4):
                    new_row = r + d_row[i]
                    new_col = c + d_col[i]

                    dfs(new_row, new_col)

    for v in visited:
        print(v)

    print(answer)
