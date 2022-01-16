def solution(i, n, sum):
    if i == n:
        sum += i
        return sum
    else:
        sum += i
        return solution(i+1, n, sum)


def solution2(n):
    if n == 0:
        return 0
    else:
        return n + solution2(n-1)


i = 0
n = 4
sum = 0
print(solution(i, n, sum))
print(solution2(10))

def sol(n):
    if n == 5:
        return

    else:
        print("자기자신 호출")
        return sol(n+1)

sol(3)