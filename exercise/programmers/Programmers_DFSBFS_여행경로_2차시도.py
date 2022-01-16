def solution(tickets):
    answer = []
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

    k = 0
    while k < 10:
        k += 1
        start = cities[0]
        path = [start]
        cands_stack = graph[start]

        print("반복 시작\n시작지점: ", start, "  /  후보지:" , cands_stack)
        while cands_stack:
            dest = cands_stack.pop()
            path.append(dest)
            cands_stack = graph[dest]
            print("방문한 노드: ", dest, "  /  후보지: ", cands_stack)
        print("만들어진 경로: ", path)
        if len(path) == len(tickets):
            answer.append(path)
        else:
            continue;

    print("answer : ", answer)
    print("Graph: ", graph)


def solution2(tickets):
    cities = []
    for i in range(len(tickets)):
        for j in range(len(tickets[i])):
            if [tickets[i][j], 0] not in cities:
                cities.append([tickets[i][j], 0])

    for i in range(len(cities)):
        for j in range(len(tickets)):
            if cities[i][0] == tickets[j][1]:
                cities[i][1] += 1

    print("cities: ", cities)

    path = []

    start = tickets[0][0]
    cand_stack = [cities[0]]
    for i in range(len(tickets)):
        if start == tickets[i][0]:
            cand_stack.append(tickets[i][1])
    print("반복 시작\n시작지점: ", start, "  /  후보지:", cand_stack)

    while cand_stack:
        dest = cand_stack.pop()
        if tickets[i][0] == dest:
            cand_stack.append(tickets[i][0])
            print("stack: ", cand_stack)
        if not cand_stack:
            break;






answer = []

def dfs(graph, start, path, num):
    global answer
    path.append(start)
    print("\nstart: ", start)
    print("지금까지 path: ", path)
    cand_stack = graph[start].copy()
    cand_stack.sort()
    print("cand_stack: ", cand_stack)

    if len(path) > num:
        return

    while cand_stack:
        dest = cand_stack.pop(0)
        return dfs(graph, dest, path, num)

    else:
        print("끝자리 도착, path: ", path)
        if len(path) == num:
            answer.append(path)
        else:
            print("잘못 찾은 경로")
            path.pop(0)



def solution3(tickets):
    global answer
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

    path = []
    num = len(tickets) + 1

    start = cities[0]
    dfs(graph, start, path, num)
    print("answer: ", answer)
    print(graph)



tickets1 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets2 = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
print("1번답: ", solution3(tickets2))
# print("2번답: ", solution(tickets2))
