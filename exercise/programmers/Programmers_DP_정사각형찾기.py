def solution2(board):
    max_point=0
    for i in range(len(board)):
        max_point+=sum(board[i][:])
    if max_point==0:
        return 0
    max_point=0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]==0:
                continue
            else:
                min_point=min(board[i][j-1],board[i-1][j],board[i-1][j-1])
                min_point+=1
                board[i][j]=min_point
                if max_point < board[i][j]:
                    max_point=board[i][j]
    if max_point==0:
        return 1
    else:
        return max_point**2


def solution3(board):
    max_value = 0
    # 이 경우는, board의 모든 원소가 0인 경우 0을 리턴하기 위해서 만든 부분이다.
    for i in range(len(board)):
        max_value += sum(board[i][:])
    if max_value == 0:
        return 0

    #
    max_value = 0
    # i, j 두 인덱스를 통해서, board[1][1]부터 board의 마지막 원소까지 반복한다.
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            # board[i][j]가 0이라면, continue한다.
            if board[i][j] == 0:
                continue

            # 그렇지 않다면, 위의 원소, 왼쪽 원소, 왼쪽 위의 원소 3가지를 비교한다.
            # 그리고 그 중 최소값을 뽑아서, 그 최소값에 1을 더한 값을 board[i][j]에 넣는다.
            else:
                min_value = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
                board[i][j] = min_value + 1

                # 그리고, 최대값을 저장해두기 위해 board[i][j]가 나올 때마다 최대값인지 아닌지를 판단해서 저장한다.
                if max_value < board[i][j]:
                    max_value = board[i][j]

    print(board)
    if max_value == 0:
        return 1
    else:
        return max_value**2


board = [[0,1,1,1], [1,1,1,1], [1,1,1,1], [0,0,1,0]]
print(solution3(board))