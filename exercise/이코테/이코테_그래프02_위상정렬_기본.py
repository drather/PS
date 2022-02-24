"""
위상 정렬

다음과 같은 순서로 문제를 풀이한다.
0. 입력 받기 및 사용할 변수 선언
    - graph: 노드, 링크 정보 저장
    - in_degree: 노드별 진입 차수 저장
    - answer: pop 된 노드들을 순서대로 저장

1. 간선정보에 대해 입력 받으면서, target 의 진입 ㅏ수를 1씩 증가시킨다.

2. in_degree 가 0 인 노드들을 queue 에 담는다.

3. queue 에 원소가 존재하는 동안, 다음을 반복한다.
    - queue 에서 노드를 하나 pop 한다
    - answer 에 node 를 append 한다
    - pop 돤 노드의 인접 노드들의 진입 차수를 1씩 감소시킨다.
    - 만약, 진입차수가 1 감소된 노드의 진입차수가 0이 되었다면, queue 에 append 한다.

"""

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