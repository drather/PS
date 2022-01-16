"""
동적계획법 문제이다. 한 집을 털면 인접한 두 집을 털 수 없다는 점에서 동전 선택(예제1)문제와 비슷하다.
그러나, 집들이 원형으로 배치되어 있다는 점에서 차이가 있다.
동전 선택 문제에서는 바로 앞에 동전만 고려했다면, 여기선 인접한 두 집의 money도 고려해야 한다.
따라서, 각 인덱스를 나머지 연산으로 고려하면 좋을 것 같다.
"""


def solution(money):
    length = len(money)
    dp = [0] * length

    for i in range(0, len(dp)):
        print(i)
        print("앞에꺼 인덱스: ", (i + length - 1) % length, "앞에꺼 값: ", dp[(i + length - 1) % length])
        print("뒤에꺼 인덱스: ", (i + length - 2) % length, "뒤에꺼 값: ", dp[(i + length - 2) % length] + money[i])
        dp[i] = max(dp[(i + length - 1) % length], dp[(i + length - 2) % length] + money[i])

        print("dp[i]: ", dp[i])
    answer = dp[-1]

    print(dp)
    return answer


def solution2(money):
    length = len(money)
    dp = [0] * length
    dp[0] = money[0]

    print("index:\t", " 0, 1, 2, 3, 4")
    print("money: \t", money, "\n")
    for i in range(len(dp)):
        print("현재 i: ", i)
        print("1번째 전에꺼의 인덱스, 값: ", (i + length - 1) % length, dp[(i + length - 1) % length])
        print("2번째 전에꺼의 인덱스, 값: ", (i + length - 2) % length, dp[(i + length - 2) % length] + money[i])
        dp[i] = max(dp[(i + length - 1) % length],
                    dp[(i + length - 2) % length] + money[i])
        print("dp[i]: ", dp[i])

        print("dp:\t\t", dp)
    answer = dp[-2]
    return answer


def solution3(money):
    length = len(money)
    # dp배열 2개를 선언한다.
    # dp1 배열은 0번째 집을 터는 경우이다. 따라서, 마지막 집은 털지 않는다
    # dp2 배열은 0번째 집을 털지 않는 경우이다. 따라서, 경우에 따라 마지막 집을 털 수도 있다.
    dp1 = [0] * length
    dp2 = [0] * length

    # dp1 배열은 첫 집을 턴다고 가정했기 때문에, dp[0]의 값을 money[0]으로 초기화한다.
    dp1[0] = money[0]

    # 0번부터, len(dp1)-2까지 순회한다. 따라서, dp1[-1]은 0이 들어간다. 그러므로 결과값을 정할 때 dp1[-2]를 사용해야 한다
    for i in range(0, len(dp1) - 1):
        # dp1[i]를 정함에 있어서, 그 dp[i-2] + money[i]와, dp[i-1]을 비교하는 것과 같다.
        # 이 코드에서는 처음 원소와 마지막 원소가 연결되어 있는 것으로 간주해야하므로, 원형 큐의 형식으로 구현했다.
        # 굳이 그럴 필요는 없는 것 같다.
        dp1[i] = max(dp1[(i + length - 1) % length],
                     dp1[(i + length - 2) % length] + money[i])

    # 첫 집을 털지 않는 경우이기 때문에 , 1부터 반복하고 len(dp2)-1까지 반복한다.
    for i in range(1, len(dp2)):
        # 위와 비슷하다.
        dp2[i] = max(dp2[(i + length - 1) % length],
                     dp2[(i + length - 2) % length] + money[i])

    print("dp1[-2]: ", dp1)
    print("dp2[-2]: ", dp2)

    # 두 값중 큰 값을 출력한다.
    answer = max(dp1[-2], dp2[-1])
    return answer


money = [1, 2, 3, 1, 5]
print("정답: ", solution3(money))
