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
my_que = queue.Queue()
my_que.put(start)
visited[start[0]][start[1]] = True
answer = 0

while not my_que.empty():
    dest = my_que.get()
    print("answer: ", answer)
    print("\nDest: ", dest)

    if dest[0] == rows - 1 and dest[1] == cols:
        break

    for i in range(4):
        new_row = dest[0] + dy[i]
        new_col = dest[1] + dx[i]

        if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and mat[new_row][new_col] != 0:
            visited[new_row][new_col] = True
            my_que.put([new_row, new_col])
            answer += 1

print("answer: ", answer)