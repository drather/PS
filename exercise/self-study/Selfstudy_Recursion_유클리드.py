def solution(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    else:
        print(m, n)
        print(n, m % n)
        return solution(n, m%n)

print(solution(48,60))