"""
주어진 그래프의 인접행렬을 통해서, 최소 신장 트리를 만들 것.
입력: 그래프의 인접 행렬
출력: 최소 신장 트리의 합
알고리즘은 Kruskal 알고리즘을 사용할 것
- 간선들을 오름차순으로 정렬
- k = 0
- 간선들의 count가 n-1이 될 때까지,
    k += 1
    if 현재까지의 간선들 + 앞으로 추가할 어느 한 간선이 사이클을 형성하지 않으면 -> 여기서 union-find 알고리즘 사용
        현재까지의 간선들 + 앞으로 추가할 어느 한 간선
- return 간선 집합

union-find 알고리즘이란?
- 두 집합의 합집합을 만든다. -> union(x, y)
- 한 원소가 어느 집합에 속하는지 알아낸다. -> find(x)
>> 사이클 검사에 이용한다.
"""
import heapq as hq

# union - find 프로그램
rank = {}
parent = {}


def make_set(node):
    parent[node] = node
    rank[node] = 0


def find_set(node):
    # print(node)

    if parent[node] != node:
        parent[node] = find_set(parent[node])

    return parent[node]


def union_set(node1, node2):
    root1 = find_set(node1)
    root2 = find_set(node2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(node_num, edges):
    for i in range(node_num):
        make_set(i)

    print(parent)
    print(rank)

    edges.sort(key=lambda x:x[2])
    mst = []

    for edge in edges:
        start, dest, weight = edge

        if find_set(start) != find_set(dest):
            union_set(start, dest)
            print(parent)
            mst.append(edge)

    sum_ = 0
    for i in mst:
        sum_ += i[2]

    return sum_


n = 4
cost = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]

print(kruskal(n, cost))
