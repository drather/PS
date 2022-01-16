def solution(n):
    answer = ''
    if n % 2 == 1:
        for i in range(n//2):
            answer += "수박"
        answer += "수"

    else:
        for i in range(n//2):
            answer += "수박"

    return answer

n = 5
print(solution(n))
