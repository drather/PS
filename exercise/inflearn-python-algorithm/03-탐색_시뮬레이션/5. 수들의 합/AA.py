"""
수들의 합
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의
합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

▣ 입력설명
첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …,
A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

▣ 출력설명
첫째 줄에 경우의 수를 출력한다.

▣ 입력예제 1
8 3
1 2 1 3 1 1 1 2

▣ 출력예제 1
5


#############################
풀이
매 단계에서 합을 구하면 시간 초과가 발생한다.
따라서, 한 단계에서 구한 totol 값과 target과의 비교를 통해서 다음과 같이 조치한다.
1. total > target
- total에서 arr[ldx]를 뺀다.
- ldx 의 값을 1 증가

2. total == target
- answer 1 증가
- total에서 arr[ldx]를 뺀다
- ldx 1 증가

3. total < target
- rdx의 값이 인덱스 범위를 초과하지 않았다면
    total 에 arr[rdx]를 더한다
    rdx 를 1 증가시킨다
- rdx의 값이 인덱스 범위를 초과했다면
    break 한다.
"""

import sys
sys.stdin = open("in5.txt", "rt")

len_arr, target = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start_idx = 0

ldx = 0
rdx = 1
total = arr[ldx]

while True:
    if total < target:
        if rdx < len_arr:
            total += arr[rdx]
            rdx += 1
        else:
            break

    elif total == target:
        answer += 1
        total -= arr[ldx]
        ldx += 1

    else:
        total -= arr[ldx]
        ldx += 1

print(answer)








# for _ in range(len(arr)):
#     end_idx = start_idx + 1
#     mid_sum = arr[start_idx]
#
#     while end_idx < len_arr:
#         mid_sum += arr[end_idx]
#         if mid_sum > target:
#             start_idx += 1
#             break
#
#         elif mid_sum < target:
#             end_idx += 1
#
#         else:
#             answer += 1
#             start_idx += 1
#             break
#
# print(answer)











