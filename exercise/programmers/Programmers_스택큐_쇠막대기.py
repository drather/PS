def solution(arr):
    answer = 0
    arr = list(arr)
    data = []

    # 주어진 문자열을 배열로 다루기 위해서 list로 바꾸고, 각각의 원소를 순회한다.
    # 순회하면서, 여는 괄호는 l, 닫는 괄호는 r, 레이저를 나타내는 ()는 c로 바꿔서 data배열에 append한다.
    i = 0
    while True:
        if i >= len(arr):
            break;
        if arr[i] == "(" and arr[i + 1] == ")":
            data.append("c")
            i += 1
        elif arr[i] == "(":
            data.append("l")
        elif arr[i] == ")":
            data.append("r")
        i += 1

    print("data: ", data)

    stick_num = 0

    # stick_num은 현재 절단기에 올라가 있는 막대기의 갯수를 의미한다.
    # data배열을 돌면서, 어떤 원소인지에 따라 그에 맞는 행동을 취한다.
    for i in range(len(data)):

        # 원소가 l일 경우, 막대기 하나가 시작되었음을 의미한다. 따라서, stick_num을 1 증가시켜주고, answer 또한 증가시켜준다.
        if data[i] == "l":
            print("---막대 하나 시작---")
            stick_num += 1
            answer += 1

            print("stick_num: ", stick_num)
            print("asnwer: ", answer)
            print("\n")

        # c일 경우, 레이저가 있음을 의미한다. 레이저가 3개의 쇠막대기를 자르면, 3개만큼 answer값이 증가한다.
        # 즉, c를 만날 때마다 answer 에 stick_num을 더해야 함을 의미한다.
        if data[i] == "c":
            print("---커팅---")
            answer += stick_num

            print("stick_num: ", stick_num)
            print("asnwer: ", answer)
            print("\n")

        # r일 경우, 하나의 막대기가 끝났음을 의미한다.
        # 이 경우, 현재 절단기에 올라와있는 막대의 갯수를 의미하는 stick_num을 1 감소시킨다.
        if data[i] == "r":
            stick_num -= 1

            print("---막대기 하나 끝---")
            print("stick_num: ", stick_num)
            print("asnwer: ", answer)
            print("\n")

    return answer


arr = "()(((()())(())()))(())"
print(solution(arr))