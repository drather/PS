def solution(arr, commands):
    answer = []

    for i in range(len(commands)):
        num1 = commands[i][0] - 1
        num2 = commands[i][1] - 1
        num3 = commands[i][2] - 1

        temp = arr[num1: num2+1]
        temp.sort()
        answer.append(temp[num3])
    print(answer)
    return answer


arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(arr, commands)