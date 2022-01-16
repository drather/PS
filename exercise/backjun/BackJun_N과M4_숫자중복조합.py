def dfs(level):
    if level == limit:
        for r in result:
            print(r, end=" ")
        print()

    else:
        for i in range(num+1):
            result[level] = i
            dfs(level+1)


if __name__ == "__main__":
    num, limit = map(int, input().split())

    check = [0] * (num+1)
    result = [0] * limit

    dfs(1)