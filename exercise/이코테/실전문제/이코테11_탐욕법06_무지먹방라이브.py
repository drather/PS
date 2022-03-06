"""
https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

그냥 먹방을 하면 다른 방송과 차별성이 없기 때문에 무지는 아래와 같이 독특한 방식을 생각해냈다.

회전판에 먹어야 할 N 개의 음식이 있다.
각 음식에는 1부터 N 까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다.
무지는 다음과 같은 방법으로 음식을 섭취한다.

무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.
다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.
무지가 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다.
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times,
네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때
몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하라.
"""
import heapq


def solution2(food_times, k):
    pq = []
    length = len(food_times)
    times_sum = 0
    remain_time = k

    if sum(food_times) < k:
        return -1

    [heapq.heappush(pq, [ft, idx]) for idx, ft in enumerate(food_times, 1)]

    while True:
        print()
        time, idx = heapq.heappop(pq)
        required_time = time * length

        print(f"length, time, idx: {length}, {time}, {idx}")
        print(f"remain_time, required_time: {remain_time}, {required_time}")
        print(f"remain_time - required_time: {remain_time - required_time}")

        if remain_time - required_time < 0:
            print("종료해야 할 반복 돌입")
            answer_idx = idx
            # for i in range(remain_time):
            #     _, answer_idx = heapq.heappop(pq)
            print(f"first_answer_idx: {answer_idx}")
            while pq:
                _, answer_idx = heapq.heappop(pq)
                print(f"answer_idx: {answer_idx}")

            return answer_idx

        else:
            for elem in pq:
                elem[0] -= time
                print(elem)

            remain_time -= required_time
            length -= 1

            print(f"remain_time: {remain_time}")


def solution1(food_times, k):
    idx_time_arr = sorted([(idx, ft) for idx, ft in enumerate(food_times, 1)],
                          key=lambda x: x[1])
    print([v[1] for v in idx_time_arr])

    for idx, food_time in idx_time_arr:
        print(f"\tidx: {idx}")
        print(f"\tfood_time: {food_time}")
        print(f"\tk: {k}")

        k -= food_time

        print(f"\tk - food_time: {k}")
        print()

        if k < 0:
            print("\t종료")
            return idx

    return -1


if __name__ == '__main__':
    # inputs = [
    #     ([3, 1, 2], 5),
    #     ([4, 1, 3, 2], sum([4, 1, 3, 2])-1),
    #     ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 8),
    #     ([1, 1, 1, 1, 1], 5),
    #     ([10, 20, 30, 100, 50, 30, 2], 184)
    # ]
    # result1 = 1
    #
    # for i, j in enumerate(inputs, 1):
    #     print("answer: ", solution1(*j))
    #     print()

    print(f"answer: {solution2([10, 20, 30, 100, 50, 30, 2], 184)}")
