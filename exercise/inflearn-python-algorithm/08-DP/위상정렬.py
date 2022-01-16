"""
위상정렬(그래프 정렬)
위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘입니다.
각각의 일의 선후관계가 복잡하게 얽혀있을 때 각각 일의 선후관계를 유지하면서 전체 일의
순서를 짜는 알고리즘입니다.
만약 아래와 같은 일의 순서를 각각 지키면서 전체 일의 순서를 정한다면
1 4 //1번일을 하고 난 후 4번일을 해야한다.

5 4
4 3
2 5
2 3
6 2

1
5
6
4
2
3
전체 일의 순서는 1, 6, 2, 5, 4, 3과 같이 정할 수 있다. 전체 일의 순서는 여러 가지가 있습
니다 그 중에 하나입니다.

▣ 입력설명
첫 번째 줄에 전체 일의 개수 N과 일의 순서 정보의 개수 M이 주어집니다.
두 번째 줄부터 M개의 정보가 주어집니다.
▣ 출력설명
전체 일의 순서를 출력합니다.
▣ 입력예제 1
6 6
1 4
5 4
4 3
2 5
2 3
6 2

▣ 출력예제 1
1 6 2 5 4 3
"""
import sys
from _collections import deque as dq

if __name__ == "__main__":
    sys.stdin = open("in1.txt", "rt")
    task_num, link_num = map(int, input().split())

    graph = [[0] * (task_num+1) for _ in range(task_num+1)]
    in_degrees = [0] * (task_num+1)
    in_degrees[0] = -1
    queue = dq([])
    answer = []

    for _ in range(link_num):
        src, trg = map(int, input().split())
        graph[src][trg] = 1

    # for g in range(1, task_num+1):
    #     print(graph[g][1:])
    # print()

    for col in range(1, task_num+1):
        for row in range(1, task_num+1):
            if graph[row][col] == 1:
                in_degrees[col] += 1
    # print(in_degrees[1:])

    for i in range(1, task_num+1):
        if in_degrees[i] == 0:
            queue.append(i)

    # print("시작할 때 queue: ", queue)

    while queue:
        q_size = len(queue)

        for i in range(q_size):
            src = queue.popleft()
            answer.append(src)
            # print("Src: ", src)

            for j in range(1, task_num + 1):
                # print("j: ", j)
                if graph[src][j] == 1:
                    in_degrees[j] -= 1
                    if in_degrees[j] == 0:
                        queue.append(j)

    print(*answer)