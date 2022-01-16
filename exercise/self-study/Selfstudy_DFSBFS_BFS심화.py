def solution(graph, input_start, n):
    visited = [False] * len(graph)
    queue = [input_start]
    visited[input_start] = True
    count = 0

    print("반복 시작합니다~")
    while queue:
        print("queue: ", queue)
        count += 1
        new_arr = []
        for i in queue:
            node = i
            for j in range(len(graph[node])):
                if graph[node][j] == 1 and not visited[j] and node != j:
                    new_arr.append(j)
                    visited[j] = True

        queue = new_arr
        if count == n:
            print("count == n 이므로 종료")
            return new_arr


graph = [[1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1]]
n = 3
start = 1
print(solution(graph, start, n))
