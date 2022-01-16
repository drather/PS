def solution(s):
    # 결과 값
    answer = 0
    # 문제 해결을 위한 자료구조로 스택을 선택
    stack = []

    for i in range(len(s)):
        # 스택에 문자열의 문자를 하나씩 집어넣는다.
        stack.append(s[i])

        # 스택에 문자가 1개 이하로 남아있다면, 별 다른 행동을 하지 않고 넘어간다.
        if len(stack) < 2:
            continue

        # 스택에 2개 이상의 문자가 있고, 스택의 가장 위에 있는 데이터 2개가 서로 같다면 그 2개를 없앤다.
        elif stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    # 반복이 끝난 후, stack의 길이가 0이면 문자가 모두 제거된 것이므로 1을 리턴한다.
    if len(stack) == 0:
        answer = 1

    # 그렇지 않다면 문자가 남아있는 것이므로 0을 리턴한다.
    else:
        answer = 0
    return answer

s = "baabaa"
print("결과: ", solution(s))
