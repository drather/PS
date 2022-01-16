def solution(answers):
    # 1번: 1,2,3,4,5,1,2,3,4,5
    # 2번: 2,1,2,3,2,4,2,5,2,1,2,3
    # 3번: 3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5
    answer = []

    question_num = len(answers)
    cand1 = []
    cand2 = [0] * question_num
    cand3 = [0] * question_num

    i = 0
    while i < question_num:
        temp = i % 5
        if temp == 0:
            cand1.append(1)
        elif temp == 1:
            cand1.append(2)
        elif temp == 2:
            cand1.append(3)
        elif temp == 3:
            cand1.append(4)
        elif temp == 4:
            cand1.append(5)
        i += 1

    i = 0
    while i < question_num:
        temp = i % 8

        if i % 2 == 0:
            cand2[i] = 2
        elif temp == 1:
            cand2[i] = 1
        elif temp == 3:
            cand2[i] = 3
        elif temp == 5:
            cand2[i] = 4
        elif temp == 7:
            cand2[i] = 5
        i += 1

    i = 0
    while i < question_num:
        temp = i % 10
        if temp == 0 or temp == 1:
            cand3[i] = 3
        elif temp == 2 or temp == 3:
            cand3[i] = 1
        elif temp == 4 or temp == 5:
            cand3[i] = 2
        elif temp == 6 or temp == 7:
            cand3[i] = 4
        elif temp == 8 or temp == 9:
            cand3[i] = 5
        i += 1

    score1 = 0
    score2 = 0
    score3 = 0

    for i in range(len(answers)):
        if cand1[i] == answers[i]:
            score1 += 1
        if cand2[i] == answers[i]:
            score2 += 1
        if cand3[i] == answers[i]:
            score3 += 1

    # 디버깅 위해 score임의 설정


    # 점수, 사람
    score_list = [[score1,1], [score2,2], [score3,3]]
    # score_list = [[10, 1], [10, 2], [8,3]]
    score_list.sort(reverse=True)
    print("점수, 사람(정렬 후)")
    print(score_list)

    if score_list[0][0] == score_list[1][0] and score_list[1][0] ==  score_list[2][0]:
        answer = [1, 2, 3]

    elif score_list[0][0] == score_list[1][0]:
        answer = [score_list[0][1], score_list[1][1]]
        answer.sort()

    else:
        answer.append(score_list[0][1])

    print('answer: ', answer)
    return answer

answers = [1,2,3,4,5]
print(solution(answers))