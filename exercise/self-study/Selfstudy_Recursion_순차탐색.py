def solution(arr, target, n):
    if arr[n] == target:

        return n
    else:
        return solution(arr, target, n+1)


arr = [1, 6, 10, 5, 2, 7]
target = 7
n = 0
print("target은 ", solution(arr, target, n), "에 있다.")