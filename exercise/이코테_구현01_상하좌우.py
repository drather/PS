# size = int(input())
# commands = list(map(str, input().split()))

size = 5
commands = ['R', 'R', 'R', 'U', 'D', 'D']

d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]
move_types = ['R', 'D', 'L', 'U']

board = [[0] * (size+1) for i in range(size+1)]

row = 1
col = 1

for i in range(len(commands)):
    for j in range(4):
        if commands[i] == move_types[j]:
            new_row = row + d_row[j]
            new_col = col + d_col[j]

            if new_row <= 0 or new_col <= 0:
                continue
            else:
                row = new_row
                col = new_col

                print(new_row, new_col)

print([row, col])