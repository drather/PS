answer = []

"""
pop을 하면 안될거같다
visited를 대신할 무언가가 필요하다. 
"""

def dfs(graph, start, cands, path, num):
    global answer
    path.append(start)
    print("\n호출된 지점: ", start)
    print("지금까지 path: ", path)
    cands.sort()
    print("cand_stack: ", cands)

    while cands:
        dest = cands.pop(0)
        return dfs(graph, dest, cands, path, num)

    else:
        print("끝자리 도착, path: ", path)
        if len(path) == num:
            answer.append(path)
        else:
            print("잘못 찾은 경로")
            return dfs(graph, start, cands, path, num)


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
    cands = graph[start]

    dfs(graph, start, cands, path, num)
    print("answer: ", answer)
    print(graph)


def solution4(tickets):
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

    start = cities[0]
    cands = graph[cities[0]]
    i = 0
    path = [start]
    used = []
    print("시작노드: ", start, "  /  후보지: ", cands)

    for i in range(0, 12):
        print(i, "번쨰")
        while cands:
            i += 1
            previous = start
            dest = cands.pop()
            print("갈 곳: ", dest)
            path.append(dest)
            print("현재까지 path: ", path)
            cands = graph[dest]
            print("후보지: ", cands, "\n")

        if len(cands) == 0:
            print("끝자리 도착")
            # if len(path) == len(tickets)+1 and not path in answer:
            #
            # print("정답", path)
            answer.append(path)
            print("path: ", path)

    print("answer: ", answer)


def solution5(tickets):
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

    start = cities[0]
    path = [start]

    for i in range(0, 12):
        path = [start]
        cands = graph[start]

        print(i, "번째 반복")
        print("시작노드: ", start, "  /  후보지: ", cands)

        for j in range(len(cands)):
            i += 1
            previous = start
            dest = cands.pop()
            print("갈 곳: ", dest)
            path.append(dest)
            print("현재까지 path: ", path)
            cands = graph[dest]
            print("후보지: ", cands, "\n")

        if len(cands) == 0:
            print("끝자리 도착")
            if path not in answer:
                answer.append(path)
                print("path: ", path)

    print("answer: ", answer)




tickets1 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],["ATL","SFO"]]
tickets2 = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
print("1번답: ", solution3(tickets1))
# print("2번답: ", solution(tickets2))

