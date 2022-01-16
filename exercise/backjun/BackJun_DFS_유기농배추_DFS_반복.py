visited = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


case_num = int(input())
print("case_num: ", case_num)
for i in range(case_num):
    print("\n---------", i+1, "번 case 풀이---------")
    width, height, baechu_num = map(int, input().split())
    mat = [[0 for col in range(width)] for row in range(height)]
    visited = [[False for col in range(width)] for row in range(height)]
    count = 0
    print("width, height, baechu_num: ", width, height, baechu_num)

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
                    print("\n", m, n, "에서 dfs시작")

                    stack = [[m, n]]
                    while stack:
                        dest = stack.pop(0)
                        print("dest: ", dest)
                        visited[dest[0]][dest[1]] = True

                        for i in range(4):
                            next_row = dest[0] + dx[i]
                            next_col = dest[1] + dy[i]

                            if 0 <= next_row < height and \
                                0 <= next_col < width and \
                                not visited[next_row][next_col] and \
                                mat[next_row][next_col] == 1:
                                stack.append([next_row, next_col])

    print(count)
