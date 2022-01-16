def solution(n):
    print(n)
    if n == 1:
        return 1
    else:
        print("Return, ", n)
        return n * solution(n-1)
n = 5
print(solution(n))