def dfs(level, start):
    # print("level: ", level)
    if level == limit:
        for r in result:
            print(r, end=" ")
        print()

    else:
        for i in range(start, num+1):
            if check[i] == 0:
                check[i] = 1
                result[level] = i
                dfs(level+1, i+1)
                check[i] = 0

if __name__ == "__main__":
    num, limit = map(int, input().split())
    # num, limit = 3, 2

    result = [0] * limit
    check = [0] * (num+1)
    # print(result)
    # print(check)
    dfs(0, 1)
