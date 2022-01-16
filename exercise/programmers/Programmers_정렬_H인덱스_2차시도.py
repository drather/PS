def solution(citations):
    answers = []
    citations.sort()

    h_idx = len(citations) - 1
    h_max = max(citations)

    flag = False
    for i in citations:
        if i != 0:
            flag = True
            break

    if not flag:
        return 0

    while h_max >= 0:
        temp = 0
        for i in citations:
            if i >= h_max:
                temp += 1

            if h_max == temp:
                return temp

        h_max -= 1


citations = [3, 0, 6, 1, 5]
print(solution(citations))