import copy


def dfs(graph, start, path, length, count):
    print("\n", "---호출된 함수 정보---")
    print("DFS(",start, ")")
    path.append(start)
    print("현재까지의 path: ", path)
    print("length, count: ", length, count)

    # 티켓을 모두 사용했다면, True를 리턴한다.
    if count == length:
        print("티켓 다씀")
        return True

    try:
        # 넘겨받은 start 노드에서 갈 수 있는 다른 도시가 있는 지를 확인한다.
        graph[start]
    except:
        # 티켓을 모두 사용하지 않았는데 다른 도시로 갈 수 없다면,
        # 잘못된 경로로 들어온 것이므로 path의 마지막 원소를 pop하고 False를 리턴한다.
        print("잘못된 길로 들어옴")
        path.pop()
        return False

    # 위에 두 조건문은 재귀 호출의 정지 조건
    # 아래는, 재귀 호출하면서 할 것 정의

    # start에서 갈 수 있는 노드들을 순회한다.
    for i in range(len(graph[start])):
        dest = graph[start][i]
        print("dest: ", dest)
        count += 1

        # sub_graph 는 이미 사용한 티켓을 고려해서, 다음 후보지를 담고 있는 딕셔너리이다.
        # 이 문제 풀이의 핵심인 부분이다. 그냥 DFS만 하면, 이미 방문한 ICN 과 ATL을 계속 왕복하다 끝난다.
        # 다른 문제의 VISITED 배열과 비슷한 개념이라 생각

        # copy모듈의 deepcopy를 통해 graph를 복사한다.
        # 그냥 = 연산자를 통해 할당할 경우, sub_graph를 조작하면 graph에 영향을 미친다.
        # sub_graph = graph를 할 경우, sub_graph는 graph의 값을 갖는 것이 아니라 graph에 대한 참조를 갖기 때문

        # sub_graph[start]에는, start 노드에서 갈 수 있는 다른 노드를 담은 배열인 sub_graph[start]에서,
        # i로 선택된 노드(첫 번째 경우, ICN -> ATL이 선택되므로, ATL 노드를 말함)를 뺀 나머지를 할당한 채로 재귀호출을 한다.
        # 즉, 한번 사용한 티켓은 빼는 것.
        # [sub_graph[start]의 1번째, 2번째, ..., i-1번째 원소]  + [sub_graph[start]의 i+1번째 원소, ..., 마지막 원소]
        # sub_graph[start]가 위와 같이 바뀌어서 DFS의 파라미터로 전달된다.
        # 어떻게 바뀌는지는 콘솔창 결과 확인할 것
        sub_graph = copy.deepcopy(graph)
        sub_graph[start] = sub_graph[start][:i] + sub_graph[start][i+1:]
        print("graph[start]: ", graph[start])
        print("sub_graph[start]: ", sub_graph[start])

        # 다음 갈 수 있는 노드에 대해서 재귀 호출을 했을 때, 그 결과를 받아온다.
        # 티켓을 모두 사용했으면 True가 리턴되어 dfs_result에 저장될 것이고,
        # 잘못된 경로로 들어왔다면 False가 리턴되어 dfs_result에 저장될 것이다.
        dfs_result = dfs(sub_graph, dest, path, length, count)

        # dfs의 결과가 True라면, 그것이 정답이므로 path를 리턴한다.
        if dfs_result:
            return path

        # dfs의 결과가 False라면, 잘못된 경로로 들어온 것이므로, count를 1 감소시킨다.
        else:
            count -= 1

    # 그리고, path의 마지막 원소를 pop한다.
    popped_city = path.pop()
    print("잘못된 경로로 들어옴")
    print("pop되는 원소: ", popped_city)
    print("path: ", path, "\n")

    # return 함으로써 자신을 호출한 함수에 결과를 리턴한다.
    return


def solution(tickets):
    answer = []
    cities = []
    graph = {}

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
    length = len(tickets)
    count = 0

    print("---DFS 재귀호출 시작---")
    answer = dfs(graph, start, path, length, count)
    return answer


tickets1 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],["ATL","SFO"]]
tickets2 = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
print("1번답: ", solution(tickets1), "\n\n\n")
print("\n\n2번답: ", solution(tickets2))
