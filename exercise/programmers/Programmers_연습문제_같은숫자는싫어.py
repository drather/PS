def solution(arr):
    answer = []

    stack = []

    for i in range(len(arr)):
        stack.append(arr[i])

        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()

    return stack


arr = [1, 1, 3, 3, 0, 1, 1]
# arr = [4, 4, 4, 3, 3]
print(solution(arr))
