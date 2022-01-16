def solution1(x, n, i, res):
    if i == n:
        res *= x
        return res

    else:
        res *= x
        return solution1(x, n, i+1, res)

def solution2(x, n):
    if n == 0:
        return 1
    else:
        return x * solution2(x, n-1)

x = 5
i = 1
n = 4
res = 1
print(solution2(x,n))