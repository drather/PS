import queue


visited = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


case_num = int(input())
print("\ncase_num: ", case_num)
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
                    print("\n", m, n, "에서 BFS 시작")

                    my_que = queue.Queue()
                    my_que.put([m, n])
                    while not my_que.empty():
                        dest = my_que.get()
                        print("방문 노드: ", dest)
                        visited[dest[0]][dest[1]] = True

                        for i in range(4):
                            next_row = dest[0] + dy[i]
                            next_col = dest[1] + dx[i]

                            if 0 <= next_row < height and \
                                0 <= next_col < width and \
                                not visited[next_row][next_col] and \
                                mat[next_row][next_col] == 1:
                                my_que.put([next_row, next_col])
                                visited[next_row][next_col] = True

    print("답: ", count)