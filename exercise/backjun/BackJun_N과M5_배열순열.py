"""
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

# 조합을 구한 것. 여기선 순열을 구해야 함
# def dfs(level, start):
#     global result
#     # print("\nlevel: ", level)
#     # print("Start: ", start)
#     if level == limit:
#         for r in result:
#             print(r, end=" ")
#         print()
#
#     else:
#         # print("check: ", check)
#         for i in range(start, num):
#             result[level] = arr[i]
#             dfs(level+1, i+1)


def dfs(level):
    global result
    # print("\nlevel: ", level)
    # print("check: ", check)
    if level == limit:
        for r in range(len(result)):
            print(result[r], end=" ")
        print()

    else:
        for i in range(0, len(arr)):           # i가 0부터 (length-1) 까지 순회
            if check[arr[i]] == 0:                   # i가 0이면
                check[arr[i]] = 1                    # 방문했다 표기
                result[level] = arr[i]
                dfs(level+1)                    # level+1 을 호출
                check[arr[i]] = 0                    # level+1에 대한 dfs 가 끝나면 check[i] 를 0으로 함


if __name__ == "__main__":
    # num, limit = map(int, input().split())
    # arr = list(map(int, input().split()))
    num, limit, arr = 4, 2, [9, 8, 7, 1]
    check = [0] * (max(arr)+1)

    arr.sort()
    result = [0] * limit
    dfs(0)
