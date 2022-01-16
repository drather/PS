def solution(n, lost, reserve):
    arr = [0] * n
    for i in range(len(lost)):
        arr[lost[i] -1] -= 1

    for i in range(len(reserve)):
        arr[reserve[i]-1] += 1

    for i in range(len(arr)):
        if i == 0:
            # 0번째 학생이 체육복을 빌려야 하는데, 1번째 학생이 여벌 체육복이 있는 경우
            if arr[i] == -1 and arr[i+1] == 1:
                arr[i] += 1
                arr[i+1] -= 1

        elif i == len(arr)-1:
            # 마지막 학생이 체육복을 빌려야 하는데, 그 앞에 학생이 여벌의 체육복이 있는 경우
            if arr[i] == -1 and arr[i-1] == 1:
                arr[i] += 1
                arr[i-1] -= 1

        else:
            # 그 밖에, 양쪽에 학생이 있는 경우
            if arr[i] == -1:
                if arr[i-1] == 1:
                    arr[i] += 1
                    arr[i-1] -= 1
                    continue
                if arr[i+1] == 1:
                    arr[i] += 1
                    arr[i+1] -= 1

    print("Arr: ", arr)
    return arr.count(0) + arr.count(1)


def sol2(n, lost, reserve):
    arr = [0] * (n)
    for i in range(len(lost)):
        arr[lost[i] - 1] -= 1

    for i in range(len(reserve)):
        arr[reserve[i] - 1] += 1

    for i in range(1, len(arr)):
        pass


n = 5
lost = [2,4]
reserve = [3]

n = 3
lost = [3]
reserve = [3]
print(solution(n, lost, reserve))