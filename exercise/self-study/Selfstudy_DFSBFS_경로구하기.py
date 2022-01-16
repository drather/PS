"""
한 점에서 시작해서, 갈 수 있는 모든 경로를 구해보자.
1. DFS(Iterative)
    1). start노드를 정한다(input start로)
    2). graph[start]를 순회하면서, start에서 갈 수 있는 노드들을 cands1배열에 담아둔다.
    3). cands배열이 있다면, cands1배열을 순회한다.
        3-1). cands1 배열의 원소 하나하나마다 갈 수 있는 원소들을 cands2 배열에 저장한다.
        3-2). cands2 배열을 cands1 에 할당한다.
        3-3). start에 cands1의 원소를 하나 pop해서 할당한다.
    4). cands배열이 없다면,
        4-1). path.pop을 한다.
        4-2).
2. DFS(Recursive)
"""
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
        print("\n반복 횟수: ", count)
        print("stack: ", stack)
        start = stack.pop()
        print(start, "방문")
        visited[start] = True
        path.append(start)
        print("path: ", path)

        cands = []
        for i in range(len(graph[start])):
            if not visited[i] and graph[start][i] == 1:
                cands.append(i)

        print("인접한 노드: ", cands)
        # 갈 수 있는 노드 있는 경우
        if cands:
            stack.extend(cands)

        else:
            # 끝자락에 도착
            print("끝자락 도착")
            answer.append(copy.deepcopy(path))

            path.pop()
            temp = path[-1]
            print("temp: ", temp)
            # print("graph[temp]: ", graph[temp])

            arr = []
            for i in range(len(graph[temp])):
                if graph[temp][i] == 1 and not visited[i]:
                    arr.append(i)

            if arr:
                print("arr: ", arr)
                continue
            else:
                print("아직 pop해야함")
                print("빠진 노드: ", path.pop())
                print("path: ", path)

    print("\nanswer: ", answer)
    return answer


# 재귀적 DFS
def recurse(graph, start, answer, path, input_start):
    print("\n시작 노드: ", start)
    path.append(start)
    print("현재 path: ", path)
    cands = []

    # 갈 수 있는 노드 찾기
    for i in range(len(graph[start])):
        if i != start and graph[start][i] == 1:
            cands.append(i)

    # 갈 수 있는 노드가 없다면, 현재까지의 path를 answer의 원소로 저장하고, return하는 것으로 종료
    if not cands:
        answer.append(copy.deepcopy(path))
        print("끝자락에 도착해서 종료, answer: ", answer)
        print("빠질 노드: ", path.pop())
        print("path: ", path)
        return

    # 갈 수 있는 노드가 있다면, 그 노드로 가는 경로에 해당하는 graph의 원소를 0으로 바꾸고, 재귀 호출
    else:
        print("후보노드: ", cands)
        while cands:
            cand = cands.pop(0)
            graph[start][cand] = 0
            graph[cand][start] = 0
            recurse(graph, cand, answer, path, input_start)

        # 반복이 끝났다는 것은 해당 노드에서 더이상 갈 수 있는 노드가 없다는 뜻. 따라서 path에서 pop한다.
        print("반복 끝나고 빠질 노드: ", path.pop())


def dfs_recursive(graph, input_start):
    path = []
    answer = []
    start = input_start
    recurse(graph, start, answer, path, input_start)

    return answer


# graph = [[1, 1, 1, 1, 0, 0, 0, 0],
#          [1, 1, 0, 0, 0, 0, 0, 0],
#          [1, 0, 1, 0, 0, 1, 0, 0],
#          [1, 0, 0, 1, 1, 0, 0, 1],
#          [0, 0, 0, 1, 1, 0, 0, 0],
#          [0, 0, 1, 0, 0, 1, 1, 0],
#          [0, 0, 0, 0, 0, 1, 1, 0],
#          [0, 0, 0, 1, 0, 0, 0, 1]]

graph = [[0, 1, 1, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0]]

start = 1
# print("반복 DFS 정답: ", dfs_iterative(graph, start))
print("\n\n재귀 DFS 정답: ", dfs_recursive(graph, start))
