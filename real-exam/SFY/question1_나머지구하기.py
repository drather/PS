import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    #######################################################################################################
    result = 0
    length = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, length-1):
        for j in range(i+1, length):
            tmp1 = arr[i] % arr[j]
            tmp2 = arr[j] % arr[i]
            # print(f"부분합1: {tmp1 + tmp2}")

            result += tmp1
            result += tmp2
        # print(f"부분합2: {result}")

    #######################################################################################################

    # 표준출력(화면)으로 답안을 출력합니다.
    print("#%d" % test_case + f' {result}')
