"""
휴가(삼성 SW역량평가 기출문제 : DFS활용)
카운셀러로 일하고 있는 현수는 오늘부터 N+1일째 되는 날 휴가를 가기 위해서, 남은 N일 동
안 최대한 많은 상담을 해서 휴가비를 넉넉히 만들어 휴가를 떠나려 한다.
현수가 다니는 회사에 하루에 하나씩 서로 다른 사람의 상담이 예약되어 있다.
각각의 상담은 상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P로 이
루어져 있다.

만약 N = 7이고, 아래와 같이 예약이 잡혔있다면
    1일  2일  3일      4일   5일  6일  7일
T    4    2   3         3   2    2    1
P   20   10   15        20  30   20   10

1일에 잡혀있는 상담은 총 4일이 걸리며, 상담했을 때 받을 수 있는 금액은 20이다. 만약 1일
에 예약된 상담을 하면 4일까지는 상담을 할 수가 없다.
하나의 상담이 하루를 넘어가는 경우가 많기 때문에 현수는 예약된 모든 상담을 혼자 할 수
없어 최대 이익이 나는 상담 스케쥴을 짜기로 했다.
휴가를 떠나기 전에 할 수 있는 상담의 최대 이익은 1일, 5일, 7일에 있는 상담을 하는 것이
며, 이때의 이익은 20+30+10=60이다.

현수가 휴가를 가기 위해 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

▣ 입력설명
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 1일부터 N일까지 순서대로 주어진다. (1 ≤ T ≤ 7, 1 ≤ P ≤ 100)

▣ 출력설명
첫째 줄에 현수가 얻을 수 있는 최대 이익을 출력한다.

▣ 입력예제 1
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
▣ 출력예제 1

60
"""
import sys

# !!!!!!!!!!!!! 내가 짠 DFS 코드 !!!!!!!!!!!!!
# def dfs(level, p_sum):
#     # print("\nlevel: ", level)
#     # print("p_sum: ", p_sum)
#     global answer
#     if level > day_num:
#         return
#
#     elif level == day_num:
#         if p_sum > answer:
#             answer = p_sum
#             # print("answer: ", answer)
#             return
#
#     else:
#         if p_sum > answer:
#             answer = p_sum
#             # print("answer: ", answer)
#
#         start = level
#         next_start = start + duration[level]
#
#         dfs(next_start, p_sum + pay[level])
#         dfs(level+1, p_sum)

# !!!!!!!!!!! 안되는 코드 !!!!!!!!!!!!


def dfs(day, total):
    global answer
    if day == num_day+1:
        if total > answer:
            answer = total
    else:
        if day + duration[day] <= num_day+1:
            dfs(day+duration[day], total+pay[day])

        dfs(day+1, total)


if __name__ == "__main__":
    # sys.stdin = open("in1.txt", "rt")
    num_day = int(input())
    duration = [0]
    pay = [0]

    for _ in range(num_day):
        d, p = map(int, input().split())
        duration.append(d)
        pay.append(p)

    answer = 0
    dfs(1, 0)
    print(answer)

#
#
# import sys
# sys.stdin=open("in1.txt", "r")
# def DFS(L, sum):
#     global res
#     if L==n+1:
#         if sum>res:
#             res=sum
#     else:
#         if L+T[L]<=n+1:
#             DFS(L+T[L], sum+P[L])
#         DFS(L+1, sum)
#
#
# if __name__=="__main__":
#     n=int(input())
#     T=list()
#     P=list()
#     for i in range(n):
#         a, b=map(int, input().split())
#         T.append(a)
#         P.append(b)
#     res=-2147000000
#     T.insert(0, 0)
#     P.insert(0, 0)
#     DFS(1, 0)
#     print(res)
