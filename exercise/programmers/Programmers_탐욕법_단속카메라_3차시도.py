def solution(routes):
    routes.sort()
    answer = 0
    check = [0] * len(routes)
    print("초기 routes: ", routes)
    print("초기 check: ", check)

    # routes는 0번째 값을 기준으로 정렬한 배열이다. 각 차량의 진입, 진출 시점을 갖는다.
    # i 는 routes 배열을 순회하는 인덱스이다. 마지막 원소부터 처음 원소로 이동한다.
    for i in range(len(routes) - 1, -1, -1):
        if check[i] == 0:
            print("\ni: ", i)
            camera = routes[i][0]
            print("camera: ", camera)
            answer += 1
            print("answer: ", answer)

        # j 는 i부터 0까지 순회하는 인덱스이다.
        # check 배열을 순회한다.
        for j in range(i, -1, -1):
            # check 배열의 j번째 원소가 0 이고, routes 의 j번째 원소의 진출 지점이 camera보다 크며, routes의 j번째 지점의 진입 지점이 camera보다 작으면
            if check[j] == 0 and routes[j][1] >= camera >= routes[j][0]:
                print("j: ", j)
                check[j] = 1
                print("check: ", check)

    return answer


routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))
