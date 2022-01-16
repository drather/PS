answer = []


def recursive(n):
    global answer
    print("answer: ", answer)
    print("\nn: ", n)

    if n == 1:
        answer.append("1")
        return

    if n == 2:
        answer.append("2")
        return

    if n == 3:
        answer.append("4")
        return

    else:
        temp = n % 3
        print("나머지인 temp: ", temp)
        if temp == 1:
            answer.append("1")
            recursive((n // 3))

        if temp == 2:
            answer.append("2")
            recursive((n//3))

        if temp == 0:
            answer.append("4")
            recursive((n//3) - 1)


def solution(n):
    recursive(n)
    answer.reverse()
    result = ""
    for ans in answer:
        result += ans

    return result


n = 18
print("정답: ", solution(n))
