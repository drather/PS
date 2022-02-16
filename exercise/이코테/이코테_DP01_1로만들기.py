# num = int(input())
num = 26


if __name__ == '__main__':
    d = [0] * 50000

    for i in range(2, num+1):
        d[i] = d[i-1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)

        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)

        if i % 2 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    print(d[num])

