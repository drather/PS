def solution(n, edges):
    distances = [0] * (n)
    visited = [0] * (n)
    adj_list = dict()

    for i in range(1, n):
        adj_list[i] = []

    for i in range(len(edges)):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])

    distances[0] = -1
    print(distances)

    start = 1
    cands_queue = adj_list[start]
    visited[start] = 1

    while cands_queue:
        print("cand_queue: ", cands_queue)
        dest = cands_queue.pop(0)
        print("dest: ", dest)

        visited[dest] = 1
        distances[dest] += 1
        print("distance:", distances)
        print("visited: ", visited)
        for i in range(len(adj_list[dest])):
            if visited[adj_list[dest][i]] != 1:
                cands_queue.append(adj_list[dest][i])


    print("distances:", distances)


def solution2(n, edges):
    distances = [99] * (n+1)
    distances[1] = 0
    visited = [0] * (n+1)
    distances[0] = -99

    adj_mat = [[0 for col in range(n+1)] for row in range(n+1)]
    for i in range(len(edges)):
        adj_mat[edges[i][0]][edges[i][1]] = 1
        adj_mat[edges[i][1]][edges[i][0]] = 1

    for i in range(len(adj_mat)):
        print(adj_mat[i])

    start = 1
    queue = []
    visited[start] = 1

    for i in range(len(adj_mat)):
        if adj_mat[start][i] != 0:
            queue.append(i)
            distances[i] = 1

    print("시작노드 :", start)
    print("후보 노드들: ", queue)
    print("---반복 시작---\n")

    previous = start
    while queue:
        temp = queue.pop(0)
        print("\n방문한 노드: ", temp)
        print("이전 노드: ", previous)
        visited[temp] = 1

        distances[temp] = min(distances[temp], distances[previous] + adj_mat[previous][temp])
        print("distance["+str(temp)+"]: ", distances[temp])
        print("distance["+str(previous)+"] + ", "adj_mat[" +str(previous) + "]["+str(temp)+"]: ", distances[previous] + adj_mat[previous][temp])
        print("갱신한", temp, "의 distances값: ", distances[temp])

        for i in range(1, len(adj_mat)):
            if adj_mat[temp][i] != 0 and visited[i] == 0 and i not in queue:
                print("선택된 노드 인덱스: ", i)
                queue.append(i)
        print("다음 방문 후보 노드: ", queue)
        previous = temp

    print("visited: ", visited)
    print("distances: ", distances)

    return distances.count(max(distances))


def solution3(n, edges):
    import heapq as hq

    distances = [99] * (n+1)
    distances[1] = 0
    visited = [0] * (n+1)
    distances[0] = -99

    adj_mat = [[0 for col in range(n+1)] for row in range(n+1)]
    for i in range(len(edges)):
        adj_mat[edges[i][0]][edges[i][1]] = 1
        adj_mat[edges[i][1]][edges[i][0]] = 1

    for i in range(len(adj_mat)):
        print(adj_mat[i])

    start = 1
    visited[start] = 1
    queue = []
    for i in range(len(adj_mat)):
        if adj_mat[start][i] != 0:
            hq.heappush(queue, i)
            distances[i] = 1
            visited[i] = 1

    print("시작노드 :", start)
    print("후보 노드들: ", queue)
    print("---반복 시작---\n")

    previous = start

    while queue:
        temp = hq.heappop(queue)
        print("\n방문한 노드: ", temp)
        print("이전 노드: ", previous)
        visited[temp] = 1

        distances[temp] = min(distances[temp], distances[previous] + adj_mat[previous][temp])
        print("distance["+str(temp)+"]: ", distances[temp])
        print("distance["+str(previous)+"] + ", "adj_mat[" +str(previous) + "]["+str(temp)+"]: ", distances[previous] + adj_mat[previous][temp])
        print("갱신한", temp, "의 distances값: ", distances[temp])

        for i in range(1, len(adj_mat)):
            if adj_mat[temp][i] != 0 and visited[i] == 0 and i not in queue:
                print("선택된 노드 인덱스: ", i)
                hq.heappush(queue, i)
        print("다음 방문 후보 노드: ", queue)
        previous = temp
        print("한 단계 끝난 후 distasnces: ", distances)

    print("visited: ", visited)
    print("distances: ", distances)

    return distances.count(max(distances))

def sol(n, edges):
    import copy
    graph = {}
    dist = []
    visited = []
    large = 99

    for edge in edges:
        try:
            graph[edge[0]].append(edge[1])
        except:
            graph[edge[0]] = [edge[1]]

    for i in range(n + 1):
        if i == 0:
            dist.append(-99)
            visited.append(-1)
        elif i == 1:
            dist.append(0)
            visited.append(0)
        else:
            dist.append(large)
            visited.append(0)

    print("graph: ", graph)
    print("dist: ", dist)
    print("visited: ", visited)

    start = 0



    print("graph: ", graph)
    print("dist: ", dist)
    print("visited: ", visited)


def sol2(n, edges):
    import copy
    adj_mat = [[0 for col in range(n+1)] for row in range(n+1)]
    for i in range(len(edges)):
        adj_mat[edges[i][0]][edges[i][1]] = 1
        adj_mat[edges[i][1]][edges[i][0]] = 1

    dist = []
    visited = []
    for i in range(n + 1):
        if i == 0:
            dist.append(-99)
            visited.append(-1)
        elif i == 1:
            dist.append(0)
            visited.append(0)
        else:
            dist.append(999)
            visited.append(0)

    dist = [0] * (n+1)
    visited[0] = -1
    visited[1] = 1
    queue = [1]
    count = 1
    print("dist: ", dist)

    print("visited: ", visited)

    # while 0 in visited:
    while 0 in visited:
        print("\n")
        print("count: ", count)
        arr = []
        for i in range(len(queue)):
            start = queue[i]
            cands_node = adj_mat[start]

            print("start: ", start)
            print("cands_node: ", cands_node)
            for j in range(len(cands_node)):
                if cands_node[j] == 1 and visited[j] == 0:
                    print(j, "방문")
                    arr.append(j)
                    visited[j] = 1
                    if dist[j] == 0:
                        dist[j] += count
                    print("새로 만들어진 arr: ", arr)

            print("arr: ", arr)
        queue = arr
        count += 1

    print("dist: ", dist)
    print("visited: ", visited)

    return dist.count(max(dist))




def sol3(n, edges):
    import copy
    adj_mat = [[0 for col in range(n+1)] for row in range(n+1)]
    for i in range(len(edges)):
        adj_mat[edges[i][0]][edges[i][1]] = 1
        adj_mat[edges[i][1]][edges[i][0]] = 1


    dist = [0] * (n+1)
    dist[0] = -1
    dist[1] = -1
    queue = [1]
    count = 1
    print("dist: ", dist)

    # while 0 in visited:
    while 0 in dist:
        print("\n")
        print("count: ", count)
        arr = []
        for i in range(len(queue)):
            start = queue[i]
            cands_node = adj_mat[start]

            print("start: ", start)
            print("cands_node: ", cands_node)
            for j in range(len(cands_node)):
                if cands_node[j] == 1 and dist[j] == 0:
                    print(j, "방문")
                    arr.append(j)
                    dist[j] += count
                    print("새로 만들어진 arr: ", arr)

            print("arr: ", arr)
        queue = arr
        count += 1

    print("dist: ", dist)
    return dist.count(max(dist))


def sol4(n, edges):
    adj_list =[[] for i in range(n+1)]
    print("adj_list: ", adj_list)

    for i in range(len(edges)):
        if edges[i][1] not in adj_list[edges[i][0]]:
            adj_list[edges[i][0]].append(edges[i][1])
        if edges[i][0] not in adj_list[edges[i][1]]:
            adj_list[edges[i][1]].append(edges[i][0])

    print("adj_list: ", adj_list)

    dist = [0] * (n+1)
    dist[0] = -1
    dist[1] = -1

    start = 1
    queue = [start]
    count = 1

    print("dist: ", dist)
    print("queue: ", queue)

    # 모든 노드에 대해 bfs 할 것
    while 0 in dist:
        print("\ncount : ", count)
        next_arr = []

        # start노드에서 갈 수 있는 노드가 있다면, 그 노드들을 순회하면서
        for start in queue:
            # queue[i]는 start노드에서 갈 수 있는 노드들을 담아놓은 배열
            # queue는 [1]로 시작한다.
            print("\tqueue: ", queue)
            for cand in adj_list[start]:
                # adj_list[i]는 갈 수 있는 노드들을 담아놓은 배열
                print("\t\tadj_list[start]: ", adj_list[start])
                if dist[cand] == 0:
                    print("\t\t\tcand: ", cand)
                    dist[cand] += count
                    next_arr.append(cand)

        count += 1
        queue = next_arr
        print("next_arr: ", next_arr)
        print("dist: ", dist)

    return dist.count(max(dist))


def my_sol(n, edges):
    graph = [[] for i in range(n+1)]

    for i in range(len(edges)):
        if edges[i][1] not in graph[i]:
            graph[edges[i][0]].append(edges[i][1])

        if edges[i][0] not in graph[i]:
            graph[edges[i][1]].append(edges[i][0])

    print("Graph: ", graph, "\n")



    """
    이 위로는 데이터 준비 과정
    이 밑으로는 너비 우선 탐색을 통해 dist 배열에 값 채워넣는 과정
    """
    start = 1
    queue = [start]
    dist = [0] * (n+1)
    dist[0] = -1
    dist[start] = -1
    count = 1

    # 1번 노드와 다른 노드와의 거리에 대한 값을 갖는 dist 배열에 0이 없을 때까지 반복한다.
    # 이는 1과 연결된 모든 노드를 방문한다는 뜻이다.
    while 0 in dist:
        # new_arr 배열은 다음 단계에 탐색할 노드들을 저장하기 위한 배열이다.
        new_arr = []

        # queue에 담겨 있는 노드들마다 bfs를 한다. 즉, 시작 노드에서 갈 수 있는 노드들을 방문한다.
        # 처음 반복을 시작할 때는 [1]이므로, start는 1이다.
        print("시작하는 큐: ", queue)
        for start in queue:
            print("탐색을 시작하는 노드: ", start)

            # start에서 갈 수 있는 노드들을 탐색한다. start가 1인 경우, cand는 3, 2 이다.
            for cand in graph[start]:

                # dist[cand]는 1번 노드와의 거리를 나타낸다. 이 값이 0이라면, 아직 방문되지 않은 것이다.
                # 따라서, dist[cand]의 값을 count만큼 증가시키고, new_arr 배열에 append한다.
                if dist[cand] == 0:
                    print("bfs로 탐색한 노드: ", cand)
                    dist[cand] += count
                    new_arr.append(cand)
        print("새로 만들어진 큐: ", new_arr, "\n")
        count += 1
        queue = new_arr

    else:
        print("모든 노드 방문, 반복 종료")

    print("dist: ", dist, "\n")
    return dist.count(max(dist))


edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print("정답: ", my_sol(n, edges))