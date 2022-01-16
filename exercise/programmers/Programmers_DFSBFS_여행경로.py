# cities를 정렬된 채로 저장한다. 그래야 bfs할때 괜춘
# dfs할때는, 이름을 역순으로 정렬하고 dfs하는것도 좋을듯
# 아니면 pop을 0번째껄 하던가
# 여기서는, 그냥 딕셔너리(bfs)로 풀어볼란다

# 정정, 경로를 구해야 한다. 따라서, dfs로 푼다.

def bfs_solution(tickets):
    pass

def dfs_iterative_solution(tickets):
    import heapq as hq
    cities = []
    graph = dict()
    for i in range(len(tickets)):
        for j in range(len(tickets[i])):
            if tickets[i][j] not in cities:
                cities.append(tickets[i][j])
    print("cities: ", cities)

    for i in range(len(cities)):
        graph[cities[i]] = []
        for j in range(len(tickets)):
            if cities[i] == tickets[j][0]:
                hq.heappush(graph[cities[i]], tickets[j][1])
    print("graph: ", graph)
    print("---데이터 준비 끝---\n")

    while True:
        path = ["ICN"]
        cand_stack = graph["ICN"]
        print("Cand: ", cand_stack)
        count = len(tickets)

        while cand_stack and count > 0:
            print(count)
            dest = hq.heappop(cand_stack)
            cand_stack.append(dest)
            print("dest: ", dest)
            cand_stack = graph[dest]
            print("cand:", cand_stack)
            count -= 1

        print("path: ", path)
        print("graph:", graph)
        if len(path) == len(tickets)+1:
            print("진정답 발견")
            return path
        else:
            print("정답 아님")

    return path


def dfs_iterative_solution2(tickets):
    import heapq as hq
    cities = []
    graph = dict()
    for i in range(len(tickets)):
        for j in range(len(tickets[i])):
            if tickets[i][j] not in cities:
                cities.append(tickets[i][j])
    print("cities: ", cities)

    for i in range(len(cities)):
        graph[cities[i]] = []
        for j in range(len(tickets)):
            if cities[i] == tickets[j][0]:
                graph[cities[i]].append(tickets[j][1])
                graph[cities[i]].sort()
    print("graph: ", graph)
    print("---데이터 준비 끝---\n")


    answer = []
    k = 0
    print("전체 시작")
    print("큰 반복문 시작")
    copied_graph = graph.copy()
    path = [cities[0]]
    start = cities[0]
    cands_stack = copied_graph[start]
    count = 0
    visited = []

    print("path: ", path, "  /  start:", start, "  /  후보지: ", cands_stack)

    while cands_stack:
        print("작은 반복문 시작")
        dest = cands_stack.pop()
        print("방문 지점: ", dest)
        path.append(dest)
        cands_stack = graph[dest].copy()
        print("다음 방문 후보: ", cands_stack)
        if len(cands_stack) == 0:
            answer.append(path)

        k += 1

    print("path: ", path)
    print("answer: ", answer)
    return answer[0]




def dfs(tickets, previous_ticket, path, i):
    pass


def dfs_recursive_solution(tickets):
    pass


def test():
    a = dict()

    a[1] = [1,2,3]
    temp = a[1].copy()

    temp.append(55)
    print(a)


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]

print("정답: ", dfs_iterative_solution2(tickets))
