def solution1(s):
    answer = ""
    splited = s.split()
    print(splited)

    for i in range(len(splited)):
        for j in range(len(splited[i])):
            print(j)
            if j % 2 == 0:
                answer += splited[i][j].upper()
            else:
                answer += splited[i][j]
        answer += " "

    print(answer)
    return answer[:-1]


def solution(s):
    count = 0
    answer = ""
    for i in range(len(s)):
        print("count: ", count)
        if s[i] == " ":
            count = 0
            answer += s[i]
            continue
        elif count % 2 == 0:
            answer += s[i].upper()
            count += 1
        else:
            answer += s[i].lower()
            count += 1

    print(answer)
    return answer



s = "try hello world"
s = "sp ace"

print("answer: ", solution(s))

