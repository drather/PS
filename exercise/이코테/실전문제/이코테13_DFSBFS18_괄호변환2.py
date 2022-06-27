def divide(string):
    _str1 = ""
    _str2 = ""

    start = 0
    end = 2

    while True:
        temp = string[start:end]
        # print("Temp: ", temp)
        if check(temp) == 1 or check(temp) == 2:
            _str1 = temp
            _str2 = string[end:]
            break

        else:
            end += 2

    return _str1, _str2

def solution(p):
    global answer

    # print("\nstring: ", p)

    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == "":
        return ""

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    else:
        u, v = map(str, divide(p))
        # print("u, v: ", (u, v))

        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        if check(u) == 2:
            temp = u
            res = solution(v)
            # print("temp, res, temp+res: ", temp, res, temp+res)
            return temp + res

        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
        else:
            temp = "(" + solution(v) + ")"

            u_conv = ""
            for s in u[1:-1]:
                if s == "(":
                    u_conv += ")"
                else:
                    u_conv += "("

            temp += u_conv

            # print("temp: ", temp)
            return temp


def check(string):
    cnt1 = 0
    cnt2 = 0
    stack = []
    if not string:
        return 0

    for i in string:
        if i == "(":
            cnt1 += 1
        if i == ")":
            cnt2 += 1

        stack.append(i)
        if len(stack) < 2:
            continue
        else:
            if stack[-1] == ")" and stack[-2] == "(":
                stack.pop()
                stack.pop()

    # 이상한 문자열(X)
    if cnt1 != cnt2:
        return 0

    if cnt1 == cnt2:
        # 균형잡힌 문자열
        if stack:
            return 1

        # 올바른 문자열
        else:
            return 2


if __name__ == '__main__':

    string = "()))((()"
    answer = solution(string)

    print(answer)

    # inputs = ["(()())()", ")(", "()))((()"]
    # results = ["(()())()", "()", "()(())()"]
    #
    # for i in range(len(inputs)):
    #     if solution(inputs[i]) == results[i]:
    #         print(f"{i} case 정답")
    #     else:
    #         print(f"{i} case 오답")
    #

