INF = 10001
node_num = int(input()) + 1
edge_num = int(input())

visited = [False] * node_num
distances = [INF] * node_num

adj_mat = [[INF for i in range(node_num)] for j in range(node_num)]
for i in range(node_num):
    for j in range(node_num):
        if i == j:
            adj_mat[i][j] = 0

for i in range(edge_num):
    edge = list(map(int, input().split()))
    print(edge)
    start = edge[0]
    dest = edge[1]
    weight = edge[2]

    adj_mat[start][dest] = weight
    adj_mat[dest][start] = weight

for i in adj_mat:
    print(i)

# 시작 노드는 1이라 가정하겠다.
start = 1

def get_min_node(num):
    print("get_min_node 진입")
    for i in range(1, num):
        if not visited[i]:
            v = i
            print("초안 v: ", v)
            break

    for i in range(1, num):
        if not visited[i] and distances[i] < distances[v]:
            v = i

    print("갱신된 v: ", v)
    print("get_min_node 종료")
    return v


def prim(start, node_num):
    distances[start] = 0
    print("\n------prim 시작------")
    for i in range(1, node_num):
        node = get_min_node(node_num)
        print("\nnode: ", node)
        visited[node] = True

        for j in range(1, node_num):
            if adj_mat[node][j] != INF:
                if not visited[j] and adj_mat[node][j] < distances[j]:
                    print("값 갱신하는 j: ", j)
                    distances[j] = adj_mat[node][j]
        print("distances: ", distances[1:])


start = 4
print("초기 distances: ", distances[1:])
prim(start, node_num)
print("\n최종 distances: ", distances[1:])
print(sum(distances[1:]))
