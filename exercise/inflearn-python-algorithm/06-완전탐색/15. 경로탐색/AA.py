"""
경로 탐색(그래프 DFS)

방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프
로그램을 작성하세요. 아래 그래프에서 1번 정점에서 5번 정점으로 가는 가지 수는
1 2 3 4 5
1 2 5
1 3 4 2 5
1 3 4 5
1 4 2 5
1 4 5

총 6 가지입니다.

▣ 입력설명
첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연
결정보가 주어진다.

▣ 출력설명
총 가지수를 출력한다.

▣ 입력예제 1
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5

▣ 출력예제
6
"""
import sys

# !!!!!!!!!!!!!!!! 내가 쓴 DFS 함수 !!!!!!!!!!!!!!!!
# def dfs(source):
#     global answer
#     # print("\nsource: ", source)
#
#     if source == node_num:
#         answer += 1
#
#     else:
#         cand = mat[source]
#
#         if 1 in cand:
#             for i in range(1, node_num+1):
#                 if not visited[i] and mat[source][i] != 0:
#                     visited[i] = True
#                     dfs(i)
#                     visited[i] = False
#         else:
#             return


def dfs(source):
    global answer
    if source == node_num:
        answer += 1
        # print("path: ", path)
    else:
        for i in range(1, node_num + 1):
            if mat[source][i] == 1 and not visited[i]:
                visited[i] = True
                path.append(i)
                dfs(i)
                visited[i] = False
                path.pop()


if __name__ == "__main__":
    # sys.stdin = open("in1.txt", "rt")
    node_num, link_num = map(int, input().split())

    mat = [[0] * (node_num+1) for _ in range(node_num+1)]

    for _ in range(link_num):
        source, target = map(int, input().split())
        mat[source][target] = 1

    answer = 0
    visited = [False] * (node_num+1)
    visited[1] = True
    path = [1]

    dfs(1)
    print(answer)