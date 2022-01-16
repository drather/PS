def solution(arr, n, sum):
    if n == len(arr) - 1:
        sum += arr[n]
        return sum

    else:
        sum += arr[n]
        return solution(arr, n + 1, sum)


def solution2(arr, i):
    if i == len(arr) - 1:
        return arr[i]
    else:
        return arr[i] + solution2(arr, i + 1)


arr = [1, 2, 3, 4, 5, 6]
print("sum: ", sum(arr))
sum = 0
n = 0
i = 0
print(solution(arr, n, sum))
print(solution2(arr, i))
