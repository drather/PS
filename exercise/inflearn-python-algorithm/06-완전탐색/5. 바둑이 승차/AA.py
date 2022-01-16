"""
바둑이 승차(DFS)
철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태
울수가 없다. 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운
무게를 구하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다.
둘째 줄부터 N마리 바둑이의 무게가 주어진다.

▣ 출력설명
첫 번째 줄에 가장 무거운 무게를 출력한다.

▣ 입력예제 1
259 5
81
58
42
33
61

▣ 출력예제 1
242
"""
import sys
import heapq as hq
# sys.stdin = open("in4.txt", "r")


def dfs(idx, total, subtotal):
    global result
    if total > limit:
        return

    # 아래 조건문의 의미
    # total: 지금까지 선택한 원소들의 누적한 값
    # subtotal: 선택여부가 정해진(O, x)가 정해진 애들의 값을 누적시킨 합
    # total_arr: 전체 배열의 합
    # total + total_arr - subtotal < result 라면 자른다는 얘긴데,
    # 지금껏 더한거 + 아직 선택 여부가 정해지지 않은 애들을 전부다 선택O 해서 더한다고 했는데도 result보다 작다면
    # 그건 무조건 답이 될 수 없다.
    # 그러므로 cut
    if total + total_arr-subtotal < result:
        return

    if idx == dog_num:
        if total > result:
            result = total

    else:
        dfs(idx+1, total + arr[idx], subtotal + arr[idx])
        dfs(idx+1, total, subtotal + arr[idx])


if __name__ == "__main__":
    limit, dog_num = map(int, input().split())
    arr = []
    for _ in range(dog_num):
        arr.append(int(input()))

    total_arr = sum(arr)
    arr.sort()
    result= -1
    dfs(0, 0, 0)
    print(result)





# !!!!!!!!!!! 첫 번째 풀이, input4에서 시간 초과 발생 !!!!!!!!!!!
# def dfs(idx, subtotal):
#     if subtotal > limit:
#         return
#
#     elif idx == dog_num:
#         hq.heappush(answers, (-subtotal, subtotal))
#
#     else:
#         dfs(idx + 1, subtotal + arr[idx])
#         dfs(idx + 1, subtotal)
#
#
# if __name__ == "__main__":
#     limit, dog_num = map(int, input().split())
#     arr = []
#     for _ in range(dog_num):
#         arr.append(int(input()))
#
#     arr.sort()
#     answers = []
#     dfs(0, 0)
#     print(hq.heappop(answers)[1])

