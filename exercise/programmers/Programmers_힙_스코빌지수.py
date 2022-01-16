def check_arr(arr, num):
    for i in range(len(arr)):
        if arr[i] < num:
            return 0
    return 1

# 배열로 푼거
def solution(scovile, k):
    answer = 0
    scovile.sort(reverse=True)
    print("정렬된 scovile, 이제 반복 시작\n", scovile)

    if len(scovile) == 0:
        return -1

    while True:
        if len(scovile) < 2:
            temp = scovile.pop()
            if temp < k:
                return -1
            else:
                return answer

        if check_arr(scovile, k) == 1:
            print("check_arr 결과 확인 끝, 종료함")
            print("최후의 scovile", scovile)
            return answer

        else:
            print("다시 반복")
            answer += 1
            new_scovile = scovile[-1] + 2 * scovile[-2]
            print("new_scovile: ", new_scovile)
            scovile.pop()
            scovile.pop()
            scovile.append(new_scovile)
            scovile.sort(reverse=True)


def solution2(scovile, k):
    import heapq
    answer = 0
    heap = []

    # 입력을 받은 scovile배열을 힙 자료구조인 heap에 넣어준다.
    for i in range(len(scovile)):
        heapq.heappush(heap, scovile[i])

    while True:
        # heap에 원소가 더이상 없다면, -1을 리턴한다
        if len(heap) == 0:
            return -1

        # heap에 원소가 1개밖에 없다면, 2개의 원소를 pop할 수가 없다.
        # 따라서, 하나의 값을 가지고 k보다 높은지 낮은지를 판단해서 결과를 리턴한다.
        if len(heap) == 1:
            # heap에 남아있는 유일한 원소의 값이 k보다 작다면, 더 이상 맵게 만들 수 없다. 따라서 -1을 리턴한다.
            if heap[0] < k:
                return -1
            # heap에 남아있는 유일한 원소의 값이 k보다 크다면, 조건을 만족한 것이므로 answer를 리턴한다
            else:
                return answer

        # 본 문제에서 사용한 힙은 최소 힙이다. 따라서, 0번째에는 값이 가장 작은 원소가 들어가있다.
        # 이 값이 k보다 크다면, 다른 원소들 또한 k보다 큰 것이므로, answer를 리턴한다.
        if heap[0] >= k:
            return answer

        # 그렇지 않고 아직 heap에서 k보다 작은 원소가 있다면, heap에서 원소 2개를 꺼내서 temp1, temp2에 저장한다
        # 그리고 새로운 scovile 값을 만들어서, heap에 푸시한다.
        else:
            answer += 1
            temp1 = heapq.heappop(heap)
            temp2 = heapq.heappop(heap)
            new_scovile = temp1 + 2 * temp2
            heapq.heappush(heap, new_scovile)


scovile = [12, 10, 9, 3, 2, 1]
k = 7
print(solution2(scovile, k))