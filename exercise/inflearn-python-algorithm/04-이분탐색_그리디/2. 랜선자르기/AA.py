"""
랜선자르기(결정알고리즘)
엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이
다. 선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을
잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면
20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의
랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수
길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때
만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

▣ 입력설명
첫째 줄에는 엘리트학원이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이
입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고
항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의
정수로 입력된다.

▣ 출력설명
첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.

▣ 입력예제 1
4 11
802
743
457
539

▣ 출력예제 1
200
예제설명) 802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를
잘라내 모두 11개를 만들 수 있다.

풀이
1). 개요
이분 탐색을 사용한다.
지금 우리에게 주어진 것은, 각 랜선의 길이와 원하는 갯수이다.
이것으로 알아내야 하는 것은, 원하는 갯수 target 개를 만들기 위해서, 각 랜선을 몇 CM 으로 나눠야 할지 그 길이를 정해야 한다.
따라서, target 길이의 최소값과 최대값을 정한 뒤,
이분 탐색을 통해 target을 유추하면서,
target 으로 랜선의 각 길이를 나눈 몫을 다 더했을 때 target 이 나오는 지를 확인해야 한다.

2). 변수 설명
- left: 가능한 길이의 최소값
- right: 최대값
- mid: 예상한 길이
- exp_num: mid 의 값으로 arr 의 값을 나눠서 더한 값, 즉 갯수

3). 강의 설명
- 이분 탐색은 결정 알고리즘에 사용
- 이 경우, 답이 몇부터 몇까지 있는지 알 수 있다.
- 답의 범위를 정해놓고, 이분 검색을 쓴다.
- 답을 찍어놓고, 이 답이 정답인지 아닌지를 확인한다.

4). 강의 풀이
- k개의 랜선의 길이의 값의 범위는, 답의 범위: 1 ~ max(arr)이다.(답의 범위는 넉넉히 잡아도 상관 없다)
-

"""
import sys


def count(num):
    cnt = 0
    for x in lines:
        cnt += (x // num)

    return cnt


# sys.stdin = open("in3.txt", "rt")

line_num, target = map(int, input().split())
lines = []
for _ in range(line_num):
    lines.append(int(input()))

# line_num, target, arr = 4, 11, [802, 743, 457, 539]


# # !!!!!!!!!!!!!! 두번째 풀이 !!!!!!!!!!!!!!
# left = 1
# right = max(lines)
# answer = 0
#
# while left <= right:
#     mid = (left + right) // 2
#     if count(mid) >= target:
#         answer = mid
#         left = mid + 1
#     else:
#         right = mid - 1
#
# print(answer)


# !!!!!!!!!!!!!!!!!!!!!! 첫 번째 풀이 !!!!!!!!!!!!!!!!!!!!!!
right = max(lines)
left = 1
mid = 1
answer = 0

while left <= right:
    mid = (left + right) // 2
    # 다 합친 길이 = 원하는 갯수 * 예측 길이
    exp_num = 0

    for i in lines:
        exp_num += i // mid

    if exp_num >= target:
        answer = mid
        left = mid + 1

    elif exp_num < target:
        right = mid - 1

print(answer)