def solution(left, right):
    dp = [[-1 for _ in range(len(right)+1)] for _ in range(len(left)+1)]
    dp[0][0] = 0
    answer = 0
    for i in dp:
        print(i)

    for i in range(len(left)):
        for j in range(len(right)):
            print("\ni, j: ", i, j)
            print("left[i]: ", left[i])
            print("right[j]: ", right[j])

            if dp[i][j] == -1:
                continue

            if left[i] > right[j] and dp[i][j+1] < dp[i][j] + right[j]:
                dp[i][j+1] = dp[i][j] + right[j]

            if dp[i+1][j+1] < dp[i][j]:
                dp[i+1][j+1] = dp[i][j]

            if dp[i+1][j] < dp[i][j]:
                dp[i+1][j] = dp[i][j]

            for _ in dp:
                print(_)

    for i in range(len(left)):
        if dp[i][len(right)] > answer:
            answer = dp[i][len(right)]

        if dp[i][len(left)] > answer:
            answer = dp[i][len(left)]

    return answer


left = [3, 2, 5]
right = [2, 4, 1]

# left = [1, 1, 1, 1, 3]
# right = [2, 3, 1, 1, 1]

# left = [3, 3, 1]
# right = [7, 7, 1]
print(solution(left, right))
