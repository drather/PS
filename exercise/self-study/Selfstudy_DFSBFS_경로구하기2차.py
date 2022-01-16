
import copy

# 반복적 DFS
def dfs_iterative(graph, input_start):
    answer = []

    start = input_start
    stack = [start]
    path = []
    visited = [False] * len(graph)

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if i == j:
                graph[i][j] = 0
    count = 0
    while stack:
        count += 1
        print("\ncount : ", count)
        print("stack: ", stack)
        start = stack.pop()
        print(start, "방문")
        visited[start] = True
        path.append(start)
        print("path: ", path)

        cands = []
        for i in range(len(graph[start])-1,-1, -1):
            if not visited[i] and graph[start][i] == 1:
                cands.append(i)

        print("인접한 노드: ", cands)
        # 갈 수 있는 노드 있음
        if cands:
            stack.extend(cands)

        else:
            # 끝자락에 도착
            print("끝자락 도착")
            answer.append(copy.deepcopy(path))

            while path:
                print("빠진 노드: ", path.pop())
                try:
                    temp = path[-1]
                except:
                    return answer

                arr = []
                for i in range(len(graph[temp])-1, -1, -1):
                    if graph[temp][i] == 1 and not visited[i]:
                        arr.append(i)

                if arr:
                    print("이제 그만 뺌")
                    print("탐색 시작할 노드: ", temp)
                    break
                else:
                    print("아직 pop해야함")
                    print("빠진 path: ", path)

    print("\nanswer: ", answer)
    return answer


graph = [[1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1, 0, 0],
         [1, 0, 0, 1, 1, 0, 0, 1],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 1]]

start = 1
print("반복 DFS 정답: ", dfs_iterative(graph, start))