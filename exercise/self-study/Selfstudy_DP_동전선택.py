"""
동전 줍기 문제

입력
coins: [ c1, c2, c3, ... , cn]   동전들의 액면가를 나타낸다

출력
coins에 나타난 동전들 중에서, 인접한 동전을 선택하지 않으면서 최대 값을 가지는 조합을 출력

f배열을 순회하면서, 각 요소들을 채울 것이다
f[0] = 0이다

f[i] 는 i번쨰 동전을 선택할지 말지에 대한 답을 갖는다.
즉, f[i] = max(f[i-1], f[i-2] + coins[i])인데, i-1번째 동전을 선택한 것과, i번째 동전을 선택한 경우 두 가지 중 큰 값을 저장한다.
"""


def solution(coins):
    answer = 0
    coins.insert(0, 0)
    f = []

    for i in range(len(coins)):
        f.append(0)

    f[0] = 0
    f[1] = coins[1]

    for i in range(2, len(f)):
        f[i] = max(f[i-1], f[i-2] + coins[i])

    print(f)
    return answer


#coins = [5, 1, 2, 10, 6, 2]
coins = [3,2,5,4,1]
solution(coins)

