"""
BFS 기반 위상정렬로 풀어보다가 안돼서
플로이드 알고리즘으로 풀어본다.

코드 너무 더러우니깐 좀 정리해서 올릴 것
"""
def solution(n, results):
    mat = [[0 for i in range(n+1)] for j in range(n+1)]

    for edge in results:
        start = edge[0]
        dest = edge[1]
        mat[start][dest] = 1

    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                mat[i][j] = 0
            elif mat[i][j] == 0:
                mat[i][j] = 999

    for k in range(1, len(mat)):
        for i in range(1, len(mat)):
            for j in range(1, len(mat)):
                if mat[i][k] + mat[k][j] < mat[i][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]

    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if mat[i][j] == 999:
                mat[i][j] = 0

            if mat[i][j] >= 1:
                mat[i][j] = 1

    out_degrees = []
    for i in mat:
        out_degree = sum(i)
        out_degrees.append(out_degree)

    print("out: ", out_degrees)

    in_degrees = []
    for col in range(len(mat)):
        _sum = 0
        for row in range(len(mat)):
            _sum += mat[row][col]
        in_degrees.append(_sum)

    print("in: ", in_degrees)
    answer = 0
    for i in range(len(in_degrees)):
        if in_degrees[i] + out_degrees[i] == n-1:
            answer += 1

    return answer


results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
n = 5
print(solution(n, results))
