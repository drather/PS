"""
창고 정리
창고에 상자가 가로방향으로 일렬로 쌓여 있습니다.

만약 가로의 길이가 7이라면
1열은 높이가 6으로 6개의 상자가 쌓여 있고, 2열은 3개의 상자, 3열은 9개의 상자가 쌓여 있
으며 높이는 9라고 읽는다.
창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.
가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
위에 그림을 1회 높이 조정을 하면 다음과 같아진다.

창고의 가로 길이와 각 열의 상자 높이가 주어집니다. m회의 높이 조정을 한 후 가장 높은 곳
과 가장 낮은 곳의 차이를 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 창고 가로의 길이인 자연수 L(1<=L<=100)이 주어집니다.
두 번째 줄에 L개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 100을 넘지
않습니다
세 번째 줄에 높이 조정 횟수인 M(1<=M<=1,000)이 주어집니다.

▣ 출력설명
M회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이를 출력하세요.

▣ 입력예제 1
10
69 42 68 76 40 87 14 65 76 81
50

▣ 출력예제 1
20
"""


# width = 10
# heights = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]
# change = 50
import sys

sys.stdin = open("in1.txt", "rt")
L = int(input())
arr = list(map(int, input().split()))
m = int(input())
cnt = [0] * 101
maxH = float('-inf')
minH = float('inf')
for x in arr:
    cnt[x] += 1
    if x > maxH: maxH = x
    if x < minH: minH = x

print(cnt)

for _ in range(m):
    if cnt[maxH] == 1:
        cnt[maxH] -= 1
        maxH -= 1
        cnt[maxH] += 1
    else:
        cnt[maxH] -= 1
        cnt[maxH - 1] += 1

    if cnt[minH] == 1:
        cnt[minH] -= 1
        minH += 1
        cnt[minH] += 1
    else:
        cnt[minH] -= 1
        cnt[minH + 1] += 1

print(maxH - minH)







# !!!!!!!!!!!!!! 두 번째 풀이 !!!!!!!!!!!!!!
# import sys
# sys.stdin = open("in1.txt", "rt")
#
# width = int(input())
# heights = list(map(int, input().split()))
# change = int(input())

# !!!!!!!!!!!두 번째 풀이
#
# heights.sort()
#
# cnt = [0] * 101
# max_h = float(-21470000)
# min_h = float(21470000)

# for i in heights:
#     cnt[i] += 1
#     if i > max_h:
#         max_h = i
#     if i < min_h:
#         min_h = i
#
# for _ in range(width):
#     if cnt[max_h] == 1:
#         cnt[max_h] -= 1
#         max_h -= 1
#         cnt[min_h] += 1
#     else:
#         cnt[max_h] -= 1
#         cnt[max_h-1] += 1
#
#     if cnt[min_h] == 1:
#         cnt[min_h] -= 1
#         min_h += 1
#         cnt[min_h] -= 1
#
#     else:
#         cnt[min_h] -= 1
#         cnt[min_h] += 1
#
# print(min_h - max_h)

# !!!!!!!!!!!!!! 첫 번째 풀이 !!!!!!!!!!!!!!
# heights.sort()
# for i in range(change):
#     print("\n", heights)
#     print(sum(heights))
#     heights[0] += 1
#     heights[-1] -= 1
#
#     if heights[0] > heights[1]:
#         heights[0], heights[1] = heights[1], heights[0]
#
#     if heights[-1] < heights[-2]:
#         heights[-1], heights[-2] = heights[-2], heights[-1]
#
# print(heights[-1] - heights[0])




