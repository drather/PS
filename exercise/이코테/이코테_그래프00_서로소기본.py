"""
1. parents 배열 생성 및 초기화

2. find 연산 정의
    - 부모 테이블의 값과 인덱스가 같을 때까지 재귀 호출
    - 같으면 해당 인덱스 리턴

3. union 연산 정의
두 노드 a, b 에 대해 다음 동작 정의
    - a의 부모 재귀호출 (find a)
    - b의 부모 재귀호출 (find b)
    - a의 부모, b 의 부모 중 더 큰 놈이 더 작은 놈을 부모로 모시게 함. (parents[larger] = smaller)

4.  link 를 바탕으로 모든 원소에 대해 union 연산을 진행

5. parent 출력 -> 각 원소의 root 들을 알 수 있음

"""


node_num, link_num = map(int, input().split())
parents = [i for i in range(node_num+1)]


def find_parent(parents, x):
    print(f"find_parents: 부모, 자식: {parents[x], x}")
    if parents[x] != x:
        return find_parent(parents, parents[x])

    return x


def union(n1, n2):
    print(f"union: 노드1, 노드2: {n1, n2}")
    parent_node1 = find_parent(parents, n1)
    parent_node2 = find_parent(parents, n2)

    print(f"union: 노드1 부모, 노드2 부모: {parent_node1, parent_node2}")

    if parent_node1 > parent_node2:
        parents[node1] = parent_node2
        print(f"union: {node1}의 새로운 부모: {parents[node1]}")
    else:
        parents[node2] = parent_node1
        print(f"union: {parent_node2}의 새로운 부모: {parent_node1}")

    print(f"union: parents: {parents[1:]}")


if __name__ == '__main__':
    for _ in range(link_num):
        node1, node2 = map(int, input().split())

        union(node1, node2)
        print()

    print(parents[1:])

    for i in range(1, node_num+1):
        print(find_parent(parents, i), end=' ')

