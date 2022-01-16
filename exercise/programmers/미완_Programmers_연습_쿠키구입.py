def solution(cookie):
    answer = 0
    cookie.sort()

    temp = 0
    flag = False
    for i in range(len(cookie)-1, -1, -1):
        print("\ni: ", i)
        temp = cookie[i]
        print("temp: ", temp)
        res = 0
        for j in range(i-1, -1, -1):
            print("j: ", j)
            res += cookie[j]
            print("Res: ", res)
            if temp == res:
                return res
    else:
        return 0


cookie = [1, 1, 2, 3]
cookie = [1, 2, 4, 5]
cookie = [21, 19, 2, 10]
print(solution(cookie))
