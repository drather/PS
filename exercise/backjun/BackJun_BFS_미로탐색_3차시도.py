import queue
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

rows, cols = map(int, input().split())
print(rows, cols)
mat = []
for i in range(rows):
    temp = list(map(int, (input())))
    mat.append(temp)

for i in range(len(mat)):
    print(mat[i])

visited = [[False for col in range(cols)] for rows in range(rows)]


start = [0, 0]
queue = [start]
visited[start[0]][start[1]] = True
answer = 0
final = [rows-1, cols-1]
print("최종 목적지: ", final)

while not visited[rows-1][cols-1]:
    answer += 1
    temp = []
    while queue:
        dest = queue.pop(0)
        print("\nanswer: ", answer)
        print("Dest: ", dest)
        print("queue: ", queue)


        for i in range(4):
            new_row = dest[0] + dy[i]
            new_col = dest[1] + dx[i]

            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and mat[new_row][new_col] != 0:
                visited[new_row][new_col] = True
                temp.append([new_row, new_col])
                print("추가된 좌표: ", [new_row, new_col])

    print(answer, "번 만에 갈 수있는 노드들 ", temp)
    if [rows-1, cols-1] in temp:
        print("정답 발견, answer: ", answer)
        answer += 1
        break;
    else:
        queue = temp

print("answer: ", answer)
# for i in range(len(visited)):
# #     print(visited[i])