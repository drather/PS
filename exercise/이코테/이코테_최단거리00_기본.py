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
        src, trg, wgt = map(int, input().split())

        g[src].append((trg, wgt))

    return g


def get_min_and_not_visited_node(d, v):
    """
    다익스트라 알고리즘 실행 과정 중, 현재 distances 배열에서 최단 거리가 가장 작은 노드를 찾아 리턴하는 메서드.
    선형 탐색을 활용하는 경우, 이 메서드의 시간복잡도는 O(V) 이다.
    이 메서드는 Greedy 알고리즘을 근거로 한다.

    :param d: 최단거리 테이블을 나타내는 배열을 의미.
    :param v: 노드들의 방문 여부를 나타내는 배열 의미.
    :return: 현재 distances 배열에서, 가장 그 값이 작은 노드의 인덱스
    """
    global INF, node_num
    min_value = INF
    index = 0

    for node_idx in range(1, node_num+1):
        # 아직 미방문 상태이며, 최단거리 값이 가장 작은 원소를 선형 탐색.
        if d[node_idx] < min_value and not v[node_idx]:
            min_value = d[node_idx]
            index = node_idx

    return index


def dijkstra(d, v):
    """
    파라미터로 받은 distances, visited 배열을 에 값을 업데이트함으로써, 최단경로를 구하는 핵심 메서드.
    동적계획법을 사용한다.
    (노드 갯수 - 1) 번 반복하며, 다음 동작을 수행한다.
        - 아직 미방문 상태이며, 현재 distances 배열에서 그 값이 가장 작은 노드의 인덱스를 찾아낸다.
        - 찾아낸 노드 min_and_not_visited_node 와 인접한 노드 graph[min_and_not_visited_node] 를 이용해 distance 배열을 update.
            * graph[min_and_not_visited_node] 는 list 형태로, 각 원소는 (target, weight) 형태이다.
            - min_and_not_visited_node 와 인접한 노드에 distance 값을 업데이트 시키기 위해선 다음 값이 필요하다.
                1. distance[target]: 현재까지 계산된 인접노드까지의 최단 경로 길이
                2. new_distance: min_and_not_visited_node 까지의 거리 + min_and_not_visited_node 에서 인접노드로 가는 길이
            - 이 두 가지를 비교해서, new_distance 가 distance[target] 보다 작다면, 최단 경로를 업데이트한다.

    :param d: 최단거리 테이블.
    :param v: 방문 여부 배열.
    :return:
    """
    # 노드의 갯수 - 1 (시작정점 제외) 만큼 반복 수행
    for _ in range(node_num - 1):
        # 최단거리가 가장 짧으며 아직 미방문 노드
        min_and_not_visited_node = get_min_and_not_visited_node(d, v)
        v[min_and_not_visited_node] = True

        # 동적 계획법
        # graph[min_and_not_visited_node] 는 min_and_not_visited_node 의 인접 노드들을 의미한다.
        for trg, wgt in graph[min_and_not_visited_node]:
            # 새로운 최단 경로 후보
            new_distance = d[min_and_not_visited_node] + wgt

            # 새로운 최단 경로의 길이가 기존 최단 경로의 길이보다 작다면, update
            if new_distance < d[trg]:
                d[trg] = new_distance


def init_dijkstra(distance_array, visited_array, start):
    """
    파라미터로 받은 distances, visited 를 초기화한다.
    또한 start 파라미터를 통해, distance 배열의 시작 노드의 인접노드 인덱스의 값을 weight 로 업데이트 한다.
    :param distance_array:
    :param visited_array:
    :param start:
    :return:
    """

    visited_array[start] = True
    distance_array[start] = 0
    for j in graph[start]:
        target, weight = j[0], j[1]
        distance_array[target] = weight


if __name__ == '__main__':
    node_num, link_num = map(int, input().split())
    start_node = int(input())

    INF = 1e9

    # 방문 여부 확인 배열 생성
    visited = [False] * (node_num+1)

    # 최단거리 테이블 설정.
    # 배열의 각 인덱스가 가리키는 값은 start_node 로부터 해당 노드까지의 최단 거리를 의미
    # 무한대로 값 초기화
    distances = [1e9] * (node_num+1)

    # 인풋파일을 읽어 그래프 생성
    graph = make_graph(node_num)

    # 다익스트라 알고리즘을 활용하기 위한 세팅
    init_dijkstra(distances, visited, start_node)

    # 다익스트라 알고리즘 수행
    dijkstra(distances, visited)

    # 정답 출력
    print(distances)
    print(visited)
