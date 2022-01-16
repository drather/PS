# 제일 큰거 찾아서 1씩 감소하면 될거같은데?
def solution1(n, works):
    if sum(works) < n:
        return 0

    answer = 0
    while n > 0:
        n -= 1
        max_value = max(works)
        print("\nmax_value: ", max_value)
        idx = works.index(max_value)
        print("idx: ", idx)
        works[idx] -= 1
        print("works: ", works)

    for i in works:
        answer += i ** 2

    print("answer :", answer)
    return answer

def solution2(n, works):
    temp = sum(works) - n
    if temp < 0:
        return 0

    length = len(works)
    mok = temp // length
    min_value = mok * length
    rest = temp - min_value

    print("works 배열의 총 합에서 n을 뺸 값: ", temp)
    print("works 원소의 갯수: ", length)
    print("works 배열에 기본으로 깔릴 몫: ", mok)
    print("한번씩 더할 나머지: ", rest)

    for i in range(len(works)):
        if works[i] > mok:
            works[i] = mok

    print("나머지를 더할  works: ", works)
    idx = 0
    while rest > 0:
        print("나머지: ", rest)
        rest -= 1
        works[idx] += 1
        idx += 1
        print("works: ", works)
        if idx == len(works):
            idx = 0


    print("나머지 더한 works: ", works)

    answer = 0
    for i in works:
        answer += i ** 2

    print("answer: ", answer)
    return answer


def solution(n, works):
    works.append(0)
    works.sort()
    print("works: ", works)
    for i in range(len(works)-1, 2, -1):
        print("i: ", i)
        diff = works[i] - works[i-1]
        print("diff: ", diff)
        if diff > n:
            pass

    print("결과: ", works)


works= [4, 3, 3]
# works = [1, 1]
n = 4
print(solution(n, works))