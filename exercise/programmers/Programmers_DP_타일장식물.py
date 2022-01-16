# 둘레는 피보나치 수열의 뒤에서부터 3개의 원소들로 구할 수 있다. 

def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = -1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    answer = 2 * (dp[-1] + dp[-1] + dp[-2])

    return answer


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def dp_fibonacci(n):
    dp = [0] * n
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]

n = 5
print("정답: ", solution(n))