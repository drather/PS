"""
- 서울 - a - b - 경산을 거쳐, K시간 이내에 모금할 수 있는 최대 금액을 구할 것
- 각 도시 사이의 구간을 구간1, 구간2, 구간3이라 함
- 각 구간을 이동할 때, 도보로 갈 수도 있고, 자전거로 갈 수도 있음
- 각 방법에 대한 소요시간과 모금액은 다름
- travel 배열의 행의 갯수는 구간의 갯수를 의미한다
- travel 배열의 각 행은 [도보로 이동시 소요시간, 도보 이동시 모금 금액, 자전거 이동시 소요시간, 자전거 이동시 모금 금액]이다
- 즉, travel배열은 구간의 갯수와 각 구간에서 도보, 자전거 선택에 대한 소요시간과 금액에 대한 정보를 가진다

- 각 단계에서, travel 배열의각 원소의 값을 따져서, 최대값을 구한다.
- 너무 어려운거같으니까 다음에 풀어보자.
"""
def solution(k, travel):
    answer = 0

    # k *= 60      # 단위를 분으로 바꿈
    path_num = len(travel)
    dp = []
    for i in range(path_num+1):
        dp.append([0, 0])

    travel.insert(0, ([0] * len(travel[-1])))

    print("dp: ", dp)
    print("경로의 갯수: ", path_num)
    print("초기 travel: ", travel)
    for i in range(1, len(dp)):
        print("\n반복 회차: ", i)
        time = dp[i-1][0]
        money = dp[i-1][1]
        print("살펴볼 경로: ", travel[i])
        print("이전까지 시간 합: ", time)
        print("이전까찌 모금액 합: ", money)

        # 도보로 가는 길이 시간 초과가 나는경우, 자전거를 선택한다.
        if time + travel[i][0] >= k:
            time += travel[i][2]
            money += travel[i][3]
            print("자전거로 가면 시간 초과나기 때문에 도보 선택")

        # 자전거로 가는 길이 시간 초과가 나는 경우, 도보를 선택한다.
        elif time + travel[i][2] >= k:
            time += travel[i][0]
            money += travel[i][1]
            print("도보로 가면 시간 초과나기 때문에 자전거 선택")

        # 두 방법 모두 다 시간 초과가 나지 않는 경우, 더 큰 값을 선택하고, money와 time에 합산한다.
        else:
            # 도보로 가는 경우가 모금액이 더 큰 경우
            if travel[i][1] > travel[i][3]:
                print("도보 선택")
                time += travel[i][0]
                money += travel[i][1]

            # 자전거로 가는 경우가 모금액이 더 큰 경우
            elif travel[i][1] < travel[i][3]:
                print("자전거 선택")
                time += travel[i][2]
                money += travel[i][3]

            # 두 경우 모금액이 같은 경우, 시간이 더 작은 것을 선택한다.
            else:
                print("도보랑 자전거랑 금액 같음, 시간 덜걸리는거 선택")
                time += min(travel[i][0], travel[i][2])
                money += travel[i][1]

        dp[i] = [time, money]
        print("dp[i]:", dp[i])

    print("결과 배열: ", dp)
    print("걸린 시간: ", dp[-1][0])
    print("최대 비용: ", dp[-1][1])

    return answer


# k = 1650
# travel = [[500, 200, 200, 100],
#           [800, 370, 300, 120],
#           [700, 250, 300, 90]]
k = 3000
travel = [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]

print(solution(k, travel))