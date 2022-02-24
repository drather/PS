

from collections import deque


if __name__ == '__main__':
    node_cnt, link_cnt = map(int, input().split())
    graph = [[] * (node_cnt+1) for _ in range(node_cnt+1)]
    in_degree = [0] * (node_cnt+1)
    answer = []

    for _ in range(link_cnt):
        src, trg = map(int, input().split())
        graph[src].append(trg)

        in_degree[trg] += 1

    q = deque([i for i in range(1, node_cnt+1) if in_degree[i] == 0])

    while q:
        node = q.popleft()
        answer.append(node)

        for adj_node in graph[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                q.append(adj_node)

    print(answer)