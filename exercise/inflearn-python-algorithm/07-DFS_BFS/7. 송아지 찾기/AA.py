"""
송아지 찾기(BFS : 상태트리탐색)
현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 현수의 위치와 송아
지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과
같은 방법으로 이동한다.

현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수
있다. 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성
하세요.

▣ 입력설명
첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000
까지이다.

▣ 출력설명
점프의 최소횟수를 구한다.

▣ 입력예제 1
5 14

▣ 출력예제 1
3
"""
import sys
from _collections import deque as dq
# sys.stdin = open("in4.txt", "rt")

my_pos, cow_pos = map(int, input().split())

dx = [-1, 1, 5]
queue = dq([])

MAX = 50000
queue.append(my_pos)
distances = [0] * (MAX+1)
check = [0] * (MAX+1)
check[my_pos] = 1
dis = 0

while queue:
    start = queue.popleft()

    if start == cow_pos:
        break

    for i in dx:
        nxt = start + i
        if 0 < nxt < MAX:
            if check[nxt] == 0:
                distances[nxt] = distances[start] + 1
                check[nxt] = 1
                queue.append(nxt)

            # print("이미 갔던 곳: ", start+i)

print(distances[cow_pos])

# # 내가 짠 코드
# queue.append(my_pos)
# answer = 0
#
# while queue:
#     new_queue = set()
#     for i in range(len(queue)):
#         # print("\nqueue의 원소: ", queue[i])
#         for j in range(len(dx)):
#             temp = queue[i] + dx[j]
#             # print("새로찾은 값 temp: ", temp)
#             if temp == cow_pos:
#                 print(answer + 1)
#                 sys.exit(0)
#             else:
#                 new_queue.add(temp)
#
#     queue = dq(new_queue)
#     # print("새로운 queue: ", queue)
#     answer += 1




