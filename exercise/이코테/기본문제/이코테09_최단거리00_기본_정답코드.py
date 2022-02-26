# 노드 수, 간선의 수 입력
node_num, link_num = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 그래프 생성
graph = [[] for i in range(node_num + 1)]

# 방문 여부 확인 배열 생성
visited = [False] * (node_num + 1)

# 무한대 값으로 distances 배열을 초기화
INF = 1e9
distances = [INF] * (node_num + 1)

# 링크를 읽어서, graph 에 초기화
for _ in range(link_num):
    source, target, weight = map(int, input().split())
    graph[source].append((target, weight))


def get_smallest_node():
    """
    graph 에서, 방문하지 않은 노드 중 가장 최단거리가 짧은 노드의 번호를 반환
    :return: index
    """

    min_value = INF
    index = 0

    # 1번부터 노드를 순회하면서, 최단거리가 가장 짧은 미방문 노드를 찾는다.
    for i in range(1, node_num + 1):
        if distances[i] < min_value and not visited[i]:
            min_value = distances[i]
            index = i

    # 찾아낸 노드의 인덱스를 리턴한다.
    return index


def dijkstra(start):
    # 시작 노드의 거리 0으로 초기화
    distances[start] = 0

    # 시작 노드 방문 처리
    visited[start] = True

    # 시작노드와 연결된 노드를 순회하면서, 거리 값을 초기화한다.
    # 즉, 1번 노드가 start 인경우를 예로 들면, distances  는 다음과 같이 초기화된다.
    # index       1   2   3   4   5     6
    # distance    0   2   5   1   INF   INF

    # graph[i]: list, [(i 번 노드와 연결된 노드 1, 가중치), (i 번 노드와 연결된 노드 2, 가중치), ... ]
    # graph[i][j] : i 번 노드와 연결된 간선 정보 중, j 번째 간선
    # graph[i][j][0]: target 노드
    # graph[i][j][1]: 가중치
    for j in graph[start]:
        distances[j[0]] = j[1]

    # 시작 노드를 제외한 n - 1 개의 노드에 대해 반복
    for i in range(node_num - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            # 거리 계산.
            # cost: 계산된 노드까지 계산된 거리 + 해당 노드로 가는 weight
            cost = distances[now] + j[1]

            # 새로운 cost 값이 기존에 계산된 distance 보다 작다면, 해당 값을 할당
            if cost < distances[j[0]]:
                distances[j[0]] = cost


if __name__ == '__main__':
    dijkstra(start)

    for i in range(1, node_num + 1):
        if distances[i] == INF:
            print("INF")
        else:
            print(distances[i])
