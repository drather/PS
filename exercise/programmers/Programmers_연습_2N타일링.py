def solution(n):
    dp = [0] * (n+1)
    dp[0], dp[1], dp[2] = 0, 1, 2
    print(dp)
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])

    return dp[n] % 1000000007


def solution2(n):
    a, b = 1, 2
    for i in range(3, n+1):
        a, b = b, a+b

    return b % 10007


n = 9

# 이건 백준
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b % 10007, (a+b) % 10007

    return b


print(sol(n))
