def solution(triangle):
    # 0번째 행은 업데이트 할 필요가 없으므로 생략하고, 1번째 행부터 반복한다.
    for i in range(1, len(triangle)):
        # 각 행의 원소의 갯수에 대해 반복한다.
        for j in range(len(triangle[i])):
            # 이 경우는, 각 행의 0번째 원소에 대한 경우이다.
            # 인덱스를 잘 살펴보면, 다른 원소와 크기비교를 할 필요 없이 바로 위에 있는 원소의 더해서 덮어쓰면 된다.
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]

            # 이 경우는 각 행의 마지막 원소에 대한 경우이다.
            # 위와 마찬가지로, 인덱스를 잘 살펴보면 크기비교 필요없이 tri[i-1][j-1]의 값에 해당 원소의 값을 더해서 덮어쓴다.
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]

            # 이 경우는 해당 원소 양옆에 원소들이 있기 때문에, 크기 비교가 필요한 경우이다.
            # 최대값을 구해야 하므로, tri[i-1][j-1], tri[i-1][j]와 비교해서 더 큰 값과 tri[i][j]의 값을 더해서 덮어쓴다.
            else:
                triangle[i][j] = max(triangle[i - 1][j-1], triangle[i - 1][j]) + triangle[i][j]

    # 마지막 행에서 가장 큰 값을 리턴한다.
    print(triangle)
    answer = max(triangle[-1])
    return answer


def solution2(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            print(i, j)
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = max(triangle[i - 1][j-1], triangle[i - 1][j]) + triangle[i][j]

    answer = max(triangle[-1])
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))

