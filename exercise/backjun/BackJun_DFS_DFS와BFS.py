nodes_num, edges_num, input_start = map(int, input().split())
edges = []

for i in range(edges_num):
    temp = input().split()
    edges.append([int(temp[0]), int(temp[1])])

print("edges: ", edges)

adj_mat = [[0 for col in range(nodes_num + 1)] for row in range(nodes_num + 1)]

for i in range(len(edges)):
    adj_mat[edges[i][0]][edges[i][1]] = 1
    adj_mat[edges[i][1]][edges[i][0]] = 1

print(adj_mat)

bfs_answer = []
dfs_answer = []

visited = [-1] * (nodes_num + 1)

queue = [input_start]
visited[input_start] = 1
bfs_answer.append(input_start)
while queue:
    print("queue: ", queue)
    temp = queue.pop(0)

    print("Temp: ", temp)

    for i in range(1, len(adj_mat[temp])):
        if visited[i] == -1 and adj_mat[temp][i] == 1:
            visited[i] = 1
            queue.append(i)
            bfs_answer.append(i)
            print(i, "방문")
            print("Visited:" , visited[1:])

print("\nDFS")
visited = [-1] * (nodes_num + 1)
stack = [input_start]
dfs_answer.append(input_start)

while stack:
    print("stack: ", stack)
    temp = stack.pop()
    visited[temp] = 1
    print("temp: ", temp)
    if temp not in dfs_answer:
        dfs_answer.append(temp)

    for i in range(len(adj_mat[temp])-1, 0, -1):
        if visited[i] == -1 and adj_mat[temp][i] == 1:
            stack.append(i)

print(dfs_answer)
print(bfs_answer)


