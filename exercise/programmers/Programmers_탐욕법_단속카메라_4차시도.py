def solution(routes):
    routes.sort()
    check = [0] * len(routes)
    answer = 0
    for i in range(len(routes)-1, -1, -1):
        if check[i] == 0:
            camera = routes[i][0]
            answer += 1
        for j in range(i, -1, -1):
            if check[j] == 0 and routes[j][1] >= camera >= routes[j][0]:
                check[j] = 1

    return answer
    print("answer: ", answer)


routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))