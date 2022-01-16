"""
아래의 코드는 효율성 문제 해결 위해서 우선순위 큐를 도입하다가 멈춘거.
크루스칼 알고리즘으로 풀 것
"""

import heapq as hq
import sys
node_num, link_num = map(int, input().split())
node_num += 1

edges = []
for i in range(link_num):
    start, dest, weight = map(int, sys.stdin.readline().split())
    hq.heappush(edges, [weight, start, dest])

rank = {}
parent = {}


def make_set(node):
    parent[node] = node
    rank[node] = 0


def find_set(node):
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

    mst = []
    answer = 0

    while len(mst) != node_num and edges:

        edge = hq.heappop(edges)
        weight, start, dest = edge

        if find_set(start) != find_set(dest):
            union_set(start, dest)
            mst.append(edge)
            answer += edge[0]

    print(mst)
    answer -= mst[-1][0]

    # print(answer)


kruskal(node_num, edges)








