def solution(n, cost):
    import heapq as hq
    cost.sort(key=lambda x:x[2])
    answer = 0
    visited = [False] * n
    visited[0] = True

    while False in visited:
        for c in cost:
            start, dest, weight = c
            if visited[start] or visited[dest]:
                if visited[start] and visited[dest]:
                    continue
                else:
                    visited[start] = True
                    visited[dest] = True
                    answer += weight
                    break
    return answer

def solution2(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = [0] * n
    visited[0] = 1 #임의의 하나 일단 1로 둠. =visit함
    while sum(visited) != n:
        for cost in costs:
            s, e, c = cost #start, end, cost
            if visited[s] or visited[e]: #start, end 둘 중 하나 1이면
                if visited[s] and visited[e]: #그 중에서도 start, end 둘다 1이면
                    continue #둘이 연결되었다는 거니까 그냥 넘어감.
                else: #둘중 하나만 1이면
                    visited[s] = 1 #둘다 visit됨 처리.
                    visited[e] = 1
                    answer += c #answer
                    break
    return answer


n = 4
cost = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]

print(solution(n, cost))
