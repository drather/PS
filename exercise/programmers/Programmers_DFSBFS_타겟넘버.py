"""
numbers에 있는 숫자들을 더하거나 빼서, target으로 만드는 경우의 수를 리턴한다

각 숫자들을 노드로 한다.
numbers = [a, b, c, d, e]라 할 때, numbers에 0을 추가한다.
                            0
                a                            -a
            b       -b                  b               -b
        c   -c      c   -c          c   -c          c           -c
    d   -d    d   -d    d    -d    d    -d        d    -d    d    -d

이런 식의 트리를 만들고, DFS를 하면서 temp배열에 추가한 뒤, 그 합을 저장한다.
그리고 그 합이 target과 같다면, answer의 값을 1 증가시킨다.

위에 방버은 좀 오바인거같고, 재귀로 풀자
재귀식인 dfs()메소드를 만든다

"""


def solution(numbers, target):
    answer_list = [0]
    for i in numbers:
        temp_list = []
        for j in answer_list:
            temp_list.append(j + i)
            temp_list.append(j - i)
        answer_list = temp_list

    answer = answer_list.count(target)
    return answer


def solution2(numbers, target):
    answer_list = [0]

    for i in range(len(numbers)):
        temp_list = []
        for j in range(len(answer_list)):
            temp_list.append(answer_list[j] + numbers[i])
            temp_list.append(answer_list[j] - numbers[i])
        answer_list = temp_list

    answer = answer_list.count(target)
    return answer


answer = 0


def dfs(numbers, target, length, i):
    global answer
    if i == length:
        if target == sum(numbers):
            answer += 1
        return
    numbers[i] *= 1
    dfs(numbers, target, length, i+1)
    numbers[i] *= -1
    dfs(numbers, target, length, i+1)


def solution3(numbers, target):
    global answer
    length = len(numbers)
    dfs(numbers, target, length, 0)
    return answer


def my_dfs(numbers, target, length, i):
    global answer
    if i == len(numbers):
        if sum(numbers) == target:
            answer += 1
        return

    my_dfs(numbers, target, length, i+1)
    numbers[i] *= -1
    my_dfs(numbers, target, length, i+1)


def my_sol1(numbers,target):
    global answer
    length = len(numbers)
    my_dfs(numbers, target, length, 0)
    return answer


def my_sol2(number, target):
    answer_list = [0]
    for i in range(len(numbers)):
        temp_list = []
        for j in range(len(answer_list)):
            temp_list.append(answer_list[j] - numbers[i])
            temp_list.append(answer_list[j] + numbers[i])
        answer_list = temp_list

    my_answer = answer_list.count(target)
    return my_answer


numbers = [1,1,1,1,1]
target = 3
print(my_sol2(numbers, target))