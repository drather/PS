
def bfs(graph, start, visited):
    queue = [start]
    print(visited)
    if visited[start] == -1:
        print(start, "방문")
        visited[start] = 1

    while queue:
        temp = queue.pop(0)
        for i in range(len(graph[temp])):
            if start == i:
                print(temp, i, "자기 자신과의 연결")
            elif visited[i] == 1:
                print(temp, i, "이미 방문한 노드")
            elif graph[temp][i] == 0:
                print(temp, i, "연결 안된 노드")
            else:
                visited[i] = 1
                queue.append(i)
                print(start, i, "방문")
                print("queue: ", queue)

    print("visited: ", visited)


def bfs_solution(n, computers):
    visited = [-1] * n
    answer = 0

    for i in range(len(visited)):
        if visited[i] == -1:
            answer += 1
            start = i
            queue = [start]
            visited[start] = 1
            print(start, "방문")

            while queue:
                temp = queue.pop(0)
                for j in range(len(computers[temp])):
                    if temp == j:
                        print(temp, j, "자기 자신과의 연결")
                    elif visited[j] == 1:
                        print(temp, j, "이미 방문한 노드")
                    elif computers[temp][j] == 0:
                        print(temp, j, "연결 안된 노드")
                    else:
                        visited[j] = 1
                        queue.append(j)
                        print(start, j, "방문")
                        print("queue: ", queue)
                print(temp, "bfs한 결과 vistied: ", visited)
                print("---", temp, "bfs 끝---\n")

    return answer


def dfs_iterative_solution(n, computers):
    visited = [-1] * n
    visit_order = []
    answer = 0
    nodes = range(n)

    for i in range(len(visited)):
        if visited[i] == -1:
            answer += 1
            start = i
            stack = [start]
            visited[start] = 1
            print(start, "방문")
            visit_order.append(start)

            while stack:
                temp = stack.pop()
                for j in range(len(computers[temp])):
                    if temp == j:
                        print(temp, j, "자기 자신과의 연결")
                    elif visited[j] == 1:
                        print(temp, j, "이미 방문한 노드")
                    elif computers[temp][j] == 0:
                        print(temp, j, "연결 안된 노드")
                    else:
                        visited[j] = 1
                        stack.append(j)
                        visit_order.append(j)
                        print(start, j, "방문")
                        print("stack: ", stack)

    print("방문 순서: ", visit_order)
    return answer


answer = 0


def recursion(n, computers, visited, start):
    global answer
    visited[start] = 1
    print(start, "방문")

    dest = []
    for i in range(len(computers[start])):
        if computers[start][i] == 1 and start != i and visited[i] == -1:
            dest.append(i)

    print("Dest: ", dest)
    if dest:
        for i in range(len(dest)):
            recursion(n, computers, visited, dest[i])

    else:
        return

def recursion2(n, computers, visited, start):
    global answer
    visited[start] = 1
    print(start, "방문")

    for i in range(len(computers[start])):
        if computers[start][i] == 1 and start != i and visited[i] == -1:
            print("다음에 갈 노드: ", i)
            recursion2(n, computers, visited, i)
    return


def dfs_recursive_solution(n, computers):
    global answer
    visited = [-1] * n

    for i in range(0, n):
        if visited[i] == -1:
            print("main함수 반복,", i, "에서 dfs 시작")
            answer += 1
            recursion2(n, computers, visited, i)
    print("main함수 반복 끝\n")
    return answer


computers = [[1,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = len(computers)
print("dfs_재귀 정답: ", dfs_recursive_solution(n, computers), "\n\n")
print("dfs_반복 정답: ", dfs_iterative_solution(n, computers), "\n\n")
print("bfs 정답: ", bfs_solution(n, computers), "\n\n")

# 정답: 1
