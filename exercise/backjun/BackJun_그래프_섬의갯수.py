dy = [-1, -1, -1, 1, 1, 1, 0, 0]                # 행 움직임
dx = [-1, 0, 1, -1, 0, 1, -1, 1]                    # 열 움직임

answers = []

while True:
    size = list(map(int, input().split()))
    rows = size[1]
    cols = size[0]
    print("\n\nrows, cols: ", rows, cols)
    if rows == 0 and cols == 0:
        break

    mat = []
    for i in range(rows):
        temp = (list(map(int, input().split())))
        mat.append(temp)
    """
    여기까지가 데이터 불러오는 부분
    이 아래가 각각의 케이스 해결하는 부분
    """
    answer = 0
    visited = [[False for m in range(cols)] for n in range(rows)]

    print("-----풀이-----")
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("i, j: ", i, j)
            if mat[i][j] == 0:
                continue
            else:
                if not visited[i][j]:
                    print("\n", i, j, "에서 bfs 시작")
                    start = [i, j]
                    queue = [start]
                    visited[start[0]][start[1]] = True
                    answer += 1
                    temp = []
                    while queue:
                        print("queue: ", queue)
                        dest = queue.pop(0)
                        print("방문: ", dest)

                        for q in range(8):
                            next_row = dest[0] + dy[q]
                            next_col = dest[1] + dx[q]
                            # print("next: ", next_row, next_col)
                            if 0 <= next_row < rows \
                                    and 0 <= next_col < cols \
                                    and not visited[next_row][next_col] \
                                    and mat[next_row][next_col] == 1:
                                queue.append([next_row, next_col])
                                visited[next_row][next_col] = True

    print("answer: ", answer)
    print("---visited---")
    for q in visited:
        print(q)
    answers.append(answer)

print(answers)