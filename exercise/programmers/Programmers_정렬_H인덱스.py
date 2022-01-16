def solution(citations):
    answers = []
    citations.sort()
    print("citations: ", citations)
    h_max = max(citations)
    h_idx = 0

    flag = False
    for i in citations:
        if i != 0:
            flag = True
            break

    if not flag:
        return 0

    while h_idx <= h_max:
        temp = 0
        for i in range(len(citations)):
            if h_idx <= citations[i]:
                temp += 1

        if h_idx == temp:
            answers.append(temp)

        h_idx += 1

    print(answers)
    if answers:
        return max(answers)
    else:
        return citations[len(citations)//2]


citations = [3, 0, 6, 1, 5]
citations = [0, 1, 3, 5, 6]
citations = [1, 1, 1, 1, 1]
citations = [2, 2, 2, 2, 2]
citations = [3, 3, 3]
citations = [0, 1, 1, 1, 1, 3, 3, 4]
citations = [6, 6, 6, 6, 6]

print(solution(citations))