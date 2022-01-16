# https://programmers.co.kr/learn/courses/30/lessons/42588
def solution(heights):
    answer = [0] * len(heights)
    i = len(heights) - 1
    while i > 0:
        temp = heights[i]
        j = i - 1
        while j >= 0:
            if temp < heights[j]:
                answer[i] = j+1
                break
            else:
                j -= 1
        i -= 1
    return answer


heights =[6,9,5,7,4]
print(solution(heights))
