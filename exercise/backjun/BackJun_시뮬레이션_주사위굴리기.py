# -*- coding: utf-8 -*-

import sys

N = M = K = 0
arr = []
## 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


## x, y 좌표와 주사위 상단/하단/동/서/남/북 면에 있는 숫자
class Dice:
    def __init__(self, x, y, top, bottom, e, w, n, s):
        self.x = x
        self.y = y
        self.top = top
        self.bottom = bottom
        self.e = e
        self.w = w
        self.n = n
        self.s = s


def move(dice, d):
    nx = dice.x + dx[d]
    ny = dice.y + dy[d]

    ## 지도 밖으로 안나가야 됨
    if 0 <= nx and nx < N and 0 <= ny and ny < M:
        dice.x = nx
        dice.y = ny

        ## 동 서 북 남
        if d == 0:
            dice.top, dice.bottom, dice.w, dice.e = dice.w, dice.e, dice.bottom, dice.top
        elif d == 1:
            dice.top, dice.bottom, dice.w, dice.e = dice.e, dice.w, dice.top, dice.bottom
            pass
        elif d == 2:
            dice.top, dice.bottom, dice.n, dice.s = dice.s, dice.n, dice.top, dice.bottom
        elif d == 3:
            dice.top, dice.bottom, dice.n, dice.s = dice.n, dice.s, dice.bottom, dice.top

        ## 이동한 칸이 0이면 주사위 바닥면 복사
        ## 이동한 칸이 0이 아니면 주사위 바닥면에 숫자 복사하고 칸은 0
        if arr[dice.x][dice.y] == 0:
            arr[dice.x][dice.y] = dice.bottom
        else:
            dice.bottom = arr[dice.x][dice.y]
            arr[dice.x][dice.y] = 0
    else:
        return False

    return True


def solve(x, y, directions):
    dice = Dice(x, y, 0, 0, 0, 0, 0, 0)

    for direction in directions:
        if move(dice, direction - 1) == True:
            print(dice.top)


if __name__ == '__main__':
    N, M, x, y, K = map(int, sys.stdin.readline().split())

    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    directions = list(map(int, sys.stdin.readline().split()))

    solve(x, y, directions)