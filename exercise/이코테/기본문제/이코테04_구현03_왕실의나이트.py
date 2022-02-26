pos = input()


row, col = int(pos[1]), pos[0]
col_table = {'a': 1,
             'b': 2,
             'c': 3,
             'd': 4,
             'e': 5,
             'f': 6,
             'g': 7,
             'h': 8}

col = col_table[col]

print(f"row: {row}, col: {col}")

d_row = [-1, 1, 2, 2, -1, 1, -2, -2]
d_col = [2, 2, 1, -1, -2, -2, -1, 1]

answer = 0

for i in range(8):
    new_row = row + d_row[i]
    new_col = col + d_col[i]

    if 0 < new_row <= 8 and 0 < new_col <= 8:
        answer += 1

print(answer)



