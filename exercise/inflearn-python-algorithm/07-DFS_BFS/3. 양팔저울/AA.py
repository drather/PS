"""
양팔저울(DFS)
무게가 서로 다른 K개의 추와 빈 그릇이 있다. 모든 추의 무게는 정수이고, 그릇의 무게는 0
으로 간주한다. 양팔저울을 한 번만 이용하여 원하는 물의 무게를 그릇에 담고자 한다.
주어진 모든 추 무게의 합을 S라 하자. 예를 들어, 추가 3개이고, 각 추의 무게가 {1, 2, 6}이
면, S=9이고, 양팔저울을 한 번만 이용하여 1부터 S사이에 대응되는 모든 무게의 물을 다음과
같이 그릇에 담을 수 있다. X는 그릇에 담는 물의 무게이고, ⎕은 그릇을 나타낸다.

X   1       2       3           4       5       6   7   8   9
    ⎕:1     ⎕:2     ⎕:(1+2) (⎕+2):6 (⎕+1):6 ⎕:6 ⎕:(1+6) ⎕:(2+6) ⎕:(1+2+6)
만약 추의 무게가 {1, 5, 7}이면 S=13이고, 그릇에 담을 수 있는 물의 무게는 {1, 2, 3, 4, 5,
6, 7, 8, 11, 12, 13}이고, 1부터 S사이에서 무게에서 9와 10에 대응하는 무게의 물을 담을
수 없다.
K(3<=K<=13)개의 추 무게가 주어지면, 1부터 S사이의 정수 중 측정이 불가능한 물의 무게는
몇 가지가 있는 지 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 K(3<=K<=13)이 주어집니다.
두 번째 줄에 K개의 각 추의 무게가 공백을 사이에 두고 주어집니다. 각 추의 무게는 1부터
200,000까지이다.

▣ 출력설명
첫 번째 측정이 불가능한 가지수를 출력하세요.

▣ 입력예제 1
3
1 5 7

▣ 출력예제 1
2
"""
import sys

# # 내가 짠 첫번째 DFS 코드
# def dfs(level, total):
#     global answer
#
#     # print("\nlevel: ", level)
#     # print("total: ", total)
#
#     if level == w_num:
#         return
#
#     else:
#         if total >= 0:
#             answer[total] = 1
#         else:
#             answer[-total] = 1
#
#         dfs(level + 1, total)
#         dfs(level + 1, total - weight[level])
#         dfs(level + 1, total + weight[level])

# if __name__ == "__main__":
#     # sys.stdin = open("in1.txt", "rt")
#
#     w_num = int(input())
#     weight = list(map(int, input().split()))
#
#     # w_num, weight = 3, [1, 5, 7]
#
#     answer = [0] * (sum(weight) + 1)
#     # print("answer len: ", len(answer))
#     dfs(-1, 0)
#
#     print(answer.count(0))


def dfs(level, total):
    global answer
    if level == w_num:
        if 0 < total <= w_sum:
            answer.add(total)

    else:
        dfs(level+1, total)
        dfs(level+1, total - weight[level])
        dfs(level+1, total + weight[level])


if __name__ == "__main__":
    sys.stdin = open("in1.txt", "rt")

    w_num = int(input())
    weight = list(map(int, input().split()))
    w_sum = sum(weight)

    answer = set()

    dfs(0, 0)
    print(answer)
    print(w_sum - len(answer))
