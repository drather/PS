"""
스토쿠 검사
스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9
개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
예를 들어 다음을 보자.

1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7

위 그림은 스도쿠를 정확하게 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오
고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색
깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.

완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출
력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.

▣ 출력설명
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

"""
import sys


# 두번째 해결(check 배열을 이용, 한 배열의 값을 다른 배열의 인덱스로 활용해서, CHECK 후 그 합을 이용해 판별)
def check(b):
    check_row = [0] * 10
    check_col = [0] * 10
    for i in range(9):
        for j in range(9):
            check_row[b[i][j]] = 1
            check_col[b[i][j]] = 1

    if sum(check_row) != 9 or sum(check_col) != 9:
        return False

    for i in range(3):
        for j in range(3):
            check_grp = [0] * 10

            for x in range(3):
                for y in range(3):
                    check_grp[b[i * 3 + x][j * 3 + y]] = 1

            if sum(check_grp) != 9:
                return False
    return True

# sys.stdin = open("in2.txt", "rt")
board = [list(map(int, input().split())) for _ in range(9)]
if check(board):
    print("YES")
else:
    print("NO")







"""
######################### 첫번째 해결 #########################
set_row = set()
set_col = set()
set_sub = set()

for row in range(len(board)):
    for col in range(len(board)):
        set_row.add(board[row][col])

for col in range(len(board)):
    for row in range(len(board)):
        set_col.add(board[row][col])

dx = [0, 1, 2]
dy = [0, 1, 2]

i = j = k = 0
x = y = z = 0

flag = True
for i in range(0, 9, 3):
    for j in range(0, 9, 3):

        temp_set = set()
        for x in range(i, i+3):
            for y in range(j, j+3):
                temp_set.add(board[x][y])

        if len(temp_set) != 9:
            flag = False
            break

if flag and len(set_row) == 9 and len(set_col) == 9:
    print("YES")
else:
    print("NO")
"""





