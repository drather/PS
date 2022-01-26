# row_num, col_num = map(int, input().split())
#
# board = [list(map(int, input())) for _ in range(row_num)]

row_num, col_num = 5, 6

board = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

visited = [[0] * col_num for _ in range(row_num)]
distance = [[1] * col_num for _ in range(row_num)]

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

if __name__ == '__main__':
    from _collections import deque

    answer = 0
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        r, c = queue.popleft()
        print(f"popped row, col: {r}, {c}")

        for i in range(4):
            new_row = r + d_row[i]
            new_col = c + d_col[i]

            if 0 <= new_row < row_num and \
                    0 <= new_col < col_num and \
                    visited[new_row][new_col] == 0 and \
                    board[new_row][new_col] != 0:

                # print(f"new row, col: {new_row}, {new_col}")
                queue.append((new_row, new_col))
                distance[new_row][new_col] = distance[r][c] + 1
                visited[new_row][new_col] = 1

        for q in queue:
            print(q, end=' ')
        print()

    for d in distance:
        print(d)

    print(distance[row_num-1][col_num-1])

