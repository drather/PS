rows = 3
cols = 3
cards = [[3, 1, 2],
         [4, 1, 4],
         [2, 2, 2]]

rows = 2
cols = 4
cards = [[7, 3, 1, 8],
         [3, 3, 3, 4]]

# rows, cols = map(int, input().split())
# cards = list(map(int, input().split()))

min_value = 100001
for i in range(rows):
    temp = min(cards[i])
    if temp < min_value:
        min_value = temp

print(temp)