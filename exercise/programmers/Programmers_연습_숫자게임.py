def solution(a, b):
    length = len(a)
    answer = 0
    a.sort()
    b.sort()


    print("a: ", a)
    print("b: ", b)

    for i in a:
        for j in b:
            if i < j:
                answer += 1
                b.remove(j)
                break

    return answer


a = [5, 1, 3, 7]
b = [2, 2, 6, 8]
print(solution(a, b))