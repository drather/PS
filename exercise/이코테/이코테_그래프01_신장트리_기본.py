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
        print("cycle")
        return True


city_cnt, link_cnt = map(int, input().split())
parents = [i for i in range(city_cnt+1)]
links = []
total_cost = 0

for _ in range(link_cnt):
    src, trg, wgt = map(int, input().split())
    heapq.heappush(links, (wgt, src, trg))






for _ in range(link_cnt):
    wgt, src, trg = heapq.heappop(links)
    print(f"src, trg, wgt: {src}, {trg}, {wgt}")
    if union(parents, src, trg):
        continue

    else:
        total_cost += wgt

print(parents[1:])
print(total_cost)

print([find(parents, i) for i in parents[1:] ])
