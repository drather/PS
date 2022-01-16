def dfs(level):
    # print("\nlevel: ", level)
    # print("Result: ", result)
    if level == length:
        for i in range(len(result)):
            print(result[i], end=" ")
        print()

    else:
        for i in range(1, num+1):
            if check[i] == 0:
                check[i] = 1
                result[level] = i
                dfs(level+1)
                check[i] = 0


if __name__ == "__main__":
    # num, length = map(int, input().split())
    num, length = 3, 2

    result = [0] * length
    check = [0] * (num+1)
    dfs(0)

