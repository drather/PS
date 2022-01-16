def solution(m, n, puddles):
    board = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        board.append(temp)

    board[0][0] = 1

    for i in range(len(puddles)):
        x = puddles[i][0] - 1
        y = puddles[i][1] - 1
        board[x][y] = -1

    print("전처리 전 board: ", board)

    for i in range(1, len(board[0])):
        if board[0][i] == -1:
            continue

        if board[0][i-1] == -1:
            board[0][i] = -1
        else:
            board[0][i] = board[0][i-1]

    for i in range(1, len(board)):
        if board[i][0] == -1:
            continue
        if board[i-1][0] == -1:
            board[i][0] = -1
        else:
            board[i][0] = board[i-1][0]

    print("전처리 완료된 board", board)
    """
    이 위에는 데이터 전처리
    더 깔끔하게 할 것

    이 아래로는 알고리즘
    """
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] < 0:
                continue
            elif board[i-1][j] < 0 or board[i][j-1] < 0:
                board[i][j] = max(board[i-1][j], board[i][j-1])
            else:
                board[i][j] = board[i-1][j] + board[i][j-1]

    print("정답 board: ", board)
    answer = board[-1][-1]
    if answer < 0:
        answer = 0
    return answer % 1000000007


def solution2(m, n, puddles):
    board = [[0]*(m+1) for i in range(n+1)]
    board[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 맨 첫칸
            if i == 1 and j == 1:
                continue

            # 해당 칸이 웅덩이인 경우
            if [j, i] in puddles:
                board[i][j] = 0

            # 해당 칸의 바로 위 칸의 값과, 왼쪽 칸의 값을 더한 결과를 써넣는다.
            else:
                board[i][j] = board[i-1][j] + board[i][j-1]
    answer = board[n][m]
    return answer % 1000000007


m = 4
n = 3
puddles = [[3,3], [2,5]]

print(solution2(m,n,puddles))