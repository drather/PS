def is_start(index, arr):
    if index == 0 or arr[index - 1] < arr[index]:
        return True
    return False


def is_end(index, arr):
    if index == len(arr) - 1 or arr[index+1] > arr[index]:
        return True
    return False


if __name__ == '__main__':
    # length, target = map(int, input().split())
    # arr = list(map(int, input().split()))

    length, target = 7, 2
    arr = [1, 1, 2, 2, 2, 2, 3]

    left = 0
    right = length - 1

    start_point = None
    end_point = None

    # 시작 점 찾기
    while left <= right:
        middle = (left + right) // 2
