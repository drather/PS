"""
주어진 그래프를 BFS, DFS를 통해 순회해보자
1. BFS
2. DFS(Iterative)
3. DFS(Recursive)
"""


# 그래프를 bfs함
def bfs(graph, input_start):
    visited = [0] * len(graph)
    queue = [input_start]
    answer = []

    print("반복 시작합니다~")
    while queue:
        print("\nqueue: ", queue)
        node = queue.pop(0)
        print(node, "방문")
        answer.append(node)
        visited[node] = 1
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and visited[i] == 0 and node != i:
                queue.append(i)
    return answer


# 그래프를 반복적으로 dfs함(노드번호 오름차순 고려)
def iterative_dfs_asc(graph, input_start):
    visited = [0] * len(graph)
    answer = []
    stack = [input_start]

    while stack:
        print("\nstack: ", stack)
        temp = stack.pop()
        print("pop된 노드: ", temp)
        visited[temp] = 1
        answer.append(temp)

        for i in range(len(graph[temp]) - 1, -1, -1):
            if graph[temp][i] == 1 and visited[i] == 0 and temp != i:
                stack.append(i)
    return answer


# 그래프를 반복적으로 dfs함
def iterative_dfs_desc(graph, input_start):
    visited = [0] * len(graph)
    answer = []
    stack = [input_start]

    while stack:
        print("\nstack: ", stack)
        temp = stack.pop()
        print("pop된 노드: ", temp)
        visited[temp] = 1
        answer.append(temp)

        for i in range(len(graph[temp])):
            if graph[temp][i] == 1 and visited[i] == 0 and temp != i:
                stack.append(i)
    return answer


# 재귀함수
def recurse(graph, start, visited, answer):
    print("\n방문한 노드: ", start)
    visited[start] = 1
    answer.append(start)

    for i in range(len(graph[start])):
        if graph[start][i] == 1 and visited[i] == 0 and start != i:
            print("다음에 방문할 노드: ", i)
            recurse(graph, i, visited, answer)


# 재귀함수를 이용한 풀이
def recursive_dfs(graph, input_start):
    visited = [0] * len(graph)
    answer = []

    recurse(graph, input_start, visited, answer)
    return answer


graph = [[1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1]]

start = 0
# print("bfs 결과: ", bfs(graph, start))

# print("반복 dfs 결과: ", iterative_dfs_desc(graph, start))
print("재귀 dfs 결과: ", recursive_dfs(graph, start))
