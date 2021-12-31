col_num, row_num = map(int, input().split())
cur_row, cur_col, cur_drct = map(int, input().split())
board = []

for i in range(row_num):
    temp = list(map(int, input().split()))
    board.append(temp)

visited = [[0] * (col_num+1) for i in range(row_num+1)]
visited[cur_row][cur_col] = 1
directions = [0, 1, 2, 3]
d_row = [1, 0, -1, 0]
d_col = [0, -1, 0, 1]

# 반복
# 1. 현재 방향 + 1  % 4 해서, 다음 방향 찾기
# 2. 그 방향으로 간 위치가 미방문 지점 and 육지 and 유효한 좌표라면 -> 이동
# 3. 그 방향으로 간 위치가 조건에 안맞으면, 그냥 넘어감
# 4. 네방향 모두 가본 칸이거나 바다로 되어있는 칸인 경우, 방향 유지한채 한칸 뒤로 후진한 뒤 1단계로 돌아간다.
# 5. 후진할 위치가 바다거나, 유효한 좌표가 아닌 경우에는 종료한다.

while True:
    cur_drct = (cur_drct + 1) % 4
    print(cur_drct)

    for i in range(4):
        new_row = cur_row + d_row[i]
        new_col = cur_col + d_col[i]

        # 조건에 안맞음
        if new_row <= 0 or new_col <= 0 or board[new_row][new_col] == 1 or visited[new_row][new_col] == 1:
            continue

        # 조건에 맞음
        else:
            visited[new_row][new_col] = 1
            cur_row = new_row
            cur_col = new_col
            print(f"이동한 위치: {new_row}, new_col: {new_col}")
            break
            






