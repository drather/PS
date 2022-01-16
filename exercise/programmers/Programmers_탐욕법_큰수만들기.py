def solution(number, k):
    answer = ""
    temp = []
    # numbers에 있는 문자들을 정수로 바꿔서, temp 배열에 넣어준다.
    for i in range(len(number)):
        temp.append(str(number[i]))

    # list형인 stack에 하나씩 넣어보면서, 각 경우에 맞는 조치를 취할 것이다.
    stack = []
    for i in range(len(temp)):
        stack.append(temp[i])
        print("\ntemp[i]: ", temp[i])

        # stack에 원소가 1개밖에 없는 경우, 다른 원소가 비교할 수 없으므로 continue한다.
        if len(stack) < 2:
            continue

        # 그렇지 않다면,
        else:
            # 아직 제거해야 하는 숫자 k만큼 제거하지 않았고, stack의 마지막 원소가 그 앞 원소보다 값이 크다면
            # stack[-2]를 pop하고 k의 값을 1 감소시킨다.
            # stack의 길이가 1이 되었다면, stack[-2]를 pop할 수 없으므로 break한다.
            while k > 0 and stack[-1] > stack[-2]:
                ks = stack.pop(-2)
                print(ks, "빠짐")
                k -= 1
                if len(stack) == 1:
                    break
        print(stack)
    # 아직 k가 남아있을 경우, stack에서 가작 작은 수를 제거하고, 그 때마다 k의 값을 1 감소시킨다.
    while k > 0:
        print(stack)
        stack.remove(min(stack))
        k -= 1

    # stack의 원소를 문자로 바꿔서 answer에 붙여넣는다.
    for i in range(len(stack)):
        answer += str(stack[i])
    return answer

number = "4177252841"
k = 4
# number = "1111"
# k = 2
print(solution(number, k))