"""
크루스칼 알고리즘

크루스킬 알고리즘을 통해 최소 신장 트리를 구한다.
다음 3가지의 메서드로 구성된다.

1. find
- 해당 노드의 부모 노드를 재귀 호출을 통해 찾아낸다.

2. union
- 두 가지 노드를 받아서, parent 를 설정한다.

3. main
- 간선들을 wgt 기준으로 정렬한다.
- wgt 가 가장 작은 간선부터 신장트리에 포함시킨다. ( answer += wgt 하면서 )
- 이 때, 사이클을 발생시키는 간선은 포함시키지 않는다. (if union(x1, n2): continue)
"""


import heapq


def find(p, x):
    if parents[x] != x:
        parents[x] = find(p, p[x])

    return parents[x]


def union(p, n1, n2):
    p1 = find(p, n1)
    p2 = find(p, n2)

    if p1 > p2:
        parents[p1] = p2
        return False

    elif p1 < p2:
        parents[p2] = p1
        return False

    else:
        return True


if __name__ == '__main__':
    city_cnt, link_cnt = map(int, input().split())
    parents = [i for i in range(city_cnt+1)]
    links = []
    total_cost = 0

    for _ in range(link_cnt):
        src, trg, wgt = map(int, input().split())
        heapq.heappush(links, (wgt, src, trg))

    for _ in range(link_cnt):
        wgt, src, trg = heapq.heappop(links)

        if union(parents, src, trg):
            continue

        total_cost += wgt

    print(total_cost)
