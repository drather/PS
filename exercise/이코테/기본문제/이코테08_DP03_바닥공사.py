"""
DP: 점화식을 생각하자.

그림으로 그려서 풀려는 생각을 하기보다는, 그림의 의미를 파악하는데 주력하자.

n = 1 일때
- 1 * 2 타일을 놓는 방법 1가지 경우 밖에 없다.

n = 2 일때
- 1 * 2 타일을 2개 놓는 방법
- 2 * 1 타일을 2개 놓는 방법
- 2 * 2 타일을 1개 놓는 방법
- 총 3가지 방법이 있다.

n = 3 일때
- n = 2 일때의 가짓수에서, 1 * 2 블록을 옆에다 하나 놓으면 그것이 바로 n = 3 일때 경우의 수이다. 즉, a[n-1] 가지
- n = 1 일때의 가짓수에서, 2 * 1 블록을 옆에 두개 놓거나, 2 * 2 블록을 옆에 두는 것이 경우의 수이다. 즉, a[n-2] * 2 가지 이다.

위 내용을 종합해보면, n 을 i 로 일반화했을 때,
a[i] = a[i-1] + a[i-2] * 2 가 나온다.

- 이렇게 나오는 이유는, a[i] 를 결정하는데 영향을 끼치는 값이 a[i-1] , a[i-2] 이기 때문이다.
- 만약, 가로 길이 3짜리 타일이 있었다면, a[i-3] 도 영향을 끼쳤을 것이다.

- 즉, 문제의 의미를 잘 풀어서, 조건을 해석하여 점화식으로 나타내는 것이 중요하다.
"""

if __name__ == '__main__':
    width = int(input())

    dp = [0] * (width + 1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, width + 1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    print(dp[-1] % 796796)



