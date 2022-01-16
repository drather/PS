def solution(n, answer):
    if n >= 2:
        print(n % 2)
        answer.append(n%2)
        return solution(int(n/2), answer)
    else:
        print(n)
        answer.append(n)
        return

answer = []
n = 10
solution(n, answer)
string = ""
for i in range(len(answer)):
    j = len(answer) - i - 1
    string += str(answer[j])

print(string)