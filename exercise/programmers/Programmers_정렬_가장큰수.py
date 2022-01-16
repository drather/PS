def solution1(numbers):
    arr = []
    max_value = max(numbers)
    max_num = len(str(max_value))
    print(max_num)

    for i in range(len(numbers)):
        arr.append(str(numbers[i]))

    arr.sort(key=lambda x: x[0], reverse=True)

    print(arr)


def sol(numbers):
    max_value = max(numbers)
    max_len = len(str(max_value))

    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    print(numbers)
    arr = []
    count = 1
    while count <= max_len:
        temp = []
        for i in range(len(numbers)):
            if len(numbers[i]) == count:
                temp.append(numbers[i])
        arr.append(temp)
        count += 1

    for i in arr:
        i.sort(key=lambda x:x[0], reverse=True)

    print(arr)


def sol2(numbers):
    table = {}

    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    for i in range(len(numbers)):
        try:
            table[int(numbers[i][0])].append(numbers[i])

        except:
            table[int(numbers[i][0])] = [numbers[i]]

    print("table: ", table)





    answer = ""
    for i in range(9, 0, -1):
        try:
            table[i]
            while table[i]:
                answer += table[i].pop()
        except:
            continue


    print("answer: ", answer)
    return answer


def solution(numbers):
    ans = []

    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    for i in range(len(numbers)):
        raw = numbers[i]
        modified = ""

        while len(modified) < 5:
            modified += raw
            if len(modified) > 5:
                modified = modified[0:5]

        print([raw, modified])
        ans.append([raw, modified])

    ans.sort(key=lambda x: x[1], reverse=True)
    print(ans)

    answer = ""
    for i in ans:
        answer += i[0]

    print(answer)
    return answer


numbers = [9,  3, 30, 310, 34, 5, ] # -> 9, 5, 34, 3, 30 으로 정렬?
# numbers = [121, 12]
print(solution(numbers))
