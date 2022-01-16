"""
최대점수 구하기(DFS)
이번 정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를
풀려고 합니다. 각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩
니다. 제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다. (해당문제는
해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다.)

▣ 입력설명
첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.

▣ 출력설명
첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.

▣ 입력예제 1
5 20
10 5
25 12
15 8
6 3
7 4

▣ 출력예제 1
41
"""
import sys


def dfs(level, score, time):
    global res

    if time > m:
        return

    if level == n:
        if score > res:
            res = score

    else:
        dfs(level + 1, score + pv[level], time + pt[level])
        dfs(level + 1, score, time)


if __name__ == "__main__":
    sys.stdin = open("in1.txt", "rt")

    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)

    res = -2147000
    dfs(0, 0, 0)
    print(res)



# !!!!!!!!!!!!!!!!! 나의 풀이 !!!!!!!!!!!!!!!!!
# def dfs(q_idx, score_total, time_total):
#     global answer
#     # print("\nq_idx: ", q_idx)
#     # print("score합: ", score_total)
#     # print("time 합: ", time_total)
#
#     if time_total > time_limit:
#         return
#
#     if q_idx == q_num:
#         if score_total > answer:
#             answer = score_total
#
#     else:
#         dfs(q_idx + 1, score_total + questions[q_idx][0], time_total + questions[q_idx][1])
#         dfs(q_idx + 1, score_total, time_total)
#
#
# if __name__ == "__main__":
#     # sys.stdin = open("in1.txt", "rt")
#     q_num, time_limit = map(int, input().split())
#     questions = []
#
#     for _ in range(q_num):
#         questions.append(tuple(map(int, input().split())))
#
#     answer = 0
#     check = [0] * (q_num + 1)
#
#     dfs(0, 0, 0)
#     print(answer)

