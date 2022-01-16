"""
격자판 회문수
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는
세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5

빨간색처럼 구부러진 경우(87178)는 회문수로 간주하지 않습니다.

▣ 입력설명
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.

▣ 출력설명
5자리 회문수의 개수를 출력합니다.

▣ 입력예제 1
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5

▣ 출력예제 1
3
"""
import sys


def check(arr):
    start_idx = 0
    end_idx = len(arr)-1

    while start_idx <= end_idx:
        if arr[start_idx] != arr[end_idx]:
            return False
        start_idx += 1
        end_idx -= 1

    return True


sys.stdin = open("in1.txt", "rt")

board = [list(map(int, input().split())) for _ in range(7)]
answer = 0



# !!!!!!!!!!!!!!!!!!!!!!!! 2번째 해결 !!!!!!!!!!!!!!!!!!!!!!!!
# for i in range(7):
#     for j in range(7):
#         temp1 = []
#         temp2 = []
#         try:
#             board[i][j]
#             for k in range(j, j + 5):
#                 temp1.append(board[i][k])
#
#             if check(temp1):
#                 answer += 1
#
#             for k in range(i, i + 5):
#                 temp2.append(board[k][j])
#
#             if check(temp2):
#                 answer += 1
#
#         except IndexError:
#             pass
# print(answer)



# !!!!!!!!!!!!!!!!!! 첫번째 해결 !!!!!!!!!!!!!!!!!!!!!!!!!

# # 행 회문 찾기
# for i in range(7):
#     for j in range(7):
#         temp = []
#         try:
#             board[i][j]
#             for k in range(j, j + 5):
#                 temp.append(board[i][k])
#
#             if check(temp):
#                 answer += 1
#
#         except IndexError:
#             break
#
# # 열 회문 찾기
# for i in range(7):
#     for j in range(7):
#         temp = []
#         try:
#             board[i][j]
#             for k in range(i, i + 5):
#                 temp.append(board[k][j])
#
#             if check(temp):
#                 answer += 1
#         except IndexError:
#             break
#
# print(answer)


