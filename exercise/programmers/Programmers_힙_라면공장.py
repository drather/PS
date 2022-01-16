def solution(stock, dates, supplies, k):
    import heapq as hq
    answer = 0
    heap = []
    j = 0

    # stock이 k보다 작을 동안 반복한다
    while stock < k:
        # dates배열을 순회한다.
        for i in range(j, len(dates)):
            # dates배열을 순회하면서, stock이 dates[i]보다 큰 곳을 찾는다.
            # 왜 이러냐면, 공급받는 횟수를 줄이기 위해서 그러는 것인데 좀 쉽게 말하자면 뻐길때까지 뻐기는 것이다.
            if dates[i] <= stock:
                # 공급 받을수 있는 것 중 제일 큰 값을 받기 위해서, supplies[i]를 heap에 push한다
                hq.heappush(heap, (-supplies[i], supplies[i]))
                j = i + 1

            # 공급받아야 하는 시점에서 멈춘다.
            else:
                break;

        # 힙에서 나온 값을 temp에 저장한다. 이 값은 supplies에서 큰 순서대로 저장된다.
        # 그러다가 stock이 k보다 커지는 순간, 반복을 멈추고 answer를 리턴한다.
        temp = hq.heappop(heap)[1]
        stock += temp
        answer += 1


    return answer

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30
print(solution(stock, dates, supplies, k))