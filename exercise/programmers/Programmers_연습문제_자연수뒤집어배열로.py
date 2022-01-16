
def solution(n):
    str_num = str(n)
    answer = []

    for s in range(len(str_num)-1, -1, -1):
        answer.append(int(str_num[s]))
    return answer

n = 12345
solution(n)
