import sys
sys.stdin = open("input2.txt")

T = int(input())


def is_done(arr):
    for idx in range(len(arr)-1):
        if arr[idx] % 2 == arr[idx+1] % 2:
            return False
    return True


for test_case in range(1, T + 1):
    #######################################################################################################
    #  이 부분에 여러분의 알고리즘 구현이 들어갑니다.
    result = 0
    length = int(input())
    arr = list(map(int, input().split()))
    print(length, arr)

    odd_count = 0
    even_count = 0

    for i in arr:
        if i % 2 != 0:
            odd_count += 1

        if i % 2 == 0:
            even_count += 1
    # print('홀, 짝:', odd_count, even_count)

    # 길이가 1인경우, 무조건 가능 및 횟수 0
    if length == 1:
        result = 0

    # 홀, 짝 갯수가 2개 이상 차이나는 경우, 불가, -1
    elif max(odd_count, even_count) - min(odd_count, even_count) >= 2:
        result = -1

    # 판별
    else:
        while not is_done(arr):
            for i in range(1, length - 1):
                current_num = arr[i]
                prev_num = arr[i-1]
                next_num = arr[i+1]

                if current_num % 2 == prev_num % 2 and current_num % 2 != next_num % 2:
                    # print(f"switch, {i}, {i+1}")
                    arr[i], arr[i+1] = next_num, current_num
                    result += 1
                    break

        print(f"결과 arr: {arr}")

    #######################################################################################################
    # 표준출력(화면)으로 답안을 출력합니다.
    print("#%d" % test_case + f' {result}')