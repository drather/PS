from _collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

rows, cols = map(int, input().split())
mat = []
for i in range(rows):
    temp = list(map(int, (input())))
    mat.append(temp)

visited = [[False for col in range(cols)] for rows in range(rows)]

start = [0, 0]
my_que = deque([start])

visited[start[0]][start[1]] = True
answer = 0
final = [rows-1, cols-1]

while not visited[rows-1][cols-1]:
    answer += 1
    temp = []
    while my_que:
        dest = my_que.popleft()

        for i in range(4):
            new_row = dest[0] + dy[i]
            new_col = dest[1] + dx[i]

            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and mat[new_row][new_col] != 0:
                visited[new_row][new_col] = True
                temp.append([new_row, new_col])

    if [rows-1, cols-1] in temp:
        answer += 1
        break;
    else:
        my_que = deque(temp)

print(answer)