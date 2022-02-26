"""
반복
1. 현재 방향 + 1  % 4 해서, 다음 방향 찾기
2. 그 방향으로 간 위치가 미방문 지점 and 육지 and 유효한 좌표라면 -> 이동
3. 그 방향으로 간 위치가 조건에 안맞으면, 그냥 넘어감
4. 네방향 모두 가본 칸이거나 바다로 되어있는 칸인 경우, 방향 유지한채 한칸 뒤로 후진한 뒤 1단계로 돌아간다.
5. 후진할 위치가 바다거나, 유효한 좌표가 아닌 경우에는 종료한다.

- 방향에 따른 이동
    - direction, d_row, d_col 배열
- 회전 횟수 turn_count 로 더이상 갈 곳이 있나 없나 확인
-
"""

col_num, row_num = map(int, input().split())
cur_row, cur_col, cur_direction = map(int, input().split())
board = []

for i in range(row_num):
    temp = list(map(int, input().split()))
    board.append(temp)

visited = [[0] * col_num for i in range(row_num)]
visited[cur_row][cur_col] = 1

d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]


def turn_left():
    global cur_direction, turn_count
    cur_direction -= 1
    if cur_direction == -1:
        cur_direction = 3


# 방문한 칸 갯수
visit_count = 1

# 회전한 갯수. 4가 되면 후퇴
turn_count = 0

print(f"현재 위치: {cur_row}, {cur_col}, 방향: {cur_direction} 에서 반복 시작")
while True:
    turn_left()
    print(f"좌회전, 현재 방향: {cur_direction}")

    # 다음으로 이동할 칸
    new_row = cur_row + d_row[cur_direction]
    new_col = cur_col + d_col[cur_direction]
    print(f"이동할 위치: {new_row}, {new_col}")

    # 이동할 칸이 미방문 & 육지인 경우
    if visited[new_row][new_col] == 0 and board[new_row][new_col] == 0:
        # 해당 칸으로 이동
        cur_row = new_row
        cur_col = new_col
        board[cur_row][cur_col] = 1

        # 방문 횟수 1 증가
        visit_count += 1

        # 회전 횟수 0으로 초기화
        turn_count = 0
        print(f"이동한 위치: {cur_row}, {cur_col}, 방향: {cur_direction}, 방문 횟수: {visit_count}")

        continue

    else:
        turn_count += 1
        print(f"조건 불만족, 좌회전. 증가한 좌회전 수: {turn_count}")

    # 4 방향 모두 확인한 경우, 즉 갈 곳이 더이상 없는 경우
    if turn_count == 4:
        # 한 칸 후진할 위치
        new_row = cur_row - d_row[cur_direction]
        new_col = cur_col - d_col[cur_direction]
        print(f"후진할 위치: {new_row}, {new_col}")

        # 한 칸 후진할 위치가 바다라면, 종료
        if board[new_row][new_col] == 1:
            print(f"후진할 위치가 바다라서 종료, {board[new_row][new_col]}")
            break

        else:
            # 한칸 후진
            cur_row = new_row
            cur_col = new_col
            print(f"후진, 현 위치: {new_row}, {new_col}")

        turn_count = 0


print(visit_count)
