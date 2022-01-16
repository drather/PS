node_num, link_num = map(int, input().split())
node_num += 1
graph = [[1001 for _ in range(node_num)] for __ in range(node_num)]
in_degrees = [0] * node_num
for i in range(1, len(graph)):
    for j in range(1, len(graph)):
        if i == j:
            graph[i][j] = 0

for i in range(link_num):
    start, dest, weight = map(int, input().split())
    graph[start][dest] = weight
    graph[dest][start] = weight
    in_degrees[start] += 1
    in_degrees[dest] += 1

visited = [False] * node_num
distances = [1001] * node_num

start = 5
distances[start] = 0

def get_min_node(node_num):
    for i in range(1, node_num):
        if not visited[i]:
            v = i
            break

    for i in range(1, node_num):
        if not visited[i] and distances[i] < distances[v]:
            v = i

    return v

def prim(graph, node_num):
    print("초기 distances: ", distances)
    print("초기 vistied: ", visited)
    for i in range(1, len(graph)):
        node = get_min_node(node_num)
        print("\nnode: ", node)
        visited[node] = True

        for j in range(1, node_num):
            if graph[node][j] != 1001:
                if not visited[j] and graph[node][j] <= distances[j]:
                    distances[j] = graph[node][j]
                    print("갱신된 j와 distance값: ", j, distances[j])

        print("distances: ", distances[1:])

    print("distances: ", distances[1:])
    print("최소 신장트리 비용: ", sum(distances[1:]))

    distances.sort()
    print("정렬된 distances: ", distances)

    for i in range(0, len(distances)-1):
        if in_degrees[i] != 1:
            distances[i] = 0
            break

    print()
    print("정답: ", sum(distances[:-2]))
    return sum(distances[:-2])


print(prim(graph, node_num))



