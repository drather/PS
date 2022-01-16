"""
사과나무(BFS)
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저
있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사
과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서
남겨놓는다.

만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다.
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
현수과 수확하는 사과의 총 개수를 출력하세요.

▣ 입력설명
첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
각 격자안의 사과의 개수는 100을 넘지 않는다.

▣ 출력설명
수확한 사과의 총 개수를 출력합니다.

▣ 입력예제 1
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

▣ 출력예제 1
379
"""
import sys
from _collections import deque as dq

# sys.stdin = open("in1.txt", "rt")

n = int(input())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

start = [n // 2, n // 2]
# print("start: ", start)

check = [[0] * n for _ in range(n)]
check[start[0]][start[1]] = 1

queue = dq([])
queue.append(start)

answer = mat[start[0]][start[1]]
level = 0

while queue:
    # print("\nlevel: ", level)
    if level == n // 2:
        break

    for i in range(len(queue)):
        temp = queue.popleft()
        # print("temp: ", temp)

        for j in range(4):
            new_row = temp[0] + dx[j]
            new_col = temp[1] + dy[j]

            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat) and check[new_row][new_col] == 0:
                new_elem = (new_row, new_col)
                check[new_row][new_col] = 1
                queue.append((new_row, new_col))
                answer += mat[new_row][new_col]

                # print("new_elem: ", new_elem)

    level += 1

print(answer)












