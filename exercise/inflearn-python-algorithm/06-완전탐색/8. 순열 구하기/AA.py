"""
순열 구하기
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두
출력합니다.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
출력순서는 사전순으로 오름차순으로 출력합니다.

▣ 입력예제 1
3 2

▣ 출력예제 1
1 2
1 3
2 1
2 3
3 1
3 2
6
"""
import sys

# # !!!!!!!!! 첫 번째 풀이 !!!!!!!!!
# def dfs(level, arr):
#     global count
#     # print("\nlevel: ", level)
#     # print("check: ", check)
#     if level == depth:
#         for i in arr:
#             print(i, end=" ")
#
#         arr.pop()
#         count += 1
#         print()
#         return
#
#     else:
#         for i in range(1, num + 1):
#             if check[i] == 0:
#                 check[i] = 1
#                 arr.append(i)
#                 dfs(level + 1, arr)
#                 check[i] = 0
#         if arr:
#             arr.pop()


def dfs(level):
    global count
    if level == depth:
        for i in range(depth):
            print(result[i], end=" ")
        print()
        count += 1

    else:
        for j in range(1, num + 1):
            if check[j] == 0:
                check[j] = 1
                result[level] = j
                dfs(level + 1)
                check[j] = 0


if __name__ == "__main__":
    sys.stdin = open("in1.txt", "rt")
    num, depth = map(int, input().split())
    result = [0] * num
    check = [0] * (num+1)
    count = 0
    dfs(0)
    # print("count: ", count)
    print(count)