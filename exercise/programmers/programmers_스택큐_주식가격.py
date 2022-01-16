def solution(prices):
    # 정담을 담을 배열
    answer = [0] * len(prices)

    # i, j를 이용해서 2중 for문으로 해결할 것
    # 첫 번째 for문의 인덱스 i는 0번째부터 len(prices)-1 까지 움직인다
    # 그 다음 for문의 인덱스 j는 1번째부터 len(prices)까지 움직인다.
    for i in range(0, len(prices)-1):
        for j in range(i + 1, len(prices)):
            # 순회하면서, 일단 answer 배열의 i번째 원소를 1 증가시킨다.
            answer[i] += 1

            # 현 시점의 값보다 낮은 값이 나오는 순간 반복을 멈춘다.
            if prices[i] > prices[j]:
                break

    return answer


def solution2(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        stack.append(prices[i])
        if len(stack) < 2:
            continue

        answer[i] += 1


prices = [1, 2, 3, 2, 3]
# answer = [4,3,1,1,0]
print(solution(prices))