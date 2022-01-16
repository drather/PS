"""
시간 초과 뜬다.
프림 알고리즘보다는 Kruskal 알고리즘이 더 좋을듯.
    구현하기도 간단할 거같다.
    글구 시간복잡도가 낮을 듯

"""

node_num, link_num = map(int, input().split())
node_num += 1

in_degrees = [0] * node_num
visited = [False] * node_num
distances = [1001] * node_num

adj_list = {}
for i in range(1, node_num):
    adj_list[i] = []

for i in range(link_num):
    start, dest, weight = map(int, input().split())
    adj_list[start].append([dest, weight])
    adj_list[dest].append([start, weight])

print("adj: ", adj_list)

start = 2
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


def prim(adj_list, node_num):
    print("초기 distances: ", distances)
    print("초기 vistied: ", visited)

    for i in range(1, node_num):
        node = get_min_node(node_num)
        print("\nnode: ", node)
        visited[node] = True

        for j in adj_list[node]:
            if not visited[j[0]] and j[1] < distances[j[0]]:
                distances[j[0]] = j[1]
                print("갱신된 j와 distance 값: ", j[0], j[1])

        print("반복문 내부 distances: ", distances[1:])

    print("결과 distances: ", distances[1:])

    # distances.sort(reverse=True)
    # print("정렬된 distances: ", distances)
    #
    # for i in range(1, len(distances)):
    #     print("i: ", i)
    #     if len(adj_list[i]) >= 1:
    #         distances[i] = 0
    #         break

    print("정답: ", sum(distances[1:]) - max(distances[1:]))
    return sum(distances[1:]) - max(distances[1:])


print(prim(adj_list, node_num))