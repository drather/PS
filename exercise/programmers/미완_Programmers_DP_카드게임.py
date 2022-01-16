def solution(left, right):
    answer = 0
    left_max = max(left)
    left_max_index = left.index(left_max)
    left = left[left_max_index:]

    right_max = max(right)
    right_max_index = right.index(right_max)

    while left and right:
        if left_max > right[0]:
            answer += right[0]

        del right[0]

    print("answer: ", answer)
    return answer


left = [3, 2, 5]
right = [2, 4, 1]

left = [1, 1, 1, 1, 3]
right = [2, 3, 1, 1, 1]
print(solution(left, right))