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
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

node_num, link_num = map(int, input().split())

start = int(input())

graph = [[] for i in range(node_num+1)]

distances = [INF] * (node_num+1)

for _ in range(link_num):
    src, trg, wrt = map(int, input().split())
    graph[src].append((trg, wrt))


def dijkstra(start):
    priority_queue = []

    heapq.heappush(priority_queue, (0, start))

    distances[start] = 0

    while priority_queue:
        weight, current_node_index = heapq.heappop(priority_queue)
        print(f"weight, current_node_index: {weight},  {current_node_index}")
        if distances[current_node_index] < weight:
            print("이미 처리된 노드")
            continue

        for adj_node_index, adj_weight in graph[current_node_index]:
            new_distance = distances[current_node_index] + adj_weight
            print(f"new_distance, 기존 distance: {new_distance}, {distances[adj_node_index]}")
            if new_distance < distances[adj_node_index]:
                distances[adj_node_index] = new_distance
                print("update")
                heapq.heappush(priority_queue, (new_distance, adj_node_index))

        print()
    else:
        print("heap 비어서 종료")


dijkstra(start)

for i in range(1, node_num+1):
    if distances[i] == INF:
        print("CANNOT GO")
    else:
        print(distances[i])

