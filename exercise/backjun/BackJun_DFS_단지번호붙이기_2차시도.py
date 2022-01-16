size = int(input())
mat = []

for i in range(size):
    temp = list(map(int, (input())))
    mat.append(temp)

visited = [[False for col in range(size)] for row in range(size)]
print("adj_mat: ", mat)

"""
여기까지가 data 불러오는 부분
이 밑으로가 답
"""

def dfs(x, y, count):
    mat[x][y] = count
    visited[x][y] = True
    print(x, y, "방문")

    for _ in range(4):
        next_x = x + dx[i]
        next_x = y + dy[i]

        if 0 <= next_x < size and 0 <= next_x < size and mat[next_x][next_x] == 1 and not visited[next_x][next_x] :
            dfs(next_x, next_x, count)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = []
count = 1

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 0:
            continue

        if mat[i][j] == 1 and not visited[i][j]:
            print("---")
            num = 0
            dfs(i, j, count)
            count += 1

answer = []
for temp in range(1, count):
    num = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == temp:
                num += 1
    answer.append(num)
    temp += 1

answer.sort()
print(len(answer))

