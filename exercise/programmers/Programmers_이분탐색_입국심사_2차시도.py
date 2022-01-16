def solution(n, times):
    left = 0
    right = max(times) * n
    answer = right
    temp = right
    print("초기 left: ", left)
    print("초기 right: ", right)

    while left <= right:
        mid = (left + right) // 2
        print("\n최단 소요 시간의 예측값 mid: ", mid)
        print("left: ", left)
        print("right: ", right)

        result = 0
        for i in times:
            result += mid // i
        print("중간 결과값인 result: ", result)

        # result 값은 예측한 최단 소요시간인 mid 를 통해서 처리할 수 있는 사람 수이다.
        # 이 result 값이 n과 같은 경우, 한 가지 경우를 더 살펴봐야 한다.
        # 더 작은 소요시간 값이 있을 수 있기 때문에, right = mid - 1을 해줘야 한다.
        # 따라서, answer 에 right 를 저장한 뒤, right = mid - 1을 해준다
        # 만약, 조건을 만족하는 값 중 저장한 answer 의 값보다 작은 수가 없다면, answer를 리턴하면서 마무리한다.
        # 근데, times 배열의 원소가 1개인 경우, 이러한 방법은 오답을 낸다
        # 따라서, temp == answer인 경우는 right + 1 을 리턴한다.
        if result == n:
            if answer >= mid:
                answer = mid
                print("---저장한 answer 값: " , answer, "---")
            right = mid - 1
            print("찾은 right 값: ", right)

        # result 값이 총 사람수인 n 보다 작은 경우
        # 예측한 최단 소요 시간이 정답보다 작다는 뜻이다.
        # 따라서, left를 mid + 1 로 해야 한다.
        elif result < n:
            left = mid + 1

        # result 값이 총 사람 수인 n 보다 큰 경우
        # 예측한 최단 소요 시간이 정답보다 크다는 뜻
        # 따라서, right를 mid - 1 로 해야 한다.
        else:
            right = mid - 1

    print("answer: ", answer)
    print("temp: ", temp)
    if answer == temp:
        print("case1")
        print("리턴 값: ", right + 1)
        return right + 1

        print("마지막 left: ", left)
        print("마지막 right: ", right)
    else:
        print("case 2")
        print("리턴 값: ", answer)
        print("마지막 left: ", left)
        print("마지막 right: ", right)

        return answer


n = 6
times = [10]
print("정답: ", solution(n, times))