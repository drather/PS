def solution3(bridge_length, weight, truck_weights):
    t_num = len(truck_weights)
    time = 0
    passing = []
    passed = []

    while truck_weights:
        time += 1

        # 버스 가는중
        if passing:
            for i in range(len(passing)):
                passing[i][1] -= 1

        # 버스 도착
        if passing:
            if passing[0][1] == 0:
                passed.append(passing.pop(0))

        # 버스 출발
        current_weight = 0
        for i in range(len(passing)):
            current_weight += passing[i][0]

        if current_weight + truck_weights[0] <= weight:
            passing.append([truck_weights.pop(0), bridge_length])

    return time + bridge_length


def solution(bridge_length, weight, truck_weights):
    import queue

    time = 0
    t_num = len(truck_weights)
    passing = queue.Queue()
    passed = queue.Queue()

    while len(passed) != t_num:
        print("현재 시점: ", time)
        # bridge_lenth가 0이 됐는지 확인하고, 0이 됐다면 passed로 옮김. 즉, 버스 도착을 구현
        if passing:
            for i in range(len(passing)):
                passing[i][1] -= 1
                print("버스 통과중 , 버스 무게: ", passing[i][0] )

            if passing[0][1] == 0:
                passed.append(passing.pop(0))
                print("버스 무게 ", passed[0][0], "도착")
        else:
            print("통과중인 버스 없음")

        # 현재 다리 위 무게를 확인하고, 다음 버스 출발할 수 있는지 판단. weight 미만이라면 출발, 아니면 대기
        current_weight = 0
        for i in range(len(passing)):
            current_weight += passing[i][0]

        if truck_weights and current_weight + truck_weights[0] < weight:
            print("무게 ", truck_weights.pop(0), "인 버스 출발")
            passing.append([truck_weights.pop(0), bridge_length])

        time += 1
        if time == 8:
            break

    return time


def solution2(bridge_length, weight, truck_weights):
    # 시점
    time = 0

    # 다리를 지나고 있는 트럭
    passing = []

    # 다리를 다 건넌 트럭
    passed = []

    # 대기하고 있는 트럭이 없을 때까지 반복한다.
    while truck_weights:
        # 시점을 1 더한다.
        time += 1
        print("\n-----현재 시점은", time, "입니다-------")

        # 한번 반복하는 동안(한 시점에서 다음 시점으로 가는 동안), 다리를 건너고 있는 버스가 도착하는 것을 구현했다.
        # 다리를 건너고 있는 버스가 있다면,
        if passing:
            for i in range(len(passing)):
                # passing[i][1]의 값을 1 빼준다. passing[i][1]의 값은, 버스가 다리를 건너기 시작한 시점부터 부여받은 bridge_lenth이다
                # 즉, 다리를 건너기까지 남은 시간이 매 시점이 지날때마다 1씩 감소하는 것이다.
                passing[i][1] -= 1
                print("무게 " + str(passing[i][0]) + "인 버스 가는중, 버스 정보: " , "버스 무게: ", passing[i][0], "남은 시간: ", passing[i][1])

        # 그렇게 1초가 지나고, 버스가 도착하기 까지 남은 시간이 0이라면 그 버스는 도착한 것이다.
        # passing배열을 순회하면서,
        if passing:
            print('남은 시간: ', passing[0][1])
            # 가장 먼저 passing배열에 추가된 원소의 첫번째 값이 0이라면 그 원소를 pop해서, passed배열의 원소로 append한다.
            if passing[0][1] == 0:
                print("버스가 도착했습니다")
                print("도착한 버스 무게: ", passing[0][0])
                passed.append(passing.pop(0))
                print("도착한 버스들 목록: ", passed)

        # 버스 출발
        print("\n대기중인 버스 출발여부 판단하겠습니다")
        print("대기중인 버스 무게: ", truck_weights[0])

        # 현재 다리의 무게를 구하기 위한 변수 current_weight
        current_weight = 0
        for i in range(len(passing)):
            current_weight += passing[i][0]
        print("currnet_weight: ", current_weight)

        # 현재 다리를 지나고 있는 버스의 무게와, 대기중인 첫 번째 버스의 무게를 더한 값을 다리가 지탱할 수 있는 무게와 비교한다
        # 만약 두 값을 더한 값이 다리의 최대 무게보다 작다면
        if current_weight + truck_weights[0] <= weight:
            # 대기중인 배열의 원소를 하나 빼고, 건너는 시간을 나타내는 bridge_length값을 포함한 배열 형태를 passing에 append한다.
            passing.append([truck_weights.pop(0), bridge_length])
            print("무게", passing[0][0], "인 버스 출발합니다")
        # 두 값을 더한 값이 다리의 최대 무게보다 작다면 대기중인 버스는 출발하지 못한다.
        else:
            print("무게 초과로 버스 출발 안함")

        print("---------"+str(time)+"초 시점 종료-------------")
    return time + bridge_length


# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print("정답: ", solution2(bridge_length, weight, truck_weights))


