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
        dest = queue.pop(0)
        print("dest: ", dest)
        new_arr = []
        for j in range(len(adj_mat[dest])):
            if not visited[j] and adj_mat[dest][j] == 1:
                new_arr.append(j)
                visited[j] = True
                result.append(j)
        queue = new_arr

    for k in result:
        adj_mat[start][k] = 1

    print(start, "행: ", adj_mat[start])
    print("result: ", result)

print("\n결과")
for i in range(len(adj_mat)):
    print(*adj_mat[i])
