size = int(input())
adj_mat = []
for i in range(size):
    temp = list(map(int, (input())))
    adj_mat.append(temp)

visited = [[-1 for col in range(size)] for row in range(size)]

print("adj_mat: ", adj_mat)
print("visted: ", visited)


def dfs(adj_mat, x, y, house_num, visited):
    print("\n---호출된 함수 정보---")
    print("x: ", x)
    print("y: ", y)
    print("house_num: ", house_num)

    if x < 0 or y < 0 or x >= len(adj_mat) or y >= len(adj_mat):
        print("종료, 범위 벗어남")
        return house_num

    if adj_mat[x][y] == 0:
        print("종료, 집이 없는 곳")
        return house_num

    if visited[x][y] == 1:
        print("종료, 이미 방문한 곳")
        return house_num

    else:
        print("****집 있고 아직 방문 안된 곳****")
        visited[x][y] = 1
        house_num += 1
        a = dfs(adj_mat, x+1, y, house_num, visited)
        b = dfs(adj_mat, x, y+1, house_num, visited)
        c = dfs(adj_mat, x-1, y, house_num, visited)
        d = dfs(adj_mat, x, y-1, house_num, visited)
        print("밑, 오른, 위, 왼: ", [a, b, c, d])
        return max(a, b, c, d)


answer = []

for i in range(len(adj_mat)):
    for j in range(len(adj_mat[i])):
        if adj_mat[i][j] == 0:
            continue

        if adj_mat[i][j] == 1 and visited[i][j] != 1:
            print("\n-----" + str(i) + ", " + str(j) + "에서부터 dfs 시작-----")
            answer.append(dfs(adj_mat, i, j, 1, visited))
            print("answer: ", answer)


print("단지의 갯수: ", len(answer))
print(answer)

