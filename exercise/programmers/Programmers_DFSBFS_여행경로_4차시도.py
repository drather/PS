import copy


def dfs(graph, start, length, count, path):
    print("\n도착한 점: ", start)
    path.append(start)
    print("현재까지 path: ", path)
    print("length, count: ", length, count)

    if count == length:
        print("티켓도 모두 사용, true 리턴")
        return True
    try:
        graph[start]
    except:
        print("길이 없음, false 리턴")
        path.pop()
        return False

    for i in range(len(graph[start])):
        count += 1
        dest = graph[start][i]
        print("다음 갈 도시: ", dest)
        sub_graph = copy.deepcopy(graph)
        sub_graph[start] = sub_graph[start][:i] + sub_graph[start][i+1:]
        print("sub_graph[start]:", sub_graph[start])

        print("sub_graph: ", sub_graph)

        temp = dfs(sub_graph, dest, length, count, path)

        print("현재까지 사용한 ticket 수: ", count, "\n")
        print("함수안의 path: ", path)
        if temp:
            print("참이라 true 리턴")
            return True
        else:
            print("거짓임")
            count -= 1
    path.pop()
    print("거짓이라 false 리턴하고 pop")
    return False


def solution2(tickets):
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
    print("데이터 준비끝\n")

    start = "ICN"
    path = []
    count = 0
    cand_list = copy.deepcopy(graph[start])
    print("반복 시작")
    print("graph: ", graph)
    print("시작점: ", start)
    print("후보지 : ", cand_list)
    print("path: ", path)

    dfs(graph, start, len(tickets), count, path)
    print("path: ", path)
    return path


def travel(answer_set,answer,start,K,count):
    answer.append(start)
    if count==K:
        return True
    try:
        answer_set[start]
    except:
        answer.pop()
        return False
    for i in range(len(answer_set[start])):
        end=answer_set[start][i]
        count+=1
        temp_set=copy.deepcopy(answer_set)
        temp_set[start]=temp_set[start][:i]+temp_set[start][i+1:]
        boolean=travel(temp_set,answer,end,K,count)
        if boolean:
            return True
        else:
            count-=1
    answer.pop()
    return False




tickets1 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],["ATL","SFO"]]
tickets2 = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
print("1번답: ", solution2(tickets1))
# print("2번답: ", solution(tickets2))