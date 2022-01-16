# 미완성
"""
left: 0
right: 60
mid: 30
즉, 30초를 추정치로 잡았을 떄, 30 // 7, 30 // 10 한 몫을 누적시켜본다.
그럼 4 + 3으로, 7이다. 근데, 이 result 값이 n보다 크다. 따라서, 원하는 값은 mid보다 작은 값이다.
그러므로, left는 그대로 두고, right를 29로 한다.

left: 0
right: 29
mid: 14
즉, 14초를 추정치로 잡았을 때, 14 // 7, 14 // 10 의 값을 누적시킨다.
그럼 2 + 1로, 3이다. 이 result값이 n보다 작다. 따라서, 원하는 값은 mid보다 큰 값이다.
따라서, left를 mid + 1로 바꾸고, right는 그대로 둔다.

left: 15
right: 29
mid: 22
22초를 추정치로 했을 떄, 22 // 7, 22 // 10의 값을 누적시킨다
그럼 3 + 2로 5다. 이 값은 n보다 작다. 따라서, 원하는 값은 mid보다 큰 값이다.
따라서, left를 mid + 1로, right를 그대로 둔다.

left = 23
right = 29
mid = 26
26초를 추정치로 했을 때, 26 // 7, 22 // 10의 값을 누적시킨다.
그럼 3 + 2로 5다. n보다 작다.
left를 27로, right를 29로 한다

left = 27
right = 29
mid: 28
28초를 추정치로 했을 때, 28 // 7, 28 // 10의 값을 누적시킨다.
그럼 4 + 2로 6이다. n과 같다.



"""


def solution(n, times):
    left = 0
    right = max(times) * n
    temp = right
    answer = right

    while left <= right:
        mid = (left + right) // 2
        print("\nleft: ", left)
        print("right: ", right)
        print("mid: ", mid)

        result = 0
        temp = 0
        # times 배열을 순회한다.
        for i in range(len(times)):
            # result 변수에, mid 값(추정값)을 times의 i번째 원소로 나눈 몫을 누적시킨다.
            result += mid // times[i]
            # print("누적중인 중간결과: ", result)

        print("중간결과: ", result)

        # 예측한 값으로 뽑아낸 중간 결과가 n과 같으면
        if result == n:
            # 예측한 값으로 뽑아낸 중간 결과가 n과 같고, answer의 값(right)이 추정치보다 크면, mid의 값을 answer에 할당한다.
            # 이것은 즉,
            print("answer의 값: ", answer)
            if answer >= mid:
                answer = mid
                print("answer: ", answer)
            right = mid - 1

        # 중간결과(사람수)가 n보다 크면
        elif result > n:
            right = mid - 1

        # 중간결과(사람수)가 n보다 작으면
        else:
            left = mid + 1

    print("answer: ", answer)

    return right + 1


n = 6
times = [7, 10]
print("\n정답: ", solution(n, times))
