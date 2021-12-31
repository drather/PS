answer = 0
n, k = map(int, input().split())

while True:
    if n == 1:
        break

    else:
        temp = n % k
        # print(f"temp: {temp}")
        if temp == 0:
            n = n // k
        else:
            n -= 1
        answer += 1
        # print(f"n: {n}")

print(f"answer: {answer}")

