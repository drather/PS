"""
플로이드 워셜 알고리즘을 이용한 최단거리 경로 구하기

문제를 살펴보면, 도시의 갯수, 간선의 갯수가 1 이상 100 이하이므로, 플로이드 워셜 알고리즘을 사용할 수 있다.
    - 그렇지 않은 경우, Heap 응용 다익스크라 알고리즘을 사용해야 한다.

1. 인풋 입력
2. 인접행렬 형태의 그래프 생성
3. 그래프 모든 원소 INF 로 초기화
4. 그래프의 대각 원소 0으로 초기화
5. k, i, j 3가지 인덱스를 이용해서 최단경로 테이블을 업데이트
    k: 1 ~ city_num -1 범위. 해당 노드를 거쳐서 가는 경우의 최단거리를 계산하기 위해 사용
    i: 출발하는 도시 번호. 인접행렬의 행 번호
    j: 도착하는 도시 번호. 인접행렬의 열 번호

    - k, i, j 모두 1 ~ city_num -1 만큼 반복한다.
    - k 는 현재 반복을 수행할 노드 번호를 의미한다.
    - graph[i][j] 는 현재 단계에서, 도시 i 에서 도시 j 로 이동하는 데 걸리는 최단 거리이다.
    - 현재 i 에서 j 로 이동하는 데 걸리는 최단 거리와, i 에서 k 를 거쳐 j 를 통해 갈 때 걸리는 최단 거리를 비교한다.
    - 이를 수식으로 나타내면, graph[i][j] 와 graph[i][k] + graph[k][j] 를 비교한다.
        - graph[i][k] 와 graph[k][j] 는 i -> k 로 가는 비용 + k -> j 로 가는 비용을 더한 값이다.
    - graph[i][j] 의 값이 graph[i][k] + graph[k][j] 의 값보다 작은 경우, 업데이트하지 않는다.
    - 반대의 경우, i 에서 j 로 이동할 때, 직접 가는 것 보다 k 를 거쳐서 가는 것이 더 짧으므로, graph[i][j] 를 업데이트한다.

6. 정답 행렬에서, 입력받은 graph[1][destination1] 과 graph[destination1][destination2] 를 더한 값을 출력한다.
    - 만약 해당 값이 INF 보다 같거나 크다면, -1 을 출력한다.

"""


city_num, link_num = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (city_num+1) for _ in range(city_num+1)]

for _ in range(link_num):
    src, trg = map(int, input().split())
    graph[src][trg] = 1
    graph[trg][src] = 1

for i in range(1, city_num+1):
    graph[i][i] = 0

for k in range(1, city_num+1):
    for i in range(1, city_num+1):
        for j in range(1, city_num+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

destination1, destination2 = map(int, input().split())

for i in range(1, city_num+1):
    for j in range(1, city_num+1):
        print(graph[i][j], end=' ')
    print()


answer = graph[1][destination1] + graph[destination1][destination2]

if answer >= INF:
    print(-1)
else:
    print(answer)
