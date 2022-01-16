answer = 0


def dfs(numbers, target, length, i):
    global answer
    if i == len(numbers):
        if (sum(numbers)) == target:
            answer += 1
            return
    else:
        dfs(numbers, target, length, i+1)
        numbers[i] *= -1
        dfs(numbers, target, length, i+1)


def recursive_solution(numbers, target):
    global answer
    length = len(numbers)
    dfs(numbers, target, length, 0)

    return answer


def iterative_solution(numbers, target):
    # result_list는 0부터 시작한다. 그리고, [0, 0-a, 0+a, 0-a-b, 0-a+b, 0+a-b, 0+a+b, ... ] 이런 식으로 간다.
    result_list = [0]

    # i는 numbers의 각 원소들
    for i in range(len(numbers)):
        temp_list = []

        # result_list는 0부터 numbers의 각 원소들을 빼고 더한 값들이 있다.
        for j in range(len(result_list)):
            temp_list.append(result_list[j] - numbers[i])
            temp_list.append(result_list[j] + numbers[i])
        result_list = temp_list

    return result_list.count(target)


numbers = [1, 1, 1, 1, 1]
target = 3
print("재귀: ", recursive_solution(numbers, target))
print("반복: ", iterative_solution(numbers, target))
