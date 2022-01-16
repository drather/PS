def solution(n, count):
    if count == 9:
        print(n, "*", count, "=", n*count)
        return
    else:
        print(n, "*", count, "=", n*count)
        return solution(n, count+1)


n = 3
count = 1
solution(n, count)