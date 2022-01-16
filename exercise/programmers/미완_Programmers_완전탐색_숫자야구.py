from itertools import permutations


def check_position(str1, str2):
    pass


def check_value(str1, str2):
    pass


def solution(baseball):
    answers = []
    temp = ""

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                temp = str(i) + str(j) + str(k)
                answers.append(temp)

    for i in range(len(baseball)):
        pred = baseball[i][0]
        strike = baseball[i][1]
        ball = baseball[i][2]

    print(answers)


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))