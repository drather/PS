node_num = int(input())
adj_mat = []
for i in range(node_num):
    temp = list(map(int, input().split()))
    adj_mat.append(temp)


for i in range(node_num):
    visited = [False] * node_num
    start = i
    queue = [start]
    # visited[start] = True
    result = []

    print("\n---", start, "번 노드에서 탐색 시작---")

    while queue:
        print("\nqueue: ", queue)
        temp = queue.pop(0)
        print("temp: ", temp)
        for j in range(len(adj_mat[temp])):
            if not visited[j] and adj_mat[temp][j] == 1:
                queue.append(j)
                visited[j] = True
                result.append(j)

        for k in result:
            if adj_mat[start][k] == 0:
                adj_mat[start][k] = 1

    print("result: ", result)
    print(start, "행: ", adj_mat[start])

print("\n결과")
for i in range(len(adj_mat)):
    print(*adj_mat[i])

