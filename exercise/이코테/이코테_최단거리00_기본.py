"""
문제:
주어진 인풋으로부터 아래와 같은 그래프 자료구조를 만든다.

노드 번호   연결된 노드, 가중치
0           []
1           [(2, 2), (3, 5), (4, 1)]
2           [(3, 3), (4, 2)]
3           [(2, 3), (6, 5)]
4           [(3, 3), (5, 1)]
5           [(3, 1), (6, 2)]
6           []

그리고, 1번 노드로부부터 다른 노드까지의 최단 거리를 출력한다. 정답은 다음과 같다.
index       1   2   3   4   5   6
distance    0   2   3   1   2   4
"""
node_num, link_num = map(int, input().split())
start_node = int(input())

INF = 1e9


def make_graph(num_of_node):
    """
    다음과 같은 형태의 그래프를 만든다.
        노드 번호   연결된 노드, 가중치
        0           []
        1           [(2, 2), (3, 5), (4, 1)]
        2           [(3, 3), (4, 2)]
        3           [(2, 3), (6, 5)]
        4           [(3, 3), (5, 1)]
        5           [(3, 1), (6, 2)]
        6           []
    :param num_of_node:
    :return:
    """
    g = [[] for _ in range(node_num+1)]

    for i in range(link_num):
        source, target, weight = map(int, input().split())

        g[source].append((target, weight))

    return g


def get_min_and_not_visited_node(d, v):
    global INF, node_num
    min_value = INF
    index = 0

    for node_idx in range(1, node_num+1):
        if d[node_idx] < min_value and not v[node_idx]:
            min_value = d[node_idx]
            index = node_idx

    return index


def dijkstra(d, v):

    for _ in range(node_num - 1):
        min_and_not_visited_node = get_min_and_not_visited_node(d, v)

        v[min_and_not_visited_node] = True

        for trg, wgt in graph[min_and_not_visited_node]:
            new_distance = d[min_and_not_visited_node] + wgt

            if new_distance < d[trg]:
                d[trg] = new_distance


if __name__ == '__main__':
    visited = [False] * (node_num+1)
    distances = [1e9] * (node_num+1)

    graph = make_graph(node_num)

    # 시작 노드 설정
    # 시작 노드 방문 표시 및 거리 0 으로 초기화
    visited[start_node] = True
    distances[start_node] = 0

    for j in graph[start_node]:
        target, weight = j[0], j[1]
        distances[target] = weight

    dijkstra(distances, visited)

    print(distances)
    print(visited)
