"""
사이클 판별 알고리즘
union, find 연산을 통해 링크들을 순회하면서, 그래프 안에 사이클이 있는 지를 판별한다.

1. find_parent 메서드 정의
- 부모 노드와 자기 자신이 같으면 해당 노드 리턴
- 그렇지 않다면, 부모를 업데이트하면서 재귀 호출

2. union 메서드 정의
- 두 노드의 부모를 보고, 두 집합을 함침
- 만약 두 부모가 같다면, 사이클 발생이므로, False 리턴

3. 간선들에 대해서 union 호출

"""

node_cnt, link_cnt = map(int, input().split())
parents = [i for i in range(node_cnt+1)]


def find_parent(prt, n):
    if parents[n] != n:
        parents[n] = find_parent(prt, parents[n])

    return parents[n]


def union(prt, n1, n2):
    p1 = find_parent(prt, n1)
    p2 = find_parent(prt, n2)

    if p1 == p2:
        return False

    elif p1 < p2:
        prt[p2] = p1
        return True

    elif p1 > p2:
        prt[p1] = p2
        return True


if __name__ == "__main__":
    for _ in range(link_cnt):
        node1, node2 = map(int, input().split())

        if not union(parents, node1, node2):
            print("it has a cycle")
            break

    else:
        print("it doesn't have a cycle")
